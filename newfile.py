import random
import time

print("Welcome to Ping Pong!")
print("Type 'hit' quickly when the ball comes to you!\n")

while True:
    time.sleep(random.uniform(1, 3))  # Random ball speed
    print("Ball coming! Type 'hit' NOW!")

    start = time.time()
    user = input().lower()
    reaction = time.time() - start

    if user != "hit":
        print("You missed the ball! Game over.")
        break
    elif reaction > 1.0:
        print("Too slow! Game over.")
        break
    else:
        print("Nice hit! Continue...\n")