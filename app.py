from flask import Flask, request, render_template, send_file
import os
from werkzeug.utils import secure_filename
from translator import translate_images

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'output'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_files = request.files.getlist("images")
        image_paths = []

        for file in uploaded_files:
            if file:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                image_paths.append(filepath)

        output_zip_path = os.path.join(app.config['OUTPUT_FOLDER'], "translated_images.zip")
        translate_images(image_paths, output_zip_path)

        return send_file(output_zip_path, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
