## There are N rows
## Spaces = N -i
## i'th rows are i Numbers in increasing order starting from i
## i-1 numbers in the decreasing order

N = int(input())
i = 1
while i<=N:
    #spaces
    spaces = 1
    while spaces<=N-i:
        print(" ", end="")
        spaces = spaces +1
    #increasing numbers
    val = i
    count =1
    while count <= i:
        print(val,end="")
        val = val + 1
        count = count + 1
    # decreasing numbers
    # reset the val
    val = val -2
    count = 1
    while count<=i-1:
        print(val,end="")
        val = val - 1
        count = count + 1
    
    print()
    i = i+1