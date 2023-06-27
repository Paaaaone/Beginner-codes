weight = int(input("What is your weight? "))
weight_type = input("(K)g or (L)bs ")
if weight_type.upper() == "K":
    weight = weight / 0.45
    print("Weight is " + str(weight) + "Lbs")
elif weight_type.upper() == "L":
    weight = weight * 0.45
    print("Weight is " + str(weight) + "Kg")
else:
    print("Invalid input, try again")
