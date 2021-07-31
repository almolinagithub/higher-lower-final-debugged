import art
import game_data
import random
#present the art
# present compare A
still_in_game = True
points = 0



def right_answer():
    if int(followers_a) > int(followers_b):
        answer = "a"
    elif int(followers_a) < int(followers_b):
        answer = "b"
    return answer

def check_answer(answer,player_guess):
    return answer ==  player_guess



def get_random_vip():
    vip_random = game_data.data[random.randint(0,50)]
    data_no_followers = str(vip_random['name']+ ', '+ vip_random['description']+', '+ vip_random['country'])
    followers = str(vip_random['follower_count'])
    position = game_data.data.index(vip_random)
    return data_no_followers, followers,position

session_vip_b = get_random_vip()


while still_in_game:
    session_vip_a = session_vip_b
    session_vip_b = get_random_vip()
    if session_vip_a == session_vip_b:
        session_vip_b = get_random_vip()

    public_info_a = session_vip_a[0]
    public_info_b = session_vip_b[0]

    followers_a = session_vip_a[1]
    followers_b = session_vip_b[1]

    print(art.logo)

    print(f"Compare A: {public_info_a}")
    print(f"psssst he/she has {followers_a} followers")
    print(art.vs)
    print(f"Against B: {public_info_b}")
    print(f"psssst he/she has {followers_b} followers")

    player_guess = input("Who has more followers? (a/b) ")

    answer = right_answer()
    if check_answer(answer,player_guess):
        print("Right")
        points += 1
        print(points)
    else:
        print("Wrong")
        still_in_game = False
