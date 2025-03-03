from agency_swarm.tools import BaseTool
from pydantic import Field
import requests
import os

# Define your API key and endpoint
api_key = os.getenv("OPENAI_API_KEY")
api_endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"

class LLMApiTool(BaseTool):
    """
    This tool enables the DataSummarizerAgent to interact with a Language Model API to process raw data
    and generate a coherent and concise summary. It handles sending data to the API, receiving the response,
    and returning the summary to the agent.
    """

    raw_data: str = Field(
        ..., description="The raw data that needs to be summarized by the Language Model API."
    )

    def format_data(self):
        """
        Formats the raw data into a prompt suitable for the Language Model API.
        """
        prompt = f"Summarize the following data:\n\n{self.raw_data}\n\nSummary:"
        return prompt

    def send_request_to_api(self, prompt):
        """
        Sends a request to the Language Model API with the formatted prompt and returns the response.
        """
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.5
        }
        try:
            response = requests.post(api_endpoint, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return f"Error sending request to the API: {e}"

    def process_response(self, response):
        """
        Processes the API response to extract and return the summary.
        """
        try:
            summary = response['choices'][0]['text'].strip()
            return summary
        except (KeyError, IndexError) as e:
            return f"Error processing the API response: {e}"

    def run(self):
        """
        The main method to format the data, send it to the API, and return the summary.
        """
        prompt = self.format_data()
        response = self.send_request_to_api(prompt)
        if isinstance(response, str):  # If response is an error message
            return response

        summary = self.process_response(response)
        return summary