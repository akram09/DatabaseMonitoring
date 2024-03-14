import sys

from loguru import logger


def formatter(record):
    # check if the record has extra data
    if "job_id" in record["extra"]:
        extra_text = " [job_id=" + record["extra"]["job_id"] + "]"
        logging_format = (
            "<magenta>"
            + extra_text
            + "</magenta> | <green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>\n"
        )
    else:
        logging_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>\n"
    return logging_format


def configure_logger():
    # configure logging format
    logger.remove()
    logger.add(sink=sys.stdout, format=formatter, level="INFO")
