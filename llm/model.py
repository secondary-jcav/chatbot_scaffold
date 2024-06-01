import aiohttp
from dotenv import load_dotenv, find_dotenv
import json
import os


class Model:
    def __init__(self) -> None:
        _ = load_dotenv(find_dotenv())
        self.token = os.environ["API_KEY"]
        self.session = aiohttp.ClientSession()
        self.url = "https://api.openai.com/v1/chat/completions"

    async def send_query(self, query):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
        }
        with open("llm/prompts.json", "r") as file:
            data = json.load(file)
        data["messages"][1][
            "content"
        ] = query  # Change this according to response's format
        async with self.session.post(
            self.url, headers=headers, data=json.dumps(data)
        ) as response:
            if response.status == 200:
                response_json = await response.json()
                return response_json["choices"][0]["message"][
                    "content"
                ]  # Change this according to response's format
            else:
                print(f"Error: {response.status}")
