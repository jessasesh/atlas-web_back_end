#!/usr/bin/env python3
"""
Function that obfuscates log message using regex
"""
import os
import mysql.connector
import re
import logging
from typing import List


PII_FIELDS = ("name", "ssn", "password", "phone", "email")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Function that obfuscates log message
    """
    for field in fields:
        pattern = rf"{re.escape(field)}=.*?{re.escape(separator)}"
        message = re.sub(pattern, f"{field}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record and redact specified fields."""
        formatted_message = super().format(record)
        obfuscated_message = filter_datum(
            self.fields, self.REDACTION, formatted_message, self.SEPARATOR
        )
        return obfuscated_message


def get_logger() -> logging.Logger:
    """
    Get object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connects to mysql db
    """
    db_username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    connection = mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )
    return connection

logging.basicConfig(
    format='[HOLBERTON] user_data INFO %(asctime)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

def get_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='my_db'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        logging.error(f"Error connecting to MySQL: {e}")
        return None

def main():
    """
    Implement a main function
    """
    connection = get_db()
    if connection is None:
        return
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    for row in rows:
        filtered_data = (
            f"name=***; email=***; phone=***; ssn=***; password=***; "
            f"ip={row['ip']}; last_login={row['last_login']}; user_agent={row['user_agent']}"
        )
        logging.info(filtered_data)
    
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
