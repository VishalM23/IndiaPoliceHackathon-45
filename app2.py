import pyrebase

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

db = firebase.database()

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
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
	app.run(debug=True)
