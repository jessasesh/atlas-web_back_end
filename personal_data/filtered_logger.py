#!/usr/bin/env python3
"""
Function that obfuscates log message using regex
"""
import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Function that obfuscates log message
    """
    # construct regex pattern to match field=value format
    for field in fields:
        #  re.escape(field) and re.escape(separator)
        # treats each field string value and separator literally
        pattern = rf"{re.escape(field)}=.*?{re.escape(separator)}"
    #  re.sub to replace field values with redaction symbols
        message = re.sub(pattern, f"{field}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record and redact specified fields."""
        formatted_message = super().format(record)
        obfuscated_message = filter_datum(
            self.fields, self.REDACTION, formatted_message, self.SEPARATOR
        )
        return obfuscated_message
