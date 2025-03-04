from agency_swarm.agents import Agent


class NL2SQLAgent(Agent):
    def __init__(self):
        super().__init__(
            name="NL2SQLAgent",
            description="Converts natural language queries into SQL queries and executes them on a PostgreSQL database.",
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
