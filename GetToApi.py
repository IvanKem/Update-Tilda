# -*- coding: utf-8 -*-
import requests
import config
import json
from pprint import pprint

response = requests.get('http://api.tildacdn.info/v1/getprojectslist/?publickey=%s&secretkey=%s' % (config.publickey,config.secretkey))
answer = response.json()
project_id =[]
for project in answer['result']:
    project_id.append(project['id'])
print(project_id)

for project in project_id:
    responce = requests.get('http://api.tildacdn.info/v1/getpageslist/?publickey=%s&secretkey=%s&projectid=%s' % (config.publickey,config.secretkey,project))

    #print(responce.text)
    answer= responce.json()
    pages_id = []

    for page in answer['result']:
        #print(page['id'])
        pages_id.append(page['id'])
        responce = requests.get('http://api.tildacdn.info/v1/getpagefullexport/?publickey=%s&secretkey=%s&pageid=%s' % (config.publickey,config.secretkey,page['id']))
        pprint(responce.json()['result'])
        file_name = responce.json()['result']['filename']
        file = open (file_name , 'w', encoding='utf-8')
        file_html = responce.json()['result']['html']
        if file_html != None:
            file.write(file_html)
        file.close()

    #print(answer['result'])