# Question 1
def int_to_binary(integer_num):
    num_bit_length = integer_num.bit_length()
    num_in_binary = []
    for i in range(num_bit_length):
        remainder = str(integer_num % 2)
        integer_num = int(integer_num / 2)
        num_in_binary.append(remainder)
        
    return int("".join(reversed(num_in_binary)))

# Question 2    
def root_bisection(x):
    eps = 0.01
    low = 0
    high = max(1.0, x)
    ans = (high + low) / 2.0
    num_guesses = 0
    while abs(((ans**5) + (52*ans**3) - 29) - x) >= eps:
        num_guesses += 1
        if (ans**5) + (52*ans**3) - 29 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    print("Answer: {}, Iterations: {}".format(ans, num_guesses))

# Question 3
def root_newton_raphson(x):
    eps = 0.01
    num_guesses = 0
    while abs((x**5) + (52*x**3) - 29) >= eps:
        x = x - ((x**5) + (52*x**3) - 29) / ((5*x**4) + (104*x**2))
        num_guesses += 1
    print("Answer: {}, Iterations: {}".format(x, num_guesses))

if __name__ == "__main__":
    a = 87324838345
    b = 65234242
    c = 576762341243968
        
    print(bin(a)[2:], int_to_binary(a))
    print(bin(b)[2:], int_to_binary(b))
    print(bin(c)[2:], int_to_binary(c))
    
    root_bisection(32)
    root_newton_raphson(32)
        