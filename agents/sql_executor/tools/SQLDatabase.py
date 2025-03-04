from agency_swarm.tools import BaseTool
from psycopg2 import pool, OperationalError

# Define global constants for database connection
DB_HOST = "your_db_host"
DB_PORT = "your_db_port"
DB_NAME = "your_db_name"
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"

class SQLDatabase(BaseTool):
    """
    A tool to manage connections to a PostgreSQL database.
    This tool provides methods to open and close connections, ensuring that connections
    are reused efficiently. It also handles connection pooling and manages connection errors.
    """

    def __init__(self):
        """
        Initialize the connection pool for the PostgreSQL database.
        """
        try:
            self.connection_pool = pool.SimpleConnectionPool(
                1,  # Minimum number of connections
                10, # Maximum number of connections
                host=DB_HOST,
                port=DB_PORT,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            if self.connection_pool:
                print("Connection pool created successfully")

        except OperationalError as e:
            print(f"An error occurred while creating the connection pool: {e}")

    def open_connection(self):
        """
        Open a connection from the connection pool.
        """
        try:
            connection = self.connection_pool.getconn()
            if connection:
                print("Successfully retrieved a connection from the pool")
            return connection

        except OperationalError as e:
            print(f"An error occurred while opening a connection: {e}")
            return None

    def close_connection(self, connection):
        """
        Close a connection and return it to the connection pool.
        """
        try:
            if connection:
                self.connection_pool.putconn(connection)
                print("Connection returned to the pool successfully")

        except Exception as e:
            print(f"An error occurred while closing the connection: {e}")

    def close_all_connections(self):
        """
        Close all connections in the connection pool.
        """
        try:
            self.connection_pool.closeall()
            print("All connections in the pool have been closed")

        except Exception as e:
            print(f"An error occurred while closing all connections: {e}")

# Example usage:
# db_tool = SQLDatabase()
# connection = db_tool.open_connection()
# # Use the connection for database operations
# db_tool.close_connection(connection)
# db_tool.close_all_connections()