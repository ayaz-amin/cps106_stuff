import math

def find(elm_list, x):
    def find_recursive(elm_list, x):
        if elm_list[0] == x:
            return 0
        return find_recursive(elm_list[1:], x) + 1
    try: return find_recursive(elm_list, x)
    except: return -1

def inner_product(L1, L2):
    if len(L1) != len(L2):
        return None
    product = 0
    for i in range(len(L1)):
        product += L1[i] * L2[i]
    return product
    
def extract_number(sample_str):
    num_list = "0123456789"
    extracted = ""
    for c in sample_str:
        if c in num_list:
            extracted += c
    return extracted
    
def converging_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += 1 / (i**2)
    return sum
    
if __name__ == "__main__":
    elm_list = [1.2, 3, 555, 66, 6, 35, 345, 345, 78, 12341]
    print(find(elm_list, 78))
    print(find(elm_list, 11))

    L1 = [8.17, 4.99, 16.56, 7.31, 0.21, 16.18, 13.75, 11.28, 4.3, 17.79]
    L2 = [17.68, 1.19, 2.64, 13.01, 8.5, 15.04, 0.3, 18.72, 4.58, 9.66]
    print(inner_product(L1, L2))
    
    print(extract_number("1ksdj4sdf>R?387BDYGrrf%44@2"))
    
    n = 0
    eps = 0.001
    while True:
        approx = (math.pi ** 2 / 6) - converging_sum(n)
        if approx < eps:
            print(converging_sum(n))
            break
        n += 1
    print(f"n needs to be {n} to be within distance 0.001 of pi**2 / 6")