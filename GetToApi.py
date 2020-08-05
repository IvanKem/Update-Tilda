# -*- coding: utf-8 -*-
import requests
import config
import json

from pprint import pprint


responce = requests.get('http://api.tildacdn.info/v1/getpageslist/?publickey=%s&secretkey=%s&projectid=%s' % (config.publickey,config.secretkey,config.projectid2))

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
    file.write(responce.json()['result']['html'])
    file.close()

#print(answer['result'])
