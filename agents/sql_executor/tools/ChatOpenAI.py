from agency_swarm.tools import BaseTool
from pydantic import Field
import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatOpenAI(BaseTool):
    """
    A tool to summarize SQL query results using GPT-4.
    This tool takes the results of an SQL query as input and generates a concise summary
    or insights from the data. It handles large datasets and extracts meaningful information.
    """

    query_results: list = Field(
        ..., description="The results of an SQL query to be summarized."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method utilizes the fields defined above to perform the task of summarizing
        SQL query results using GPT-4.
        """
        try:
            # Format the query results into a string
            formatted_results = self.format_query_results(self.query_results)

            # Create a prompt for GPT-4
            prompt = (
                "Summarize the following SQL query results and provide insights:\n"
                f"{formatted_results}\n"
                "Summary:"
            )

            # Call the OpenAI API to get the summary
            response = openai.Completion.create(
                engine="gpt-4",
                prompt=prompt,
                max_tokens=150,
                temperature=0.5
            )

            # Extract the summary from the response
            summary = response.choices[0].text.strip()

            return summary

        except openai.error.OpenAIError as e:
            return f"An error occurred while accessing the OpenAI API: {e}"

    def format_query_results(self, results):
        """
        Format the query results into a string suitable for the GPT-4 prompt.
        """
        formatted = ""
        for row in results:
            formatted += ", ".join(map(str, row)) + "\n"
        return formatted

# Example usage:
# tool = ChatOpenAI(query_results=[("John Doe", 5), ("Jane Smith", 3)])
# summary = tool.run()
# print(summary)