
from config.file_path import log_path
from loguru import logger

logger.add(log_path, encoding='utf-8')
