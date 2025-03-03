from agency_swarm.agents import Agent


class SQLExecutor(Agent):
    def __init__(self):
        super().__init__(
            name="SQLExecutor",
            description="The SQLExecutor agent is responsible for executing SQL queries on a PostgreSQL database and generating insights from the results. It utilizes specific tools to manage database connections, execute queries, and summarize results.",
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
