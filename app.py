from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle, random

app = Flask(__name__)
CORS(app)    # ← VERY IMPORTANT!

model_data = pickle.load(open("model.pkl", "rb"))
model = model_data["model"]
vectorizer = model_data["vectorizer"]
data = model_data["data"]["intents"]


#main AI route
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    X = vectorizer.transform([user_msg])
    tag = model.predict(X)[0]

    for intent in data:
        if intent["tag"] == tag:
            return jsonify({"reply": random.choice(intent["responses"])})

    return jsonify({"reply": "Sorry, I didn’t understand that."})

if __name__ == "__main__":
    app.run(debug=True)
