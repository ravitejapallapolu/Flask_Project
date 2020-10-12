# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#from flask import Flask, redirect, url_for, request,render_template


# app = Flask(__name__,template_folder='../venv')
#
# @app.route('/hello/<int:user>')
# def index(user):
#    dict = {'phy': 50, 'che': 60, 'maths': 70}
#    return render_template('login.html',name=user,dic=dict)
# from flask import Flask, render_template, url_for
#
# app = Flask(__name__,template_folder='../venv',static_folder='../venv')
#
# @app.route("/")
# def index():
#    return render_template("index.html")
#
# if __name__ == '__main__':
#    app.run(debug = True)

from flask import Flask,render_template,request,url_for,session,redirect,escape
#
app = Flask(__name__,template_folder='../venv')
app.secret_key = 'ravi'
# @app.route('/')
# def student():
#    return render_template('student.html')
#
# @app.route('/result', methods=['POST','GET'])
# def result():
#    if request.method == 'POST':
#       result= request.form
#       return render_template('result.html',result = result)
#
# if __name__ == '__main__':
#    app.run(debug=True)

@app.route('/')
def index():
   if 'username' in session:
      username = session['username']
      return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
   return "You are not logged in <br><a href = '/login'></b>" + "click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return render_template('login.html')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
