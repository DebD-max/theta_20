from agency_swarm import Agency
from DataSummarizerAgent import DataSummarizerAgent
from NL2SQLAgent import NL2SQLAgent
from NL2SQLCEO import NL2SQLCEO
from SQLExecutor import SQLExecutor
from QueryParser import QueryParser
from NL2SQLCEO import NL2SQLCEO

ceo = NL2SQLCEO()
query_parser = QueryParser()
sql_executor = SQLExecutor()

agency = Agency([ceo, [ceo, query_parser],
                 [query_parser, sql_executor],
                 [ceo, sql_executor]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio()