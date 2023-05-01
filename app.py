#MUST Initilization
from flask import Flask, render_template
app = Flask(__name__)

Projects = [
    {
        'id': 1,
        'title': "Cartoon Character Recognition via Object Detection",
        'software': ['python','streamlit','YOLOv5'],
        'Description': "A  framework for character presence calculation using YOLOV5 Model with web deployment using streamlit",
    }

    {
        'id': 2,
        'title': "Traffic Light Fuzzy Logic",
        'software': ['python','sklearn'],
        'Description': " Traffic light simulation built on the mamdani fuzzy logic system using skfuzzy",
    }

    {
        'id': 3,
        'title': "Diagnosify",
        'software': ['python','Keras'],
        'Description': "The building of song/playlist depression indicator using deep learning model",
    }

    {
        'id': 4,
        'title': "ZeroMQ ScreenCapture",
        'software': ['C','C++','Python','OpenCV'],
        'Description': "",
    }
]

@app.route("/")
def hello_word():
  return render_template("home.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)