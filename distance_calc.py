'''
Eugene Lee
The program can be ran with python3 using the command `python3 distance_calc.py` in your terminal. After running the script, your terminal will prompt you to input 2 values and then output the distance and the alignment in the terminal.
'''
import numpy as np
import math

print("Enter the first word: ")
input1 = input()
input1 = input1.lower()
print("Enter the second word: ")
input2 = input()
input2 = input2.lower()
len1 = len(input1) + 1 
len2 = len(input2) + 1
alignment = np.zeros ((len1,len2))
list1 = []
list2 = []

for i in range(len1):
    alignment[i,0] = i
for i in range(len2):
    alignment[0,i] = i

for i in range(1,len1):
    for j in range(1,len2):
        if(input1[i-1] == input2[j-1]):
            alignment[i,j] = min(alignment[i-1,j] + 1, alignment[i-1,j-1], alignment[i,j-1] +1)
        else:
            alignment[i, j] = min(alignment[i-1, j] + 1, alignment[i-1, j-1] + 1, alignment[i, j-1] + 1)

i = len1 - 1
j = len2 - 1
while (i != 0 and j != 0):
    if (alignment[i][j] == (alignment[i-1][j-1] if input1[i-1] == input2[j-1] else alignment[i-1][j-1] + 1)):
        i -= 1
        j -= 1
        list1.append(input1[i])
        list2.append(input2[j])
        if(i == 0 and j != 0):
            j-=1
            list1.append('_')
            list2.append(input2[j])
        elif(i!= 0 and j == 0):
            i-=1
            list1.append(input1[i])
            list2.append('_')
    elif(alignment[i][j] == 1 + alignment[i-1][j]):
        i -= 1
        list1.append(input1[i])
        list2.append('_')
    elif(alignment[i][j] == 1 + alignment[i][j-1]):
        j -= 1
        list1.append('_')
        list2.append(input2[j])

list1.reverse()
list2.reverse()
list1 = "".join(str(x) for x in list1)
list2 = "".join(str(x) for x in list2)
print("\n",alignment,"\n")
print("The edit distance is:", math.floor(alignment[len1-1,len2-1]))
print("\nAlignment:\n",list1,"\n",list2,"\n\n")
