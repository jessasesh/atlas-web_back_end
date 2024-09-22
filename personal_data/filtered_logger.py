#!/usr/bin/env python3
"""
Function that obfuscates log message using regex
"""
import re
import logging
from typing import List

PII_FIELDS = ("email", "ssn", "password", "address", "phone_number")


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
