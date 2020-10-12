from flask import Flask, redirect, url_for, render_template, request,abort,flash

#from flask.ext import foo
# Initialize the Flask application
app = Flask(__name__)
#app = Flask(__name__,template_folder='../Redirect')
app.secret_key = 'random string'

from flask_mail import Mail, Message
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'raviteja.p2017@gmail.com'
app.config['MAIL_PASSWORD'] = 'ravi.1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'raviteja.p2017@gmail.com', recipients = ['raviteja.p2017@gmail.com'])
   msg.body = "This is the email body"
   mail.send(msg)
   return "Sent"

# @app.route('/')
# def index():
#     return render_template('log_in.html')
#

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST' :
#         if request.form['username'] == 'admin':
#             name = request.form['username']
#             return redirect(url_for('success',name=name))
#         else :
#
#             abort(403)
#
#     else:
#         return redirect(url_for('index'))
#
#
# @app.route('/success/<name>')
# def success(name):
#     return name+' logged in successfully'

# @app.route('/')
# def index():
#     return render_template('upload.html')
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or \
#                 request.form['password'] != 'admin':
#             error = 'Invalid username or password. Please try again!'
#         else:
#             flash('You were successfully logged in')
#             return redirect(url_for('index'))
#
#     return render_template('Login.html', error=error)
#

#if __name__ == '__main__':
    app.run(debug=True)
