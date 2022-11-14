import sys
def main():
    
    N = int(input())
    
    i = 1
    multiplier = 10
    
    while i<=10:
        if (N/10) <1:
            print(i)
            return
        if (N/multiplier) >= 1 and (N/multiplier) <10:
            print(i+1)
            return

        multiplier = 10 * multiplier
        i = i + 1

main()