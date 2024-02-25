from flask import Flask, request, render_template
from openai import OpenAI
import os

app = Flask(__name__)

TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")

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
          max_tokens=1024
        )

        generated_post = chat_completion.choices[0].message.content
        return render_template('result.html', topic=topic, generated_post=generated_post)
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)


