#%% (1) print the first row

file_path=r'C:\Dropbox\Projects\ds with python\Week 1 - Introduction to Python\code\novel.txt'

f=open(file_path)
s=f.readline()
print(s)
f.close()

#%% (2) print first 10 rows (using for loop)

f=open(file_path)

for i in range(10):
    s=f.readline()
    print(s)

f.close()

#%% (2) print first 10 rows (using while loop)

f=open(file_path)

i=0
while (i<10):
    s=f.readline()
    print(s)
    i=i+1
f.close()


#%% (3) print the total number of rows

f=open(file_path)

s=f.readline()
i=0
while (s):
    i=i+1
    s=f.readline()
print(i)
f.close()

#%% (3) print the total number of rows (read all lines at once)

f=open(file_path)
x=f.readlines()
print(len(x)) # not memory-efficient
f.close()


#%% (4) print the number of non-empty rows 

f=open(file_path)

i=0
for s in f:
    if len(s)>1:
        i=i+1
print(i)
f.close()

#%% (5) print the number of rows containing the word christmas

f=open(file_path)

i=0
for s in f:
    if "Christmas" in s:
        i=i+1
print(i)
f.close()

#%% (6) create list of words, and print the first 20 words

f=open(file_path)

words=[]
for s in f:
    words = words + s.split()

print(len(words))
print(words[:20])
f.close()

#%% (7) List of words containing alpha-numeric charachters

# regular expressions
import re

# extract numeric substrings 
re.findall("[\d]+","123 83 1h 32 ")

# extract aplha-numeric substrings
re.findall("[\w]+", " hello,  world!  88 ")

# match patterns
print(re.match("[\w]+@simon\.rochester\.edu","john@mit.edu"))

print(re.match("[\w]+@simon\.rochester\.edu","john@simon.rochester.edu"))


# 
f=open(file_path)

words=[]
for s in f:
    words=words + re.findall("[0-9a-zA-Z]+", s)

print(len(words))
print(words[:20])
f.close()

#%% (8) computing the frequency of each word
words[:20]
words_lower=list(map(lambda x:x.lower(),words))
words_lower[:20]

freq=dict()
for w in words_lower:
    if w in freq:
        freq[w]+=1
    else:
        freq[w]=1
print(freq)

#%% (9) 20 most used words
freq_list=[(freq[d],d) for d in freq.keys()] # alternatively, use freq.items()
freq_list[:10]

freq_list.sort(key=lambda x:x[0],reverse=True)

freq_list[:20]

#%% (10) export frequencies to file
output_file_path=r'C:\Dropbox\Projects\ds with python\Week 1 - Introduction to Python\code\output.csv'
output=open(output_file_path,'w')
for freq,word in freq_list:
    output.write("%d,%s\n"%(freq,word))
output.close()
