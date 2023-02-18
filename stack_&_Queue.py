# stack
book = []
book.append("Learn c")
book.append("Learn c++")
book.append("Learn java")
book.append("Learn python")
print(book)
book.pop()
print(book)
print("Now the top book is :", book[-1])
book.pop()
print("Now the top book is :", book[-1])
book.pop()
print("Now the top book is :", book[-1])
book.pop()
if not book:
    print("Not enough book")

# Queue
from collections import deque

bank = deque(["yemon", "mominul", "anower"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()

if not bank:
    print("No person left")
