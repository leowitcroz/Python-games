print("Hello, welcome!!")
print("-" *12)
play = input("Would you like to play? ")
print("-" *12)
point = 0
if play != "yes":
    quit()

print("OKAY!! LET'S BEGIN :)")
print("-" *12)


print("first question")
answer = int(input("2 + 2 is? "))
if answer == 4:
     print("YOU ROCK!!")
     point = point + 1
else:
    print("OH NO! YOU MISSED :(")
    point = point - 1
print("Your points are {}".format(point))
print("-" *12)



print("second question")
answer = input("What CPU stands for? ")
if answer == "central processing unit":
     print("YOU ROCK!!")
     point = point + 1
else:
    print("OH NO! YOU MISSED :(")
    point = point - 1
print("Your points are {}".format(point))
print("-" *12)


print("third question")
answer = int(input("when was the official end of WW2? "))
if answer == 1945:
     print("YOU ROCK!!")
     point = point + 1
else:
    print("OH NO! YOU MISSED :(")
    point = point - 1
print("Your points are {}".format(point))
print("-" *12)



print("fourth question")
answer = int(input("how many seconds there are in an hour? "))
if answer == 3600:
     print("YOU ROCK!!")
     point = point + 1
else:
    print("OH NO! YOU MISSED :(")
    point = point - 1
print("Your points are {}".format(point))
print("-" *12)




print("fifth question")
answer = input("famous italian food? ")
if answer == "pizza":
     print("YOU ROCK!!")
     point = point + 1
else:
    print("OH NO! YOU MISSED :(")
    point = point - 1
print("Your points are {}".format(point))
print("-" *12)




print("sixth question")
answer = input("what's the second newton law formula? ")
if answer == "f=m.a":
     print("YOU ROCK!!")
     point = point + 1
else:
    print("OH NO! YOU MISSED :(")
    point = point - 1
   
print("-" *12)

print("Your final points are {}".format(point))
