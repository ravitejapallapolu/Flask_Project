from flask import Flask, redirect, url_for, render_template, request

# Initialize the Flask application
app = Flask(__name__,template_folder='../Redirect')


@app.route('/')
def index():
    return render_template('log_in.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and request.form['username'] == 'admin':
        name = request.form['username']
        return redirect(url_for('success',name=name))
    else:
        return redirect(url_for('index'))


@app.route('/success/<name>')
def success(name):
    return name+' logged in successfully'


if __name__ == '__main__':
    app.run(debug=True)
