# Bubble Sorting :: O(n)

## it is input independent algorithm
''' if elemets are to tbe sorted, sorting are done in pairs. 
In ASC sort
if a > b --> a is swapped with b, and the loop continues.
Also vice-versa.
'''

s = [2,7,6,9,1,8]

#Asc Sort
for i in range(len(s)-1):
    for j in range(len(s)-i - 1):
        if s[j] > s[j+1]:
            s[j] , s[j+1] = s[j+1], s[j]
            print("[+]" , s[j] , s[j+1])

print("\n", s)
