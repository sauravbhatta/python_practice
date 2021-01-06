"""
list1=[2,5,7,9,1]
list1[2]=11
print(list1)
print(len(list1))
print(range(len(list1)))


friends=["Raj","Jai","Ram"] 
for f in friends:
    print("Happy Birthday", friends)

friends=["Raj","Jai","Ram"]    
for i in range(len(friends)):
    f=friends[i]
    print("Happy Birthday", f)
    
s=['e','o','a','u','i']
s.sort();
print(s) 
print(s[-2])
   
x=[11,21,4,5,98]
print(len(x))
print(sum(x))
print(sum(x)/len(x))
print(min(x))
print(max(x))   
print(x.append)


num_list=list()
while True:
      inp=input("Enter a number: ")
      x='done'
      if inp==x :break
      value=float(inp)
      num_list.append(value)
      

average=sum(num_list)/len(num_list)
print("Average is: ",average)


#Strings & Lists

x="How are you?"
print(x.split())
print(len(x))
"""