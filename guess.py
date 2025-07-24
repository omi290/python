import random
secret_value = random.randint(1,100)
def guess_the_no():
    while True:
        a= int(input("Guess the no"))
        if a < secret_value:
            print("your no is less")
        elif a > secret_value:
            print("your no is higher")
        else:
            print(f"You gussed it right! {a} is the no.")
            break

guess_the_no()