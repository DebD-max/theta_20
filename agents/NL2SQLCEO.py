from agency_swarm.agents import Agent


class NL2SQLCEO(Agent):
    def __init__(self):
        super().__init__(
            name="NL2SQLCEO",
            description="Acts as the central coordinator for the agency, managing communication between agents and ensuring smooth operation.",
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
