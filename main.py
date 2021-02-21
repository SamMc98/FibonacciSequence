numberA = 0
numberB = 1
seqPos = [numberA, numberB]

print("Fibonacci Sequence Program\n")
print("Which number do you wish the sequence to not exceed?")
try:
  userNum = input()
  print("\nHere is the sequence, not exceeding",int(userNum),":")
  while numberA < int(userNum) and numberB < int(userNum):
        
        numberA = numberA + numberB
        if (numberA < int(userNum)):
          print(numberA)
          seqPos.append(numberA)
        
        numberB = numberA + numberB
        if (numberB < int(userNum)):
          print(numberB)
          seqPos.append(numberB)
except ValueError:
   print("That's not a number!")

print("\nWhich position of the sequence would you like to return a value from? You can choose a number up to:", len(seqPos))
try:
  userPos = input()
  if (int(userPos) <= len(seqPos)):
    print("\nThe number at position", int(userPos), "is:", seqPos[int(userPos)-1])
  else:
    print("Out of range!")
except ValueError:
   print("That's not a number!")