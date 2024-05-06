import json

import requests as requests
from flask import current_app as app


def suggest_emoji_sequence(prompt):
    try:
        system = open("assets/suggestion_system_prompt.txt").read()
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)

        chat_completion_data = {
            "model": "Meta-Llama-3-8B-Instruct-Q6_K.gguf",
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
    except Exception as e:
        # Handle OpenAI errors
        app.logger.error(f"OpenAI API error: {e}")
        return None
