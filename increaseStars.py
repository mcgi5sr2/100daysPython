import sys
def main():
    
    N = int(input("Input "))
    i = 1
    
    while i <= N:
        stars = N +1
        while stars > i:
            print("*",end="")
            stars = stars - 1
        print()
        i = i+1
 
main()