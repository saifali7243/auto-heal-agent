import logging
import os

LOG_DIR = "logs"
LOG_FILE = "logs/system.log"

# Create logs directory if not exists
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)
