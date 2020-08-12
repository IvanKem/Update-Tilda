# -*- coding: utf-8 -*-
import requests
import config_example
import config
import json
from pprint import pprint
from urllib.request import urlretrieve
import os



response = requests.get('http://api.tildacdn.info/v1/getprojectslist/?publickey=%s&secretkey=%s' % (config.publickey or config_example.publickey,config.secretkey or config_example.secretkey))
answer = response.json()

for project in answer['result']:
    project_id = project['id']



    if os.path.exists(config_example.export_path):
        pass
    else:
        os.mkdir(config_example.export_path)
    if os.path.exists(config_example.export_path + '/' + project_id):
        pass
    else:
        os.mkdir(config_example.export_path + '/' + project_id)
    responce = requests.get('http://api.tildacdn.info/v1/getpageslist/?publickey=%s&secretkey=%s&projectid=%s' % (config.publickey or config_example.publickey,config.secretkey or config_example.secretkey,project_id  ))

    #print(responce.text)
    answer= responce.json()
    pages_id = []

    for page in answer['result']:
        print(page['id'])
        #pages_id.append(page['id'])

        css_path = config_example.export_path + '/' + project_id+'/'+ page['id']+ '/css'
        js_path = config_example.export_path + '/' + project_id + '/' + page['id'] + '/js'
        images_path = config_example.export_path + '/' + project_id + '/' + page['id'] + '/images'

        if config_example.export == {}:
            if os.path.exists(config_example.export_path + '/' + project_id + '/' + page['id']):
                pass
            else:
                os.mkdir(config_example.export_path + '/' + project_id+'/'+ page['id'])


            if os.path.exists(css_path):
                pass
            else:
                os.mkdir(css_path)


            if os.path.exists(images_path):
                pass
            else:
                os.mkdir(images_path)


            if os.path.exists(js_path):
                pass
            else:
                os.mkdir(js_path)

        else:
            page_ID = config_example.page_ID
            page_path = config_example.export_path + '/' + project_id + '/' + page['id']
            if os.path.exists(page_path):
                pass
            else:
                os.mkdir(page_path)
            try:
                images_path = config_example.export_path + '/' + project_id + '/' + page['id']+'/' + config_example.export[page_ID]['images_path']
                print(images_path)
                if os.path.exists(images_path):
                    pass
                else:
                    os.mkdir(images_path)
            except FileNotFoundError:
                images_path = config_example.export[page_ID]['images_path']
                print(images_path)
                if os.path.exists(images_path):
                    pass
                else:
                    os.mkdir(images_path)

            try:
                css_path = config_example.export_path + '/' + project_id + '/' + page['id'] + '/' + config_example.export[page_ID]['css_path']

                if os.path.exists(css_path):
                    pass
                else:
                    os.mkdir(css_path)

            except FileNotFoundError:
                ccs_path = config_example.export[page_ID]['css_path']
                if os.path.exists(css_path):
                    pass
                else:
                    os.mkdir(css_path)

            try:
                js_path = config_example.export_path + '/' + project_id + '/' + page['id'] + '/' + config_example.export[page_ID]['js_path']

                if os.path.exists(js_path):
                    pass
                else:
                    os.mkdir(js_path)
            except FileNotFoundError:
                images_path = config_example.export[page_ID]['js_path']
                if os.path.exists(js_path):
                    pass
                else:
                    os.mkdir(js_path)


        responce = requests.get('http://api.tildacdn.info/v1/getpagefullexport/?publickey=%s&secretkey=%s&pageid=%s' % (config.publickey or config_example.publickey,config.secretkey or config_example.secretkey,page['id']))
        # pprint(responce.json()['result']['css'])
        file_list_css = responce.json()['result']['css']
        for file in file_list_css:
            urlretrieve(file['from'], (css_path + '/'+ file['to']))

        file_name = responce.json()['result']['filename']
        file = open(config_example.export_path + '/' + project_id+'/'+ page['id'] + '/'+  file_name, 'w', encoding='utf-8')
        file_html = responce.json()['result']['html']
        if file_html != None:
            file.write(file_html)
        file.close()

        file_list_images = responce.json()['result']['images']
        for file in file_list_images:
            urlretrieve(file['from'], (images_path +'/'+ file['to']))

        file_list_js = responce.json()['result']['js']
        for file in file_list_js:
            urlretrieve(file['from'], (js_path +'/' + file['to']))



