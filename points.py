import random
import time


def home_win(a, b):
    points = a + b
    return points

def away_win(c, d):
    points = c + d
    return points


def home_draw(e, f):
    points = e + f
    return points

def away_draw(g, h):
    points = g + h
    return points

def first_game():
    score = [0, 1, 0, 0, 2, 0, 1, 0, 1]
    home_team = ("Juventus")
    away_team = ("Napoly")
    home_goals = random.choice(score)
    away_goals = random.choice(score)
    print (home_team, ":", away_team)
    print (  home_goals, ":", away_goals)
    time.sleep(5)
    newhome_goals = random.choice(score)
    newaway_goals = random.choice(score)
    tatolhome_goals = home_goals + newhome_goals
    tatolaway_goals = away_goals + newaway_goals
    print (  tatolhome_goals, ":", tatolaway_goals) 
    if tatolhome_goals > tatolaway_goals:
        print (home_team, "won")
        x = home_win(3, 0)
        print ("home points:", x)
    elif tatolhome_goals < tatolaway_goals:
        print (away_team, "won")
        y = away_win(3, 0)
        print ("away points:", y)
    elif tatolhome_goals == tatolaway_goals:
        print ("Draw")
        z = home_draw(1, 0)
        o = away_draw(1, 0)
        print ("Home points:", z, "Away Points:", o)

def points(hom_win, away_win, home_draw, away_draw):
     if tatolhome_goals > tatolaway_goals:
         hpoints = 3
         
         Points = hpoints
     elif tatolhome_goals < tatolaway_goals:
         apoints = 3
         Points = apoints
     elif tatolhome_goals == tatolaway_goals:
         dhpoints = 1
         dapoints = 1
         Points = dhpoints
         Points = dapoints
       



first_game()
