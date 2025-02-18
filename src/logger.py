import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Ym%d-%y-%H-%M-%S')}.log"
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PAT = os.path.join(log_path,LOG_FILE)