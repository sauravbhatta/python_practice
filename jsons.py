#JSON#
'''
import json
data='''{
"name": "Chuck",
"phone":{ 
"type": "intl1",
"number": "9954968714"
    },
"email":{
"hide" : "yes" 
    }
}'''

info=json.loads(data)
print("Name:" ,info["name"])
print("Hide:",info["email"]["hide"])

O/P
MNGNET1477D:python_special saurav.b01$ python jsons.py
('Name:', u'Chuck')
('Hide:', u'yes')'''

