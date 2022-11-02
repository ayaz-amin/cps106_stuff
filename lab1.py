class Lab1(object):
    def get_largest_odd_number_q1(self, x, y, z):
        _max = 0
        if (x >= _max) and (x % 2 == 1):
            _max = x
        if (y >= _max) and (y % 2 == 1):
            _max = y
        if (z >= _max) and (z % 2 == 1):
            _max = z
        
        return _max
        
    def get_largest_odd_number_q2(self, n=10):
        print("Enter {} integers".format(n))
        i = 0
        num = -1
        while i < n:
            s_input = int(input("Enter integer {}: ".format(i + 1)))
            if (s_input > num) and (s_input % 2 ==1):
                num = s_input
            i += 1
        return num
        
    def add_money(self, money_list):
        total = 0
        for amount in money_list:
            value = int(amount.split(" ", 1)[0])
            total += value
        return total
        
if __name__ == "__main__":
    lab1_test = Lab1()

    print("")
        
    # Question 1:
    print("Question #1")
    print("===========")
    
    print("Largest odd number: {}".format(lab1_test.get_largest_odd_number_q1(234, 653, 34)))
    print("Largest odd number: {}".format(lab1_test.get_largest_odd_number_q1(56, 776, 787)))
    print("Largest odd number: {}".format(lab1_test.get_largest_odd_number_q1(79, 87465, 764563)))
    
    print("")

    # Question 2:
    print("Question #2")
    print("===========")

    print("Largest odd number: {}".format(lab1_test.get_largest_odd_number_q2()))
    
    print("")
    
    # Question 3:
    print("Question #3")
    print("===========")
    
    print("Total: {} CAD".format( lab1_test.add_money([
        "527 CAD", "392 CAD", "477 CAD", "495 CAD", "569 CAD", "380 CAD",
        "38 CAD", "19 CAD", "473 CAD", "31 CAD", "478 CAD", "538 CAD", 
        "614 CAD", "987 CAD", "632 CAD", "525 CAD", "955 CAD", "322 CAD",
        "357 CAD", "526 CAD"
    ])))