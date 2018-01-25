from flask import Flask, render_template, request
import base64
from PIL import Image
import PIL.ImageOps    
from io import BytesIO, StringIO

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/process",methods=['POST'])
def process():
    data = request.form['imgData']

    binary_data = base64.b64decode(request.values['imgData'].split(',')[-1])
    image_data = Image.open(BytesIO(binary_data)).convert('RGB')
    
    buffer = BytesIO()
    PIL.ImageOps.invert(image_data).save(buffer, format="JPEG")
    img_str = base64.b64encode(buffer.getvalue())
    """fd = open('image.png', 'wb')
    fd.write(binary_data)
    fd.close()"""
    return img_str