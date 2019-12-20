# Enter the Quantity of strings
n = int(input("Enter the number : "))
s =list()

# Input the strings
for m in range(n):
    s.append(str(input("Enter string  : ")))

# Computation begins
for k in range(n):    
    l = len(s[k])

    # Nested loop is used 
    evenString = "".join([s[k][i] for i in range(0, l, 2) if i < l])
    oddString = "".join([s[k][j] for j in range(1, l, 2) if j < l])

    # Finally Solution
    print(f"{evenString} {oddString}")
