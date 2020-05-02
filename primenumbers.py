#get n

n = int(input("Enter an integer (2 or greater): "))

factor = 2

if n < 2:
    print("It has to be greater than two.")

else: 
    print("The prime factors of " + str(n) +" are:")
while n >= factor:
    if n % factor == 0:  
        print(factor)
        n = n/factor
    else: 
        factor += 1