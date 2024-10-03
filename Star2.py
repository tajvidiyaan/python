number = int(input("enter number : "))
for i in range(0 , number + 1):
    print(i * "*")
    for j in range(0 , number - 1):
        print(number * "*")
        number -= 1
        print(number * "*")
