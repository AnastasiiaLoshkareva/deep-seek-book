#This is just testing of Gemini API work - this file is not used in project
from google import genai

GEMINI_API_KEY=""
client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)