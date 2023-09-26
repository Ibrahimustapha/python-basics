import random

def gen_random():
    for i in range(4):
        random_num = random.randint(180757466,200000000)
        print(random_num)

print(gen_random())

random_number_generator = lambda: random.randint(180757466,200000000)

for i in range(4):
    random_number = random_number_generator()
    print(f"Random number: {random_number}")