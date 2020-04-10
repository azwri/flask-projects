# -*- coding:utf8 -*-

from flask import Flask, request, url_for


app = Flask(__name__)


@app.route('/')
def home():
    page = 'Home Page'
    return f"""
    <h1>{page}</h1>
    <form method="GET" action="first_last">
        <label>First Name:</label>
        <input type='text' name='first_name' />
        <label>Last Name:</label>
        <input type='text' name='last_name' />
        <input type='submit' value='Submit' />
    </form>
    """.format(page)


@app.route("/hello/", methods=['GET', 'POST'])
def hello():
    return u"""
    <h1>Hello World</h1>
    <h1 style='direction: rtl; color: blue; text-align: center;'>مرحبا بالعالم</h1>
    """


@app.route('/say_hello/<name>/', methods=['GET', 'POST'])
def say_hello(name):
    name = name
    return f"""
    <h1>Hello {name}</h1>
    """


@app.route('/first_last/', methods=['GET', 'POST'])
def first_last():
    first = request.args.get('first_name').capitalize()
    last = request.args.get('last_name').upper()
    test = ''
    if first.startswith('A'):
        test = 'Hola'
    return f"""
    <h1>First Name: {test} {first}</h1>
    <h1>Last Name: {last}</h1>
    """, print(request)


if __name__ == "__main__":
    app.run(debug=True)
