from flask import Flask, jsonify, request
from flask_cors import cross_origin

from yolo_detection_images import detectObjects

app =  Flask(__name__)
import io, base64
from PIL import Image

# Assuming base64_str is the string value without 'data:image/jpeg;base64,'

@app.route('/',methods = ['POST'])
@cross_origin(supports_credentials=True)
def detect():
     if request.method == 'POST':
        img = request.json['data']
        img1 = base64.b64decode(img)
        with open('images/dog123.jpeg', 'wb') as f:
            f.write(img1)
        
        return jsonify(detectObjects('images/dog123.jpeg'))

if __name__ == '__main__':
    app.run()
