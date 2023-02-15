import os

import openai
from flask import Flask, redirect, render_template, request, url_for, jsonify

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "GET":
        query_parameters = request.args
        if query_parameters.get("prompt"):
            prompt = query_parameters.get("prompt")
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.6,
                max_tokens=4000-int(len(prompt)/5),
            )
            return jsonify(response.choices[0].text)
        return jsonify('No prompt provided')
    return jsonify('ChatGPT API')