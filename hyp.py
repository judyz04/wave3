# import math Library
import math

side1 = int(input("Input the smallest length: "))
side2 = int(input("Input the 2nd smallest length: "))

hyp = (math.hypot(side1, side2))
final = round(hyp, 2)
print("the hypotenuse is " + str(final) + " units.")