def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    try:
        score = float(input("Enter Score:"))
        x = score
        if 1.0 >= x <= 0.0:
            print("Bad score")
        elif x >= 0.9:
            print("A")
        elif x >= 0.8:
            print("B")
        elif x >= 0.7:
            print("C")
        elif x >= 0.6:
            print("D")
        elif x < 0.6:
            print("F")
    except:
        print("Bad score")
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculateGrade()