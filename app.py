from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename
from pymongo import MongoClient
from bson import ObjectId  # Import ObjectId
from datetime import datetime
import os
import json

UPLOAD_FOLDER = 'uploads'  # Define the upload folder

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Set the upload folder in the app config
# MongoDB Atlas connection string
client = MongoClient('mongodb+srv://krishbhat:b8ckN6OqOl9E9rsQ@cluster0.bg0ffqy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['fileuploads']
collection = db['uploads']

ALLOWED_EXTENSIONS = {'txt', 'docx', 'pdf', 'rtf', 'jpg', 'png', 'gif', 'bmp', 'svg', 'mp4', 'mov', 'avi', 'mkv', 'wmv', 'mp3', 'wav', 'flac', 'aac', 'ogg', 'doc', 'ppt', 'xls', 'pdf', 'odt', 'zip', 'rar', 'tar.gz', '7z', 'bz2', 'py', 'java', 'c', 'cpp', 'html', 'css', 'js', 'xlsx', 'csv', 'ods', 'pptx', 'key', 'odp', 'db'}

MAX_FILE_SIZE_MB = 50  # Define the maximum file size in megabytes

def allowed_file(filename):
    # Check if the file extension is allowed
    if '.' not in filename or filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
        return False
    
    # Check the file size
    file_size_mb = request.content_length / (1024 * 1024)  # Convert bytes to megabytes
    if file_size_mb > MAX_FILE_SIZE_MB:
        return False
    
    return True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files[]' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    files = request.files.getlist('files[]')
    if len(files) == 0:
        return jsonify({'message': 'No files selected'}), 400
    uploaded_files = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Calculate file size in megabytes
            upload_data = {
                'filename': filename,
                'extension': file.filename.rsplit('.', 1)[1].lower(),
                'size_mb': file_size_mb,  # Use calculated file size
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Convert datetime to string
                'status': 'Uploaded'
            }
            inserted_id = collection.insert_one(upload_data).inserted_id
            upload_data['_id'] = str(inserted_id)  # Convert ObjectId to string
            uploaded_files.append(upload_data)
        else:
            return jsonify({'message': f'One or more files are not allowed or exceed the maximum size of {MAX_FILE_SIZE_MB} MB'}), 400
    return jsonify({'message': 'Files successfully uploaded', 'data': uploaded_files}), 201

@app.route('/uploads', methods=['GET'])
def get_uploads():
    uploads = list(collection.find({}, {'_id': False}))  # Exclude _id field
    for upload in uploads:
        upload['date'] = upload['date'].strftime('%Y-%m-%d %H:%M:%S')  # Format datetime
    return jsonify({'uploads': uploads}), 200  # Return the uploads directly without using json.loads and json.dumps

# CSS styles


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
