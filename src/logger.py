
import logging
import os
from datetime import datetime

# 1. Generate a unique-looking log filename
LOG_FILE = (
    f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S_%f')}.log"
)

# 2. Create the logs directory
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# 3. Build the complete log file path
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# 4. Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format=(
        "[ %(asctime)s ] %(lineno)d %(name)s "
        "- %(levelname)s - %(message)s"
    ),
    level=logging.INFO,
)