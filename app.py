#import the Flask class from flask
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_uploads import UploadSet, configure_uploads, IMAGES

#create the application object
app = Flask(__name__)

#use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('welcome.html') # render a template

#route for handling the login page logic
@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


#Image Uploader
app.config['SECRET_KEY'] = 'hardsecretkey'

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/images'

configure_uploads(app, photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return filename


    return render_template('upload.html')


#start the server with run()
if __name__ == "__main__":
    app.run(debug=True)
