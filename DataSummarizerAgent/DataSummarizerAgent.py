from agency_swarm.agents import Agent


class DataSummarizerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="DataSummarizerAgent",
            description="Takes raw data from the database and generates a user-readable summarized output.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        return message
