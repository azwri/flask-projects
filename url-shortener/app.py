from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = '^%$RFDASGER$E @!$!#$@4##%(^&w45qBDVGERue~~~0978e6DFsdfDSAF'


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        code = request.form['code']
        # url = request.form['url']
        urls = {}
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)

        if request.form['code'] in urls.keys():
            flash('Is already exsited, select another')
            return redirect(url_for('index'))

        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url': request.form['url']}
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save(os.path.abspath('./media/') + '/' +full_name)
            urls[request.form['code']] = {'file': full_name}

        with open('urls.json', 'w') as urls_file:
            json.dump(urls, urls_file)
        return render_template('your-url.html', code=code)
    else:
        # GET 1:
        # code = request.args.get('code')
        # url = request.args.get('url')
        # GET 2:
        # code = request.args['code']
        # url = request.args['url']
        # return render_template('your-url.html', code=code, url=url)
        return redirect(url_for('index'))


# if __name__ == "__main__":
#     app.run(debug=True)


# in termnial:
# export FLASK_APP=app
# flask run

# export FLASK_ENV=development
# flask run
