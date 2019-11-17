import pyrebase
from flask import *
app = Flask(__name__)
config = {
    "apiKey": "AIzaSyCQMH5ByN78Uhd7JNCpPwbGkDh_fFCmbRs",
    "authDomain": "dummy-b7637.firebaseapp.com",
    "databaseURL": "https://dummy-b7637.firebaseio.com",
    "projectId": "dummy-b7637",
    "storageBucket": "dummy-b7637.appspot.com",
    "messagingSenderId": "374974448752",
    "appId": "1:374974448752:web:ba7428ad8c78af12b0e0b5",
    "measurementId": "G-9625M7LTPZ"
}

firebase = pyrebase.initialize_app(config)
db=firebase.database()
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])

def basic():
    unsuccessful = 'Please check your credentials'
    successful = 'Login successful'
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            if request.method=='POST':
                        x='go'
                        return redirect(('go'))
        except:
            return render_template('new.html', us=unsuccessful)

    return render_template('new.html')
@app.route('/go', methods=['GET', 'POST'])
def go():
    if request.method == 'POST':
        if request.form['submit'] == 'add':

            name = request.form['name']
            db.child("todo").push(name)
            todo = db.child("todo").get()
            to = todo.val()
            return render_template('index.html', t=to.values())
        elif request.form['submit'] == 'delete':
            db.child("todo").remove()
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run()