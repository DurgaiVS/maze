from stack import Stack

x = Stack()
x.put(1)
x.put(5)
x.put(4)
x.put(3)
x.put(2)
x.append(6)

print(x.get())
print(x.get())
print(x.get())
print(x.empty())

print(x.get())
print(x.get())
print(x.empty())
