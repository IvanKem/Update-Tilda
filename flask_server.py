from flask import Flask, request,request, redirect

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        page = "None"
        if "pageid" in request.args:
            page = request.args.get('pageid','')


        project = 'None'
        if "projectid" in request.args:
            project = request.args.get('projectid','')

        file = open('data.py', 'w', encoding='utf-8')
        page_id = 'page_id =' + page
        project_id = 'project_id='+project
        if page != None:
            file.write(page_id)
            file.write('\n'+project_id)
        file.close()



        return """
            <html>
                <body>
                    <p>{}</p>
                    <p>{}</p>
                </body>
            </html>
            """.format(page, project)



    elif request.method == 'POST':
        pageid = request.values.get('pageid')  # Your form's
        return pageid



app.run(debug=True, port=8080)
