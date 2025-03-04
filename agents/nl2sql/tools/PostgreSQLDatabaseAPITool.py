from agency_swarm.tools import BaseTool
from pydantic import Field
import psycopg2
from psycopg2 import sql, OperationalError, DatabaseError

class PostgreSQLDatabaseAPITool(BaseTool):
    """
    This tool enables the NL2SQLAgent to connect to a PostgreSQL database using the provided connection string.
    It facilitates executing SQL queries on the database and returning the results.
    """

    connection_string: str = Field(
        ..., description="The connection string for the PostgreSQL database in the format 'postgresql://username:password@hostname:port/database_name'."
    )
    query: str = Field(
        ..., description="The SQL query to be executed on the PostgreSQL database."
    )

    def connect_to_database(self):
        """
        Establishes a connection to the PostgreSQL database using the provided connection string.
        """
        try:
            connection = psycopg2.connect(self.connection_string)
            return connection
        except OperationalError as e:
            return f"Error connecting to the database: {e}"

    def execute_query(self, connection):
        """
        Executes the provided SQL query on the PostgreSQL database and returns the results.
        """
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql.SQL(self.query))
                if cursor.description:  # Check if the query returns data
                    results = cursor.fetchall()
                    return results
                else:
                    connection.commit()  # Commit if it's an INSERT/UPDATE/DELETE
                    return "Query executed successfully."
        except DatabaseError as e:
            return f"Error executing the query: {e}"

    def run(self):
        """
        The main method to connect to the database, execute the query, and return the results.
        """
        connection = self.connect_to_database()
        if isinstance(connection, str):  # If connection is an error message
            return connection

        try:
            result = self.execute_query(connection)
            return result
        finally:
            connection.close()