"""
purse=dict()
purse['money']=12;
purse['candy']=3;
purse['tissues']=75;
print(purse)
print(purse['candy'])
purse['money']=purse['candy']+purse['money']
print(purse['money'])


counts=dict()
names=['raj','Ram','Rocky','sam','Ram']
for n in names:
    if n not in counts:
       counts[n]=1
       
    else:
       counts[n]=counts[n]+1
       
print(counts)

counts=dict()
names=['raj','Ram','Rocky','sam','Ram']
for n in names:
    counts[n] =counts.get(n,0)+1
print(counts)


dict={'Sam':1,'Joy':4,'Shawn':7}
for key in dict:


dict={'Sam':1,'Joy':4,'Shawn':7}
print(dict.keys())    
print(dict.values())
print(dict.items())
    print(key,dict[key]
"""
name=open("Purge.txt","rt")
counts=dict()
for line in name:
     words=line.split()
     for word in words:
         counts[word]=count.get(words,0)+1