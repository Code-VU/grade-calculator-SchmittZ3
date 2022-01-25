try:
    score = float(input("Enter Score:"))
    x = score
    if 1.0 < x or x < 0.0:
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