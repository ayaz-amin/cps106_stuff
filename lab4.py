def return_innermost_num(enclosed_num):
    if type(enclosed_num) == int:
        return enclosed_num
    return return_innermost_num(enclosed_num[0])

def reverse_tuple(T):
    if len(T) == 2:
        return T[1], T[0]
    return reverse_tuple(T[1:]) + (T[0],)

def check_substring(sub, bigstring):
    if len(bigstring) < len(sub):
        return False
    if bigstring[:len(sub)] == sub:
        print(bigstring)
        return True
    check_substring(sub, bigstring[1:])

def count_words(phrase):
    num_spaces = 0
    for i in range(len(phrase)-1):
        if phrase[i + 1] == " ":
            num_spaces = num_spaces + 1
    return num_spaces + 1

def n_epsilon(n, epsilon):
    sum = 0
    for i in range(1, n+1):
        sum = sum + (4 * (-1) ** (i + 1) / (2 * i - 1))
        if (sum - 3.141592653589793) < epsilon:
            return i

if __name__ == "__main__":
    print(return_innermost_num([5]))
    print(return_innermost_num([[55]]))
    print(return_innermost_num([[[123]]]))
    print(return_innermost_num([[[[[[[[[[[[18]]]]]]]]]]]]))

    print(reverse_tuple((1, 2, 3, 4, 5)))
    print(reverse_tuple(('red', 'green', 'blue', 'yellow')))
    
    print(check_substring("hi", "high"))
    print(check_substring("yu", "hyundai"))
    print(check_substring("yel", "yellow"))
    print(check_substring("sub", "bigstring"))
    print(check_substring("toe", "no way m8 xd"))
    
    print(count_words('A  white cat and a black cow'))
    print(count_words('a b c de f g h'))
    print(count_words("Orange you glad I didn't say banana"))
    
    print(n_epsilon(200, 1))
    print(n_epsilon(200, 0.5))