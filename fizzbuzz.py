number = list(range(1,25))
for i in range(len(number)):
    if number[i]%4 ==0 and number[i]%6 == 0:
        print("fizzbuzz")
    elif number[i]%4 == 0:
        print("fizz")



   
    elif number[i]%6 == 0:
        print("buzz")

    else:
        print(number[i])
