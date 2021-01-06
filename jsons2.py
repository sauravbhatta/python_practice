'''
import json
input='''[
{"id" :"001",
"x":"2",
"name":"Chuck"
},
{"id" :"009",
"x":"5",
"name":"Chuck"
}
]'''

info=json.loads(input)
print("User Count :",len(info) )
for i in info:
    print('Name:',i['name'])
    print('Id:',i['id'])
    print('Attribute',i['x'])
O/P
MNGNET1477D:python_special saurav.b01$ python jsons2.py
('User Count :', 2)
('Name:', u'Chuck')
('Id:', u'001')
('Attribute', u'2')
('Name:', u'Chuck')
('Id:', u'009')
('Attribute', u'5')'''