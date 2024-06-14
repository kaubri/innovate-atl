#!/bin/python3

import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

from flask import Flask, render_template, request, json
from config import OPENAI_API_KEY  # Import the API key
from openai import OpenAI

# Create instance of Flask application
app = Flask(__name__)

# Configure the OpenAI API key
client = OpenAI(
    # This is the default and can be omitted
    api_key=OPENAI_API_KEY,
)

system_guidance = '''Process this community service request. Requests should fall within 3 categories:
Infrastructure Installation, Infrastructure Maintenace, or Public Safety Concerns.
Provide a JSON response (not in markdown) with the location and category from the user's prompt: '''

def process_user_prompt(prompt): 
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", # 60K TPM, 500 RPM, 10K RPD, 200K TPD
        messages=[
            {
                "role": "system",
                "content": system_guidance,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    y = json.loads(response.choices[0].message.content)

    return prompt, system_guidance + prompt, y, y["location"], y["category"]

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    prompt = request.form['prompt']
    user_prompt, system_prompt, system_response, location, category = process_user_prompt(prompt)
    return render_template('submission.html', user_prompt_p=user_prompt, system_prompt_p=system_prompt, system_response_p=system_response, loc=location, cat=category)

app.run(debug=True, host='0.0.0.0', port=5000)