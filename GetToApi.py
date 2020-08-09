# -*- coding: utf-8 -*-
import requests
import config_example #your config file with all keys and with export
import config
import json
from pprint import pprint
from urllib.request import urlretrieve
import os

#get all projects id
response = requests.get('http://api.tildacdn.info/v1/getprojectslist/?publickey=%s&secretkey=%s' % (config.publickey, config.secretkey))
answer = response.json()

for project in answer['result']:
    project_id = project['id'] + '-p'
    #create Export folder and folders with project id
    if os.path.exists(config.export_path):
        pass
    else:
        os.mkdir(config.export_path)
    if os.path.exists(config.export_path + '/' + project_id):
        pass
    else:
        os.mkdir(config.export_path + '/' + project_id)
    #get all pages id
    responce = requests.get('http://api.tildacdn.info/v1/getpageslist/?publickey=%s&secretkey=%s&projectid=%s' % (config.publickey, config.secretkey, project_id))

    # print(responce.text)
    answer = responce.json()
    pages_id = []

    for page in answer['result']:
        #print(page['id'])
        pages_id.append(page['id'])
        page_id = page['id']+'-s'
        #create folders with page id and with js,css,html and images files
        if os.path.exists(config.export_path + '/' + project_id + '/' + page_id):
            pass
        else:
            os.mkdir(config.export_path + '/' + project_id + '/' + page_id)

        if os.path.exists(config.export_path + '/' + project_id + '/' + page_id + '/css'):
            pass
        else:
            os.mkdir(config.export_path + '/' + project_id + '/' + page_id + '/css')

        if os.path.exists(config.export_path + '/' + project_id + '/' + page_id + '/html'):
            pass
        else:
            os.mkdir(config.export_path + '/' + project_id + '/' + page_id + '/html')

        if os.path.exists(config.export_path + '/' + project_id + '/' + page_id + '/images'):
            pass
        else:
            os.mkdir(config.export_path + '/' + project_id + '/' + page_id + '/images')

        if os.path.exists(config.export_path + '/' + project_id + '/' + page_id + '/js'):
            pass
        else:
            os.mkdir(config.export_path + '/' + project_id + '/' + page_id + '/js')
        # get full export of page
        responce = requests.get('http://api.tildacdn.info/v1/getpagefullexport/?publickey=%s&secretkey=%s&pageid=%s' % (config.publickey, config.secretkey, page['id']))
        # pprint(responce.json()['result']['css'])

        #all css files
        file_list_css = responce.json()['result']['css']
        for file in file_list_css:
            urlretrieve(file['from'], (config.export_path + '/' + project_id + '/' + page_id + '/css/' + file['to']))
        # all html files
        file_name = responce.json()['result']['filename']
        file = open(config.export_path + '/' + project_id + '/' + page_id + '/html/' + file_name, 'w', encoding='utf-8')
        file_html = responce.json()['result']['html']
        if file_html != None:
            file.write(file_html)
        file.close()
        # all images files
        file_list_images = responce.json()['result']['images']
        for file in file_list_images:
            urlretrieve(file['from'], (config.export_path + '/' + project_id + '/' + page_id + '/' + 'images/' + file['to']))
        # all js files
        file_list_js = responce.json()['result']['js']
        for file in file_list_js:
            urlretrieve(file['from'], (config.export_path + '/' + project_id + '/' + page_id + '/' + 'js/' + file['to']))

