import random

highest = 1000
answer = random.randint(1,highest)
print(answer)
guess = 0
print("please guess number between 1 and {}".format(highest))

while guess != answer:
    guess = int(input())

    if guess == answer:
        print("well done")
        break
    else:
        if guess < answer:
            print("please guess higher")
        else:
            print("please guess lower")
