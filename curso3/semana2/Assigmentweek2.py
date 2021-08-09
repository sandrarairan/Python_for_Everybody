import re

hand=open('regex_sum_1312428.txt')
num_list=[]
for line in hand:
    line=line.rstrip()
    numbers=re.findall('[0-9]+',line)
    [num_list.append(int(i))for i in numbers]
print(sum(num_list))