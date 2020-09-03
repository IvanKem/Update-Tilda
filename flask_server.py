from flask import Flask, request,request, redirect
import sqlite3

app = Flask(__name__)


id = 0

@app.route('/webhook', methods=['GET'])
def webhook():
    if request.method == 'GET':
        page = "None"
        if "pageid" in request.args:
            page = request.args.get('pageid','')


        project = 'None'
        if "projectid" in request.args:
            project = request.args.get('projectid','')

        if page and project:
            global id
            with sqlite3.connect('db.sqlite') as conn:
                id+=1
                cursor = conn.cursor()
                cursor.execute("INSERT INTO webhook_projects (id, project, page) VALUES (?,?,?)", (id ,project, page))
                # сохранить изменения
                conn.commit()


        return {'success': 'true'}






app.run(debug=True, port=8080)
