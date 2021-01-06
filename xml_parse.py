"""import xml.etree.ElementTree as ET
data='''<person>
<name>KSB</name>
<phone type="intl">9954968643</phone>
<email hide="yes"/>
</person>'''
tree=ET.fromstring(data)
print('NAME: ',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))

'''
python_special saurav.b01$ python xml_parse.py
('NAME: ', 'KSB')
('Attr:', 'yes')
'''



import xml.etree.ElementTree as ET
input='''<stuff>
    <users>
    <user x="2">
         <id>001</id>
         <name>Chuck</name>
         </user>
         <user x="7">
               <id>009</id>
               <name>KSB</name>
         </user>
     </users>
    </stuff>'''
    
stuff=ET.fromstring(input)
lst=stuff.findall('users/user')
print('User Count: ',len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id',item.find('id').text)
    print('Attribute',item.get("x"))
    
    Output 
    MNGNET1477D:Python_special saurav.b01$ python xml_parse.py
('User Count: ', 2)
('Name', 'Chuck')
('Id', '001')
('Attribute', '2')
('Name', 'KSB')
('Id', '009')
('Attribute', '7')

"""