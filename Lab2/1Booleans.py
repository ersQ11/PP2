#Example

print(10 > 9)
print(10 == 9)
print(10 < 9)

#Example

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Example

print(bool("Hello"))
print(bool(15))

#Example

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Example

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#Example

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#Example

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Example

def myFunction() :
  return True

print(myFunction())

#Example

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Example

x = 200
print(isinstance(x, int))

#Exercise 1

print(10 > 9)

#True


#Exercise 2

print(10 == 9)

#False


#Exercise 3

print(10 < 9)

#False


#Exercise 4

print(bool("abc"))

#True


#Exercise 5

print(bool(0))

#False