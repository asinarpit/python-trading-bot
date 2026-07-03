import logging
import os

def setup_logger():
    logger = logging.getLogger("trading_bot")
    
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("trading_bot.log", mode="a")
    
    # log message format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    return logger
