import requests


class LLMService:

    def generate(self, prompt: str):

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen3:8b",
                "prompt": prompt,
                "stream": False
            },
            timeout=300
        )

        return response.json()["response"]