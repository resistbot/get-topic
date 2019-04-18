
#====================
#read the content of the message into a variable
#size/print only needed for dev/debug

with open("messagebody.txt") as f:
    content = f.read()
    #size = len(content)
    #print (content)

#=====================
#loop through the keywords list and search the content for each keyword

with open("keywords.txt")as m:
    meta = m.read().splitlines()

#find the matching words
for var in meta:
    import re
    x = re.findall(var, content)
    
#display the found words with counts    
    #print (x , len(x))

#=====================
#of the found words, which is the most common
#could be expanded later to extract top 3 from list/array as m1, m2, m3
#useful for better matches and topic analysis

import collections
c = collections.Counter(x).most_common(1)
#print ('most common match =', c)

for key, value in c:
    #print(key, value)
    m1 = key
    #print(m1)

#=====================
#get the paired topic

pairset = {}
with open("pairs.txt") as p:
    for line in p:
        (key, val) = line.split(':')
        a = key
        v = val
    #print (v)
        
        if m1 in key:
            #print(v)
            topic = v
            print (topic)

#======================
#do something with the topic
#======================
    
#======================
#close the files
f.close()
m.close()
p.close()
