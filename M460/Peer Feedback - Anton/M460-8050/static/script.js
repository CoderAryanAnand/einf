var socket = io();
var form = document.getElementById('form')
var input = document.getElementById('content')
var messagesList = document.getElementById('messages');

messagesList.scrollTop = messagesList.scrollHeight;

form.addEventListener('submit', function(e) {
    e.preventDefault();
    if (input.value) {
        socket.emit('new_message', {content: input.value});
        input.value = '';
    }
});

messagesList.addEventListener('click', function(e) {
    if (e.target && e.target.classList.contains('delete_msg')) {
        socket.emit('msg_deleted', {id: e.target.value});        
    }

});

socket.on('receive_message', function(data) {
    var item = document.createElement('li');
    item.id = 'msg-' + data.id;
    var time = data.timestamp.slice(11, 16);
    item.innerHTML = '<strong>' + data.username + '</strong><small> sent at: </small>' + time + '<br>' + data.content + ' ';

    if (data.user_id == current_user_id) {
        item.innerHTML += '<button type="button" class="delete_msg" value="' + data.id + '"> 🗑️ </button>';
    }
    messagesList.appendChild(item);
    messagesList.scrollTop = messagesList.scrollHeight;
});

socket.on('delete_html_msg', function(msg) {
    console.log("delete_html_msg received:", msg);
    var btn = document.getElementById('msg-' + msg.message_id);
    if (btn) {
        btn.remove();
        console.log("button exists");
    }
    else {
        console.log("no button");
    }
    messagesList.scrollTop = messagesList.scrollHeight;
});

socket.on('user_connected', function(data) {
    if (document.getElementById('user-' + data.username)) {
        console.log('bing bang bong')    
        return;
    }
    console.log('bing bang bong')
    var online = document.getElementById('online');
    var item = document.createElement('li');
    item.id = 'user-' + data.username;
    item.innerHTML = '<strong>' + data.username + '</strong>';
    online.appendChild(item);
});

socket.on('user_disconnected', function(data) {
    var onlineList = document.getElementById('online');
    var item = document.getElementById('user-' + data.username);
    if (item) {
        onlineList.removeChild(item);
    }
});