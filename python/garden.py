from __future__ import print_function, division
from random import randint

NUM_LEDS = 100
POINTS = 10

def calculate_score():
    random = randint(0, POINTS)
    print("random", random)

    scores = [random]

    total = sum(scores)
    print("total", total)
    potential = len(scores) * POINTS
    print("potential", potential)
    score = float(total / potential)
    print("score", score, int(score * NUM_LEDS))
    return int(score * NUM_LEDS)

def main():
    score = calculate_score()
    print(score)

if __name__ == '__main__':
    main()
