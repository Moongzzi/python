def gugudan(dan=2):
    for i in range (1,9+1):
        print(dan, "X", i, "=", dan*i)
    print("========================")
    
gugudan(3)
gugudan(2)
gugudan()

def sum(*numbers):
    sum_value = 0
    for number in numbers:
        sum_value += number
    
    return sum_value

print("1 + 3 =", sum(1, 3))
print("1 + 3 + 5 + 7=", sum(1,3,5,7))

def min(*numbers):
    min_value = numbers;
    for number in numbers:
        if min_value > numbers:
            min_value = number

    return min_value

print("min(3, 6, -2) =", min(3, 6, -2)) 