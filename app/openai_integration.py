import json

import requests as requests
from openai import OpenAI
from flask import current_app as app


def suggest_emoji_sequence(system, prompt):
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)

        chat_completion_data = {
            "model": "gpt-3.5-turbo",
            "max_tokens": config["limits"]["max_tokens"],
            "messages": [
                {
                    "role": "system",
                    "content": system
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": config["temperature"] if "temperature" in config else 1,
            "frequency_penalty": config["frequency_penalty"] if "frequency_penalty" in config else 0
        }

        response = requests.post(config["endpoints"]["chat_completion"], json=chat_completion_data).json()
        suggestion = response["choices"][0]["message"]["content"].strip()

        return suggestion

        # # Call the OpenAI API with the prompt to get a suggestion
        # response = client.chat.completions.create(
        #     messages=[
        #         {
        #             "role": "system",
        #             "content": system,
        #         },
        #         {
        #             "role": "user",
        #             "content": prompt,
        #         }
        #     ],
        #     model="gpt-3.5-turbo",
        #     max_tokens=2048,  # Adjust based on the expected length of completion
        #     n=1,  # Number of completions to generate
        #     stop=None,  # Any stopping criteria if needed
        #     temperature=0.8  # The creativity of the response; tweak as needed
        # )
        # suggestion = response.choices[0].text.strip()
        # return suggestion
    except Exception as e:
        # Handle OpenAI errors
        app.logger.error(f"OpenAI API error: {e}")
        return None
