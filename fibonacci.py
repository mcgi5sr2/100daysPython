import sys
def main():
    
    N = int(input("Input Number here"))
    
    # first number is always 0 i=0
    # second number is always 1
    # third number is i-2 + i-1
    # val =  ,
    n1 = 0
    n2 = 1
    i = 0
    s = ""
    
    if N == 1:
        print(n1)
    else:
        while i < N:
            #print(n1, end ="")
            s += str(n1)
            nth = n1 + n2
            
            n1 = n2
            n2 = nth
            i += 1
        print(s)
main()
