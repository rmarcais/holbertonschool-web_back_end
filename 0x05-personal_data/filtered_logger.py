#!/usr/bin/env python3
"""Task 0. Regex-ing"""

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the log messafe obfuscated"""
    for field in fields:
        pattern = r"(?<={}=)[\w*\d*\/.@-]+(?={})".format(field, separator)
        message = re.sub(pattern, redaction, message)
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
        """Filters values in incoming log records using filter_datum
        """
        m = super().format(record)
        message = filter_datum(self.fields, self.REDACTION, m, self.SEPARATOR)
        return message
