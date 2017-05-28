def pythagorean(): # make a function
    leg1 = int(input("Enter the value of one leg: ")) # get user input for leg1
    leg2 = int(input("Enter the value of another leg: ")) # get user input for leg2

    square1 = leg1**2 # Square of leg 1
    square2 = leg2**2 # Square of leg 2

    sq_sum = square1 + square2 # Addition of squre 1 and 2

    result = sq_sum ** (0.5) # the result

    print("The hypotenuse is: " + str(result)) # print out the result
    # converted int to string using str()
    # This was done so that there will be no parentheses ^^
    # I DID receive some help from Andrew... so don't judge me 

pythagorean() # call the function
