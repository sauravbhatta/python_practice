"""
Tuples are another kind of sequence that functions similar to a list


x=("Pwan","Bishal","Ankit")
print(x[1])
x[2]="Ram"
print(x)

Cannot change in tuples("Unmutable").Tuples cant be sorted,appended and reversed"""
""" 
t=tuple()
print(dir(t))
MNGNET1477D:Python_special saurav.b01$ python Tuples.py
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
'__getslice__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__',
'__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

The item method in dictionaries returns a list of tuples

t1=(0,1,2)
t2=(3,5,6)
if t1>t2:
   print("True")
   
else:
   print("False")
          """
t1={'a':0,'b':1,'c':2}
tmp=list()
for k,v in t1.items():
    tmp.append((v,k))

       
print(tmp)
t1=[(0,'a'),(1,'b'),(22,'c')]
tmp=sorted(t1,reverse=True)
print(tmp)

   
