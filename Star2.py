number = int(input("enter number : "))
for i in range(1 , number + 1):
    print(i * "*")
for j in range(1 , number + 1):
    number -= 1
    print(number * "*")