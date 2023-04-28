import mysql.connector


def get_database_connection():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pythonLab",
            port=3307
        )
    except mysql.connector.Error as error:
        print(f"Failed to Connect to MySQL: {error}")

    return db
