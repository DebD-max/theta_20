from agency_swarm.tools import BaseTool
from pydantic import Field
import psycopg2
from psycopg2 import sql, OperationalError

# Define global constants for database connection
DB_HOST = "your_db_host"
DB_PORT = "your_db_port"
DB_NAME = "your_db_name"
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"

class QuerySQLDatabaseTool(BaseTool):
    """
    A tool to execute SQL queries on a PostgreSQL database.
    This tool takes an SQL query as input and returns the results of the query execution.
    It handles connection management, query execution, and error handling.
    """

    sql_query: str = Field(
        ..., description="The SQL query to be executed on the PostgreSQL database."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method utilizes the fields defined above to perform the task of executing
        SQL queries on a PostgreSQL database.
        """
        try:
            # Establish a connection to the PostgreSQL database
            connection = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )

            # Create a cursor object to execute the SQL query
            cursor = connection.cursor()

            # Execute the SQL query
            cursor.execute(self.sql_query)

            # Fetch the results of the query execution
            results = cursor.fetchall()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            # Return the results
            return results

        except OperationalError as e:
            return f"An error occurred while connecting to the database: {e}"

        except Exception as e:
            return f"An error occurred during query execution: {e}"

# Example usage:
# tool = QuerySQLDatabaseTool(sql_query="SELECT * FROM customers WHERE purchase_count > 5;")
# results = tool.run()
# print(results)