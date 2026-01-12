import random

def pick_ball_expriment():
    balls = ['Blue','Red','Green']

    result = random.choices(balls)

    pro = balls.count('Red')/len(balls)
    print("Probability of picking a Red ball is",pro)

    if result == 'Red':
        return "Red ball was picked. You WIN !!!"
    else:
        return "Better luck next time :)"

res = pick_ball_expriment()
print(res)
