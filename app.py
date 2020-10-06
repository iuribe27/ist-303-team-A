#import the Flask class from flask
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_uploads import UploadSet, configure_uploads, secure_filename, IMAGES, os

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


#Profile Image Uploader
app.config['SECRET_KEY'] = 'hardsecretkey'

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/images'
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]

def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

configure_uploads(app, photos)

@app.route('/upload_image')
def upload_form():
    return render_template('upload_image.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            if image.filename == "":
                flash("No filename")
                return redirect(request.url)

            if allowed_image(image.filename):
                filename = secure_filename(image.filename)

                image.save(os.path.join(app.config["UPLOADED_PHOTOS_DEST"], filename))

                flash("Image uploaded")

                return render_template('upload_image.html', filename=filename)

            else:
                flash("That file extension is not allowed")
                return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='images/' + filename), code=301)

##END for Profile Image Uploader

#start the server with run()
if __name__ == "__main__":
    app.run(debug=True)
