

""" values = [1,2.23,5,7,2,30,15]
print(values[0])
print(values[6]) """

""" day_of_week = input("Are you failing this class ")
if day_of_week == "yes bro":
    print("correct")
else:
    print("incorrect") """

""" def add(words):
    amountofwords = words.split()
    return len(amountofwords)
    

words = input("Enter a sentence: ")
print(f"That sentence has {add(words)} words.") """


""" def number(x):
    if x % 2 == 0:
        return "odd"
    else:
        return "even"
x = int(input("Enter a number"))
print(f"Your number is {number(x)}.") """

""" def service(x):
    if x == "great":
        return "25%"
    elif x == "good":
        return "20%"
    elif x == "okay":
        return "15%"
    elif x == "bad":
        return "0%"
    else:
        return "as much as you want"
x = str(input("How was your service. "))
print(f"I will tip {service(x)}.") """

""" def x(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors
number = int(input("Pick a number. "))
print(f"The number's factors are{x(number)}.") """

def gcf(x, y):
    factors = []
    for i in range(x, y):
        if x % i == 0 and y % i == 0:
            factors.append(i)
        return factors
    gcf = int(input("Pick 2 numbers. "))
    print(f"The two number's greatest common factors are{gcf(x, y)}")