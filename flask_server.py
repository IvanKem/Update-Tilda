from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    greeting = "Я вас не знаю :("
    if "name" in request.args:
        greeting = "Привет, {}".format(request.args['name'])

    fruit = "Я не знаю, какой у вас любимый фрукт..."
    if "fruit" in request.args:
        fruit = "Ваш любимый фрукт - {}!".format(request.args['fruit'])

    return """
    <html>
        <body>
            <p>{}</p>
            <p>{}</p>
        </body>
    </html>
    """.format(greeting, fruit)

app.run(debug=True, port=8080)
