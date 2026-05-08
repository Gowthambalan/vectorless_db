# import requests

# OLLAMA_URL = "http://localhost:11434/api/generate"

# def generate_response(prompt: str):
#     response = requests.post(
#         OLLAMA_URL, 
#         json={
#             "model": "llama3",
#             "prompt": prompt,
#             "stream": False
#         }
#     )
#     return response.json()["response"]



import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_response(prompt: str):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3:8b",
                "prompt": prompt,
                "stream": False
            }
        )

        print("STATUS:", response.status_code)
        print("RAW:", response.text)  # 👈 MUST SEE THIS

        data = response.json()

        # ✅ SAFE HANDLING
        if "response" in data:
            return data["response"]

        elif "error" in data:
            return f"Ollama Error: {data['error']}"

        else:
            return f"Unexpected response: {data}"

    except Exception as e:
        return f"Exception: {str(e)}"
