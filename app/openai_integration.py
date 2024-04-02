from openai import OpenAI
from flask import current_app as app

# Initialize OpenAI with the API key from the environment variable
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=app.config['OPENAI_API_KEY'],
)


def suggest_emoji_sequence(system, prompt):
    try:
        # Call the OpenAI API with the prompt to get a suggestion
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system,
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
            max_tokens=2048,  # Adjust based on the expected length of completion
            n=1,  # Number of completions to generate
            stop=None,  # Any stopping criteria if needed
            temperature=0.8  # The creativity of the response; tweak as needed
        )
        suggestion = response.choices[0].text.strip()
        return suggestion
    except Exception as e:
        # Handle OpenAI errors
        app.logger.error(f"OpenAI API error: {e}")
        return None
