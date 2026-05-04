import os
import sys
import logging

logging_str = "[%(asctime)s - %(name)s - %(levelname)s - %(message)s]"

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logfile_path = os.path.join(log_dir, "logging.log")


logging.basicConfig(
    level=logging.INFO,
    format= logging_str,
    handlers=[
        logging.FileHandler(logfile_path),
        logging.StreamHandler(sys.stdout)
    ]
    
)

logger= logging.getLogger("DatascienceLogger")


 