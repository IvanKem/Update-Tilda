from flask import Flask, request,request, redirect

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # You probably don't have args at this route with GET
        # method, but if you do, you can access them like so:
        pageid = request.args.get('pageid','')
        file = open('data.py', 'w', encoding='utf-8')
        if pageid != None:
            file.write(pageid)
        file.close()
        return pageid



    elif request.method == 'POST':
        pageid = request.values.get('pageid')  # Your form's
        return pageid


app.run(debug=True, port=8080)
