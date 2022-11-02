def spacedout(str_, numSpaces):
    out_str_ = ""
    for s in str_:
        out_str_ += (s + " " * numSpaces)
    return out_str_

def reverse_(str1):
    str_list = []
    for s in str1:
        str_list.append(s)
    return "".join(reversed(str_list))

def isPalindrome(str1):
    if len(str1) == 1:
        return [str1]
    
    permutations = []
    for s in isPalindrome(str1[:-1]):
        for i in range(len(s) + 1):
            permutations.append(s[:i] + str1[-1] + s[i:])
    return permutations
    
def findHighestOccur(n):
    n_str = str(n)
    n_dict = {}
    max_val = 0
    highesest_occur = -1
    for num in n_str:
        if num in n_dict:
            n_dict[num] += 1
            if n_dict[num] > max_val:
                highest_occur = num
        else:
            n_dict[num] = 0
    return int(highest_occur)

if __name__ == "__main__":
    x = "It was a dark and stormy night"
    y = 1
    print(spacedout(x, 1))
    
    print(reverse_("I am here"))
    
    print(findHighestOccur(983254682376587235235))
    print(findHighestOccur(767347657623764765766665))
    print(findHighestOccur(923740923466234678666872628347666))
    
    print(isPalindrome("abcd"))