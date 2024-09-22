#!/usr/bin/env python 3
"""
Function that returns obfuscacted log message
"""
import re
from typing import List


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Returns obfuscated data
    """
    escaped_fields = [re.escape(field) for field in fields]
    filter = r'(' + '|'.join(escaped_fields) + r')=([^;{}]+)'.format(separator)

    return re.sub(filter, r'\1=' + redaction, message)
