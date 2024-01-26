import qdrant_client


class DatabaseConnectionError(Exception):
    """Exception raised when the database connection operation fails."""
    pass


def create_database_connection():
    """Create a database connection."""
    try:
        connection = connect_to_db()
        return connection
    except Exception as error:
        raise DatabaseConnectionError(
            "Failed to connect to the database") from error


def connect_to_db():
    """Connect to the Qdrant database."""
    # Add your actual Qdrant database connection logic here
    client = qdrant_client.Client()
    client.connect(host="localhost", port=6333)
    return client
