from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from com_in_ineuron_ai_utils.utils import decodeImage
from predict import dogcat

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "input.jpg"
        self.classifier = dogcat(self.filename)


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')
    

@app.route("/predict", methods=['POST'])
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictiondogcat()
    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(debug=True)
    os.remove("input.jpg")