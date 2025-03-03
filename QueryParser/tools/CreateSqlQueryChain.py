from agency_swarm.tools import BaseTool
from pydantic import Field
from langchain import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Initialize the OpenAI model
llm = OpenAI(model="text-davinci-003", api_key="YOUR_OPENAI_API_KEY")

class CreateSqlQueryChain(BaseTool):
    """
    A tool to convert natural language queries into SQL queries.
    This tool takes a natural language input and parses it to identify key components
    such as tables, columns, conditions, and operations needed for SQL query generation.
    It constructs a valid SQL query based on these components.
    """

    natural_language_query: str = Field(
        ..., description="The natural language query to be converted into an SQL query."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method utilizes the fields defined above to perform the task of converting
        natural language queries into SQL queries.
        """
        # Define the prompt template for the LLM
        prompt_template = PromptTemplate(
            input_variables=["query"],
            template=(
                "Convert the following natural language query into an SQL query:\n"
                "Query: {query}\n"
                "SQL Query:"
            )
        )

        # Create the LLM chain with the prompt template
        sql_chain = LLMChain(llm=llm, prompt=prompt_template)

        # Run the chain with the natural language query
        sql_query = sql_chain.run(self.natural_language_query)

        # Return the generated SQL query
        return sql_query

# Example usage:
# tool = CreateSqlQueryChain(natural_language_query="Show me all customers who purchased more than 5 items.")
# sql_query = tool.run()
# print(sql_query)