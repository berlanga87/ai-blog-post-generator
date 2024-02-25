from flask import Flask, jsonify, request, render_template
from openai import OpenAI
import os
import json
import random
import requests
import together

import logging

logger = logging.getLogger(__name__)


logger.setLevel(logging.DEBUG)


handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

app = Flask(__name__)

TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")
together.api_key = os.environ.get("TOGETHER_API_KEY")

client = OpenAI(api_key=TOGETHER_API_KEY,
  base_url='https://api.together.xyz',
)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        topic = request.form['topic']
        chat_completion = client.chat.completions.create(
          messages=[
            {"role": "system", "content": "You are a creative AI trained to write informative and engaging blog posts."},
            {"role": "user", "content": f"Write a blog post about {topic}."},
          ],
          model="mistralai/Mixtral-8x7B-Instruct-v0.1",
          max_tokens=512
        )

        generated_post = chat_completion.choices[0].message.content
        return render_template('result.html', topic=topic, generated_post=generated_post)
    return render_template('index.html')

@app.route('/get-topics')
def get_topics():
    with open('topics.json', 'r') as file:
        topics_data = json.load(file)
        topics_list = topics_data['topics']
    
    selected_topics = random.sample(topics_list, 5)
    return jsonify(selected_topics)

@app.route('/generate-image', methods=['POST'])
def gen_image():
    data = request.get_json()
    prompt = data.get('prompt', '')
    img_prompt = get_img_prompt(prompt)

    response = together.Image.create(
        prompt=img_prompt,
        model="stabilityai/stable-diffusion-2-1",
        height=400,
        width=600
    )

    image_data = response["output"]["choices"][0]
    return jsonify(image_data), 200


def get_img_prompt(topic):
    chat_completion = client.chat.completions.create(
        messages=[
        {"role": "system", "content": "You are a creative AI trained to create Stable Difussion prompts."},
        {"role": "user", "content": f"Generate a prompt for an image that will be shown with a blog post about {topic}. Return it in JSON format with 'prompt' as the key"},
        ],
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        max_tokens=1024
    )

    response = chat_completion.choices[0].message.content
    img_prompt = json.loads(response)['prompt']
    return img_prompt



if __name__ == '__main__':
    app.run(debug=True)


