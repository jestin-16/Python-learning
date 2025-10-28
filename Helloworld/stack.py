class Stack:
    def __init__(self, max_size=5):
        self.stack = [None] * max_size
        self.top = -1
        self.max = max_size

    def push(self):
        if self.top >= self.max - 1:
            print("Stack Overflow")
        else:
            number = int(input("Enter a number: "))
            self.top += 1
            self.stack[self.top] = number
            print(f"Pushed {number} to stack")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            print(f"Element deleted: {self.stack[self.top]}")
            self.top -= 1
    def display(self):
        if self.top==-1:
            print("Stack Underflow")
        else:
            for i in range(self.top,-1,-1):
                print(self.stack[i])
    def peek(self):
        if self.top == -1:
            print("Stack underflow")
        else:
            print(self.stack[self.top])


s=Stack()
while 1:
    print("Enter a choice \n 1. push \n 2.pop \n 3.peek \n 4.display \n 5.exit")
    ch=int(input("Enter a choice"))
    match ch:
        case 1:
            s.push()
        case 2:
            s.pop()
        case 3:
            s.peek()
        case 4:
            s.display()
        case 5:
            exit(0)
        case _:
            print("invalid choice")