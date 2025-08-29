"""
Der Fehler ist das a zuerst den Wert von b erhält, und dann mit b addiert wird. Das heisst, man addiert einfach b die ganze Zeit. 
Man muss den Wert von b speichern bevor man zu es addiert, aber es darf nicht in a gespeichert werden, da man diese Variable auch für die Addition braucht.
Also speichert man es in einer anderen Variable, welches dann, nach der Addition, in a gespeichert wird.
"""

def print_fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        c = b
        b = a + b
        a = c

# Print the first 5 Fibonacci numbers
print_fibonacci(5)