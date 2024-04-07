from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os
from urllib.parse import urlencode

app = Flask(__name__)

# Define the upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to process the uploaded files
def process_files(source_file, target_file):
    # Your processing logic goes here
    # For simplicity, let's just return the target file path
    return target_file


@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'source_file' not in request.files or 'target_file' not in request.files:
            return redirect(request.url)

        source_file = request.files['source_file']
        target_file = request.files['target_file']

        # If the user does not select a file, the browser submits an empty file without a filename
        if source_file.filename == '' or target_file.filename == '':
            return redirect(request.url)

        if source_file and target_file:
            # Save the files to the upload folder
            source_filename = secure_filename(source_file.filename)
            target_filename = secure_filename(target_file.filename)
            
            source_file_path = os.path.join(app.config['UPLOAD_FOLDER'], source_filename)
            target_file_path = os.path.join(app.config['UPLOAD_FOLDER'], target_filename)
            # source_file_path = os.path.join("./public", source_filename)
            # target_file_path = os.path.join("./public", target_filename)
            source_file.save(source_file_path)
            target_file.save(target_file_path)

            # print("Uploaded Source File Path:", source_file_path)
            # print("Uploaded Target File Path:", target_file_path)
    
            print("Uploaded Source File Path:", source_file_path)
            print("Uploaded Target File Path:", target_file_path)
            os.system("cd roop") 
             


            

            # Process the files
            # processed_file_path = process_files(source_file_path, target_file_path)

            # return render_template('result.html', processed_file=processed_file_path)
            return render_template('check.html', sf = source_filename, tf = target_filename)
        

    return render_template('upload.html')





@app.route('/up', methods=['GET', 'POST'])
def or_upload_files():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'source_file' not in request.files or 'target_file' not in request.files:
            return redirect(request.url)

        source_file = request.files['source_file']
        target_file = request.files['target_file']

        # If the user does not select a file, the browser submits an empty file without a filename
        if source_file.filename == '' or target_file.filename == '':
            return redirect(request.url)

        if source_file and target_file:
            # Save the files to the upload folder
            source_filename = secure_filename(source_file.filename)
            target_filename = secure_filename(target_file.filename)

            source_file_path = os.path.join(app.config['UPLOAD_FOLDER'], source_filename)
            target_file_path = os.path.join(app.config['UPLOAD_FOLDER'], target_filename)
            source_file.save(source_file_path)
            target_file.save(target_file_path)

            print("Uploaded Source File Path:", source_file_path)
            print("Uploaded Target File Path:", target_file_path)

            # Process the files
            processed_file_path = process_files(source_file_path, target_file_path)

            return render_template('result.html', processed_file=processed_file_path)

    return render_template('upload.html')



# @app.route('/', methods=['GET', 'POST'])
# def upload_files():
#     if request.method == 'POST':
#         # Check if the POST request has the file part
#         if 'source_file' not in request.files or 'target_file' not in request.files:
#             return redirect(request.url)

#         source_file = request.files['source_file']
#         target_file = request.files['target_file']

#         # If the user does not select a file, the browser submits an empty file without a filename
#         if source_file.filename == '' or target_file.filename == '':
#             return redirect(request.url)

#         if source_file and target_file:
#             # Save the files to the upload folder
#             source_filename = secure_filename(source_file.filename)
#             target_filename = secure_filename(target_file.filename)
#             source_file_path = os.path.join(app.config['UPLOAD_FOLDER'], source_filename)
#             target_file_path = os.path.join(app.config['UPLOAD_FOLDER'], target_filename)
#             source_file.save(source_file_path)
#             target_file.save(target_file_path)

#             # Process the files
#             processed_file_path = process_files(source_file_path, target_file_path)

#             return render_template('result.html', processed_file=processed_file_path)

#     return render_template('upload.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
