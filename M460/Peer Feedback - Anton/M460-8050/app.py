from flask import Flask, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
import os
import re
from werkzeug.security import generate_password_hash, check_password_hash

from flask_socketio import SocketIO, emit

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'mlg.db')

app = Flask(__name__)
app.secret_key= 'i_am_craaazy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
db = SQLAlchemy()
db.init_app(app)

socketio = SocketIO(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(32), unique=True, nullable=False)
    Password = db.Column(db.String(256), nullable=False)
    online = db.Column(db.Boolean, default=False)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, server_default=func.now())

@app.route('/login', methods=('GET', 'POST'))
def login():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(Username=username).first()
        if user and check_password_hash(user.Password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            message = "Username or password didn't match."
    return render_template('login.html', message=message)

@app.route('/register', methods=('GET', 'POST'))
def register():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username:
            message = "Please enter a username."
        elif not re.match(r'^[A-Za-z0-9_!]+$', username):
            message = "Username can only contain English letters, numbers, underscores and exclamation marks."
        elif not password:
            message = "Please enter a password."
        elif User.query.filter_by(Username=username).first():
            message = "Username already exists."
        else:
            new_user = User(Username=username, Password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return redirect(url_for('dashboard'))
    return render_template('register.html', message=message)

@app.route('/', methods=['GET'])
def dashboard():

    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = db.session.get(User, session['user_id'])
    if not user:
        session.clear()
        return redirect(url_for('login'))
    
    messages = Message.query.order_by(Message.timestamp.asc()).all()
    
    message_list = []
    for message in messages:
        author = db.session.get(User, message.user_id)
        message_list.append({
            'username': author.Username if author else 'Deleted User', 
            'content': message.content,
            'timestamp': str(message.timestamp),
            'id': message.id,
            'user_id': user.id
        })

    online_users = User.query.filter_by(online=True).all()

    return render_template('index.html', messages=message_list, online_users=online_users, username = user.Username if user else 'no user')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/delete_acc')
def delete_acc():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = db.session.get(User, user_id)
    if user:
        socketio.emit('user_disconnected', {'username': user.Username})
        user.online = False
        db.session.delete(user)
        db.session.commit()
    
    session.clear()
    return redirect(url_for('login'))

@socketio.on('new_message')
def save_message(data):
    if 'user_id' not in session:
        return
    
    content = data['content']
    user_id = session['user_id']

    if content:
        new_message = Message(user_id=user_id, content=content)
        db.session.add(new_message)
        db.session.commit()

        user = db.session.get(User, user_id)
        username = user.Username

        emit('receive_message', {
            'username': username,
            'content': content,
            'timestamp': str(new_message.timestamp),
            'id': new_message.id,
            'user_id': user_id
        }, broadcast=True)

@socketio.on('msg_deleted')
def delete_message(data):
    if 'user_id' not in session:
        return
    
    message_id = int(data['id'])

    msg = db.session.get(Message, message_id)
    if msg:
        db.session.delete(msg)
        db.session.commit()
        emit('delete_html_msg', {'message_id': message_id}, broadcast=True)

@socketio.on('connect')
def handle_connect():
    user_id = session.get('user_id')
    if not user_id:
        return

    current_user = db.session.get(User, user_id)

    if current_user:
        current_user.online = True
        db.session.commit()
        emit('user_connected', {'username': current_user.Username}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    user_id = session.get('user_id')
    if not user_id:
        return

    current_user = db.session.get(User, user_id)
    if current_user:
        current_user.online = False
        db.session.commit()
        emit('user_disconnected', {'username': current_user.Username}, broadcast=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, host="0.0.0.0", port=8001, debug=True)