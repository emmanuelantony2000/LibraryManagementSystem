from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/', methods=['POST'])
def homepage_func():
    try:
        if request.form['button'] == 'first':
            return redirect(url_for('inputBooks'))
        elif request.form['button'] == 'second':
            return redirect(url_for('bookIssue'))
    except:
        return render_template('homepage.html')

@app.route('/inputBooks')
def inputBooks():
    return render_template('inputBooks.html')

@app.route('/inputBooks', methods=['POST'])
def inputBooks_post():
    try:
        if request.form['button'] == 'submit':
            book_name = request.form['book_name']
            author_name = request.form['author_name']
            book_code = request.form['book_code']
            l = [book_name, author_name, book_code]
            command = ['python3', 'inputBooks.py', 'separator'.join(l)]
            command = ' '.join(command)
            os.system(command)
            return render_template('inputBooks.html')
        elif request.form['button'] == 'back':
            return redirect(url_for('homepage'))
    except:
        return render_template('inputBooks.html')

@app.route('/bookIssue')
def bookIssue():
    return render_template('bookIssue.html')

@app.route('/bookIssue', methods=['POST'])
def bookIssue_post():
    try:
        if request.form['button'] == 'submit':
            name = request.form['name']
            class_ = request.form['class']
            id_ = request.form['id']
            code = request.form['code']
            l = [name, class_, id_, code]
            command = ['python3', 'bookIssue.py', 'separator'.join(l)]
            command = ' '.join(command)
            os.system(command)
            return render_template('bookIssue.html')
        elif request.form['button'] == 'back':
            return redirect(url_for('homepage'))
    except:
        return render_template('bookIssue.html')

if __name__ == "__main__":
    first = 'python3 first.py'
    os.system(first)
    app.run(debug=True)