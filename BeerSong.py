
def bottlesofbeer():
    for x in range(98, -1, -1):
        print("{} of beer on the wall, {} bottles of beer".format(x+1, x+1))
        if x == 0: x = "no more"
        print("take one down, pass it around, {} bottles of beer on the wall".format(x))
    return
bottlesofbeer()