import sys
from loguru import logger


class BSLogger:

    def __init__(self, log_file_path: str, debug: bool = True, level: str = "INFO", rotation: str = "10 MB", compression: str = "zip", retention: str = "1 month"):
        logger.remove()
        logger.add(
            log_file_path,
            level=level,
            rotation=rotation,
            compression=compression,
            retention=retention
        )
        if debug:
            logger.add(sys.stdout, level="DEBUG")

    @staticmethod
    def info(msg: str) -> None:
        logger.info(msg)

    @staticmethod
    def error(msg: str) -> None:
        logger.error(msg)

    @staticmethod
    def warning(msg: str) -> None:
        logger.warning(msg)

    @staticmethod
    def success(msg: str):
        logger.success(msg)

    @staticmethod
    def debug(msg: str) -> None:
        logger.debug(msg)

    @staticmethod
    def trace(msg: str) -> None:
        logger.trace(msg)
