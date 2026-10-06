import sys
def simpleint(p,t,r):
    return p*t*r/100

if __name__ == "__main__":
    p=int(sys.argv[1])
    t=int(sys.argv[1])
    r=int(sys.argv[1])
    print("Simple interest is :", simpleint(p,t,r))