from random import randint



rules = 'Find the greatest common divisor of given numbers.'
#Алгорит Евклида, выглядит сложно, но прикольно! 
def gcd(num1, num2):
    max_val = max(num1, num2)
    min_val = min(num1, num2)

    while min_val:
        max_val, min_val = min_val, max_val % min_val
    return max_val

def gplay_game():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    num = f"{num1} {num2}"
    correct_answer = gcd(num1, num2)
    return correct_answer, num