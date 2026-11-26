
from loguru import logger
from pathlib import Path

# Define log directory
LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Remove default logger
logger.remove()

# Console logging
logger.add(
    sink=lambda message: print(message, end=""),
    level="INFO",
    colorize=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

# File logging
logger.add(
    sink=LOG_DIR / "app_{time:YYYY-MM-DD}.log",
    level="DEBUG",
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    enqueue=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} | {message}"
)