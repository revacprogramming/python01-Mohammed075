# Functions

def computepay(h,r):
    if h<=40:
        p=h*r
    else:
        p=(40*r)+(h-40)*1.5*r
    return p
def main():    
    h = float(input("Enter Hours:"))
    r = float(input("Enter the Rate:"))
    p = computepay(h,r)
    print("Pay", p)
main()