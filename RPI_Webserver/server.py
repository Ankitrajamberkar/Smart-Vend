from flask import Flask, render_template, request, send_file
import os

from qrgenerator import generate_qrcode
x = 1


app = Flask(__name__)



@app.route('/',methods=['GET','POST'])
def index():
    return render_template('landingpage.html')



@app.route('/ordersnacks',methods=['GET','POST'])
def ordersnacks():
    return render_template('snaksorderpage.html')

@app.route('/aboutus',methods=['GET','POST'])
def aboutus():
    return render_template('about_us.html')

uploads_dir = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads_dir, exist_ok=True)

@app.route('/uploadfile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('fileUpload.html', message='No file part')

        file = request.files['file']

        # If the user submits an empty form
        if file.filename == '':
            return render_template('fileUpload.html', message='No selected file')

        # If the file is selected and has an allowed extension (e.g., .txt, .jpg, .png)
        if file:
            # Save the file to the 'uploads' directory
            file.save(os.path.join(uploads_dir, file.filename))

            return render_template('fileUpload.html', message='File uploaded successfully')

    return render_template('fileUpload.html')



@app.route('/showqrcode', methods=['GET', 'POST'])
def showqrcode():
    qrfile = generate_qrcode("Vishwas C")
    print(qrfile)
    return render_template('qrcode.html')

# Error handling for any error
@app.errorhandler(Exception)
def handle_error(error):
    return render_template('error.html', error=error), 500


if __name__ == '__main__':
    # Use a custom IP address and port
    app.run(host='127.0.0.1', port=8080, debug=True)
