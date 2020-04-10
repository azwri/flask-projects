from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    # return 'Hi'
    return render_template('home.html')


@app.route('/your-url/', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        code = request.form['code']
        url = request.form['url']
        return render_template('your-url.html', code=code, url=url)
    else:
    # GET 1:
    # code = request.args.get('code')
    # url = request.args.get('url')
    # GET 2:
    # code = request.args['code']
    # url = request.args['url']
        # return render_template('your-url.html', code=code, url=url)
        return 'This is not valid'


# if __name__ == "__main__":
    # app.run(debug=True)


# in termnial:
# export FLASK_APP=app
# flask run

# export FLASK_ENV=development
# flask run
