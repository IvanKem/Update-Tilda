# -*- coding: utf-8 -*-
import requests
import config_example
import config
import json
from pprint import pprint
from urllib.request import urlretrieve
import os
from config_example import *
from config import *
import data

if os.path.exists(export_path):
    pass
else:
    os.mkdir(export_path)
if os.path.exists(export_path + '/' + str(data.project_id)):
    pass
else:
    os.mkdir(export_path + '/' + str(data.project_id))

if data.project_id == '' and data.page_id == '':

    response = requests.get('http://brainz2020.page-on.ru/v1/getprojectslist/?publickey=%s&secretkey=%s' % (config.publickey or config_example.publickey,config.secretkey or config_example.secretkey))
    answer = response.json()

    for project in answer['result']:
        project_id = project['id']



        if export == {} :
            if os.path.exists(export_path + '/' + project_id):
                pass
            else:
                os.mkdir(export_path + '/' + project_id)
        responce = requests.get('http://brainz2020.page-on.ru/v1/getpageslist/?publickey=%s&secretkey=%s&projectid=%s' % (config.publickey or config_example.publickey,config.secretkey or config_example.secretkey,project_id  ))

        #print(responce.text)
        answer= responce.json()


        for page in answer['result']:
            print(page['id'])
            #pages_id.append(page['id'])

            css_path = export_path + '/' + project_id+'/'+ page['id']+ '/css'
            js_path = export_path + '/' + project_id + '/' + page['id'] + '/js'
            images_path = export_path + '/' + project_id + '/' + page['id'] + '/images'

            if config_example.export == {}:
                if os.path.exists(export_path + '/' + project_id + '/' + page['id']):
                    pass
                else:
                    os.mkdir(export_path + '/' + project_id+'/'+ page['id'])


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
                projects_id = export.keys()
                print(projects_id)
                for project_id in projects_id:
                    project_id = str(project_id)
                    project_path = export_path + '/' + project_id
                    page_path = export_path + '/' + project_id + '/' + page['id']

                    if os.path.exists(project_path):
                        pass
                    else:
                        os.mkdir(project_path)

                    if os.path.exists(page_path):
                        pass
                    else:
                        os.mkdir(page_path)
                    try:
                        images_path = export_path + '/' + project_id + '/' + page['id']+'/' + export[int(project_id)]['images_path']
                        print(images_path)
                        if os.path.exists(images_path):
                            pass
                        else:
                            os.mkdir(images_path)
                    except FileNotFoundError:
                        images_path =  export[int(project_id)]['images_path']
                        print(images_path)
                        if os.path.exists(images_path):
                            pass
                        else:
                            os.mkdir(images_path)

                    try:
                        css_path = export_path + '/' + project_id + '/' + page['id'] + '/' + export[int(project_id)]['css_path']

                        if os.path.exists(css_path):
                            pass
                        else:
                            os.mkdir(css_path)

                    except FileNotFoundError:
                        ccs_path = export[int(project_id)]['css_path']
                        if os.path.exists(css_path):
                            pass
                        else:
                            os.mkdir(css_path)

                    try:
                        js_path = export_path + '/' + project_id + '/' + page['id'] + '/' + export[int(project_id)]['js_path']

                        if os.path.exists(js_path):
                            pass
                        else:
                            os.mkdir(js_path)
                    except FileNotFoundError:
                        js_path = export[int(project_id)]['js_path']
                        if os.path.exists(js_path):
                            pass
                        else:
                            os.mkdir(js_path)


            responce = requests.get('http://brainz2020.page-on.ru/v1/getpagefullexport/?publickey=%s&secretkey=%s&pageid=%s' % (config.publickey or config_example.publickey,config.secretkey or config_example.secretkey,page['id']))
            # pprint(responce.json()['result']['css'])
            file_list_css = responce.json()['result']['css']
            try:
                for file in file_list_css:
                    urlretrieve(file['from'], (css_path + '/'+ file['to']))
            except :
                pass

            file_name = responce.json()['result']['filename']
            file = open(export_path + '/' + project_id+'/'+ page['id'] + '/'+  file_name, 'w', encoding='utf-8')
            file_html = responce.json()['result']['html']
            if file_html != None:
                file.write(file_html)
            file.close()


            file_list_images = responce.json()['result']['images']
            try:
                for file in file_list_images:
                    urlretrieve(file['from'], (images_path +'/'+ file['to']))
            except:
                pass

            file_list_js = responce.json()['result']['js']
            try:
                for file in file_list_js:
                    urlretrieve(file['from'], (js_path +'/' + file['to']))
            except:
                pass
else:
    css_path = export_path + '/' + str(data.project_id) + '/' + str(data.page_id) + '/css'
    js_path = export_path + '/' +  str(data.project_id) + '/' + str(data.page_id) +'/js'
    images_path = export_path + '/'+ str(data.project_id) + '/' + str(data.page_id) + '/images'

    if os.path.exists(export_path + '/'+ str(data.project_id) + '/' + str(data.page_id)):
        pass
    else:
        os.mkdir(export_path + '/'+ str(data.project_id) + '/' + str(data.page_id))
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
    responce = requests.get('http://brainz2020.page-on.ru/v1/getpagefullexport/?publickey=%s&secretkey=%s&pageid=%s' %
        (config.publickey or config_example.publickey, config.secretkey or config_example.secretkey, data.page_id))
    # pprint(responce.json()['result']['css'])
    file_list_css = responce.json()['result']['css']
    try:
        for file in file_list_css:
            urlretrieve(file['from'], (css_path + '/' + file['to']))
    except:
        pass

    file_name = responce.json()['result']['filename']
    file = open(export_path + '/' + str(data.project_id) + '/' + str(data.page_id) + '/' + file_name, 'w', encoding='utf-8')
    file_html = responce.json()['result']['html']
    if file_html != None:
        file.write(file_html)
    file.close()

    file_list_images = responce.json()['result']['images']
    try:
        for file in file_list_images:
            urlretrieve(file['from'], (images_path + '/' + file['to']))
    except:
        pass

    file_list_js = responce.json()['result']['js']
    try:
        for file in file_list_js:
            urlretrieve(file['from'], (js_path + '/' + file['to']))
    except:
        pass



