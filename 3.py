try:
    x = 1 / 0
except ZeroDivisionError :
    pass

#2

try:
    x = 1 / "hi"
except TypeError :
    pass

#3
file = input("enter a file name you want to read")
try:
    open(file)

except FileNotFoundError:
        pass