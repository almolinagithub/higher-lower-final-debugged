
import random
import art
import  game_data

still_in_game = True
points = 0

print("Welcome to the higher lower bla bla bla, the rules are the same..go!")

def vip():
    vip = random.choice(game_data.data)
    return vip

def format_string(vip):
    vip_string = str(vip["name"] +","+ vip["description"] +","+ vip["country"])
    return vip_string

def check_answer(answer,followers_a,followers_b):
    if followers_vip_a > followers_vip_b:
        if answer == "a":
#            points += 1
    #        print(points)
            return True
        else:
            print("Sbagliato")
            still_in_game = False
            return False

    elif followers_vip_a < followers_vip_b:
        if answer == "b":
    #        points += 1
            return True
        else:
            print("Sbagliato")
            still_in_game = False
            return False

vip_b = vip()



while still_in_game:

    vip_a = vip_b
    vip_b = vip()

    vip_a_data = format_string(vip_a)
    vip_b_data = format_string(vip_b)

    followers_vip_a = vip_a["follower_count"]
    followers_vip_b = vip_b["follower_count"]


    print(f"Compare VIP A :{vip_a_data} ..........psss: they F are {followers_vip_a}")

    print(art.vs)

    print(f"with VIP B :{vip_b_data} .........psss: they F are {followers_vip_b}")

    answer = input("who has more followers?  (a/b) ")

    if not check_answer(answer,followers_vip_a,followers_vip_b):
        still_in_game = False
    else:
        points += 1
        print(points)

