5# Code Largest o3

def largestNumber():
    A = int(input())
    B = int(input())
    C = int(input())

    if A>=B and A>=C:
        print(A, "is largest")
        return

    if B>=A and B>=C:
        print(B, "is largest")
        return

    else:
        print(C, "is largest")
        return
        
largestNumber()