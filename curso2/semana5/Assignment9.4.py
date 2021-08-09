# Problem Statement : 

# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages. The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail. The
# program creates a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file. After the dictionary is
# produced, the program reads through the dictionary using a maximum loop to
# find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

words = list()
email = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    line = line.split()
    #words.append(line[1])
    email[line[1]] = email.get(line[1],0) + 1


#for w in words:
    #email[w] = email.get(w,0) + 1

largest = -1
theemail = None

for k,v in email.items():
    if v > largest:
        largest = v
        theemail = k
print(theemail,largest)





    