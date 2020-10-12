from flask_wtf import Form
from wtforms import TextField
from flask import Flask, render_template
#from forms import ContactForm

class ContactForm(Form):
   name = TextField("Name Of Student")

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def index():
    return 'HELLo'

@app.route('/contact')
def contact():
   form = ContactForm()
   return render_template('contact.html', form = form)

#if __name__ == '__main__':
   app.run(debug = True)

