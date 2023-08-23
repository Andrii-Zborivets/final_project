from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    score = response[dominant_emotion]

    label = dominant_emotion.capitalize()
    score_formatted = "{:.2%}".format(score)

    result_text = f"For the given statement, the system response is {label}: {score_formatted}. The dominant emotion is {dominant_emotion}"
    return result_text

@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5500)