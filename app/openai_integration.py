import requests as requests
from openai import OpenAI
from flask import current_app as app


config = {
  "OPENAI_API_KEY": "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",
  "endpoints": {
    "image_prompt": "http://10.0.0.199:1234/v1/chat/completions",
    "image": "http://localhost:9821/get-image",
    "chat_completion": "http://10.0.0.199:1234/v1/chat/completions"
  },
  "limits": {
    "image_prompt": 512,
    "max_context_tail": 1024,
    "min_tokens": 150,
    "max_tokens": 1024
  },
  "streaming": {
    "obs" : {
      "host": "10.0.0.182",
      "port": 4455,
      "password": "ZBIpz077QZtKcAe0"
    }
  },
  "secret": "F9fOYN+r4hDUN0bEZN9zqX6FlzmtNIm3",
  "oauth": {
    "google" : {
      "client_id": "questar.vrzchampions.world",
      "secret": ""
    },
    "facebook" : {
      "client_id": "questar.vrzchampions.world",
      "secret": ""
    }
  },
  "temperature": 1,
  "frequency_penalty": 0.1
}


# Initialize OpenAI with the API key from the environment variable
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=config['OPENAI_API_KEY'],
)


def suggest_emoji_sequence(system, prompt):
    try:
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
