import sys
def main():
    
    N = int(input())
    
    if (N/10) <1:
        print(1)
        return
    
    if (N/10) >= 1 and (N/10) <10:
        print(2)
        return
    
    if (N/100) >= 1 and (N/100) <10:
        print(3)
        return
    
    if (N/1000) >= 1 and (N/1000) <10:
        print(4)
        return
    
    if (N/10000) >= 1 and (N/10000) <10:
        print(5)
        return
    
main()