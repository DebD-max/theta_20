from agency_swarm.agents import Agent


class QueryParser(Agent):
    def __init__(self):
        super().__init__(
            name="QueryParser",
            description="The QueryParser agent is responsible for parsing the natural language input from the user and identifying the key components needed for SQL query generation. It utilizes the 'create_sql_query_chain' tool to convert natural language queries into SQL.",
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
