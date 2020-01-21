from random import seed
from random import radiant
seed(1)
for i in range(10):
	value = radiant(0, 10)
	print(value)
print("What is your first name?")
n = input("What is your first name?: ")
print(n)
print("What is your last name?")
v = input("What is your last name?: ")
print(v)
print("Hi there, "+str(n)+" "+str(v)+", nice to meet you!")

print("\nHow old are you?")
b = int(input("How old are you?: "))
if(b >= 16):
    print(""+str(b)+"\n"+str(b)+" is a good age.\nYou are old enough to drive.")
if(b <= 15):
    print(""+str(b)+"\n"+str(b)+" is a good age.\nYou are not old enough to drive.")

print("\nSo, "+str(n)+", are you happy or sad today?")
a = input("So, "+str(n)+", are you happy or sad today?")
if(a == "Happy"):
    print(""+str(a)+"\nYou are "+str(a)+".\nThat is good to hear.")
elif(a == "happy"):
    print(""+str(a)+"\nYou are "+str(a)+".\nThat's great!")
if(a == "Sad"):
    print(""+str(a)+"\nYou are "+str(a)+".\nI'm sorry to hear that.")
elif(a == "sad"):
    print(""+str(a)+"\nYou are "+str(a)+".\nI'm sorry to hear that.")

if(a == "sad"):
    print("Tell me whats wrong.")
    c = input("Tell me whats wrong: ")
    print("/n"+str(c)+"\nI hope things get better.")
if(a == "Sad"):
    print("Tell me whats wrong.")
    c = input("Tell me whats wrong: ")
    print("\n"+str(c)+"\nI hope things get better.")
if(a == "Happy"):
    print("Tell me more.")
    d = input("Tell me more: ")
    print("\n"+str(d)+"\n Sounds like you're having a good day!")
if(a == "happy"):
    print("Tell me more.")
    d = input("Tell me more: ")
    print("\n"+str(d)+"\n Sounds like you're having a good day!")
print("\nWell, "+str(n)+", it has been nice chatting with you.")
