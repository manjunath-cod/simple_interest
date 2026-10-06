def simple_interest(p, r, t):
    return (p * r * t) / 100
    

if __name__ == "__main__":

    p =float(input("Enter a principal amount : "))
    r =float(input("Enter a rate of interest : "))
    t =float(input("Enter a time period : "))

print("The simple interest is: {simple_interest(p, r, t)}")