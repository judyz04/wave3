# the amount of stuff purchased. 

ans1 = input("Did you buy something?(Yea or No only): ")

if ans1 == str("Yes"):
    n = int(input("How many extra items did you buy: "))
    total = 10.95 + (2.95*n)
    total2 = n + 1 
    print("You bought " + str(total2) + " items.")
    print("Your total shipping fee is $" + str(total) +".")
elif ans1 == str("No"):
    print("Have a good day.")
else:
    print("Answer Yes or No.")