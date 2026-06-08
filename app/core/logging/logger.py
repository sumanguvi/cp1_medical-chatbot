"""Logging configuration."""

import sys

from loguru import logger

from app.core.config.settings import settings

logger.remove()

logger.add(
    sys.stdout,
    level=settings.LOG_LEVEL,
    format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}'
)

logger.add(
    'logs/application.log',
    rotation='10 MB',
    retention='10 days',
    level=settings.LOG_LEVEL
)
