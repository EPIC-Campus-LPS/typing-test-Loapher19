import time
import random

def randword(len=random.randint(3,10)):
    alphabet = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    word = ""
    for i in range(len):
        word += random.choice(alphabet)
    return word

times = []
num = int(input("how many \"sentences\" "))

for i in range(num):
    sentence = []
    for i in range(3):
        sentence.append(randword(7))
    for i in sentence:
        print(i, end=" ")
    pretime = time.time()
    inp = input()
    postime = time.time()
    times.append(postime - pretime)

avtime = 0
for i in times:
    avtime += i
avtime /= num
wpm = 180 / avtime
print(f"you got {wpm:.4}wpm")
