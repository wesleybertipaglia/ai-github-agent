from google import genai
from settings import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def resumir_issues(issues: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=f"Resuma as seguintes issues do GitHub:\n{issues}"
    )
    return response.text
