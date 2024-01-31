#Example

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Example
  
for x in "banana":
  print(x)

#Example
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Example
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#Example
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Example
  
for x in range(6):
  print(x)

#Example
  
for x in range(2, 6):
  print(x)

#Example
  
for x in range(2, 30, 3):
  print(x)

#Example
  
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Example
  
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Example
  
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#Example
  
for x in [0, 1, 2]:
  pass

#Exercise 1
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Exercise 2

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":    
    continue
  print(x)

#Exercise 3
  
for x in range(6):
  print(x)

#Exercise 4

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":    
    break
  print(x)