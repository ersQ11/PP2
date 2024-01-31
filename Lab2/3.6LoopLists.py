#Example

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Example

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Example

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Example

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]