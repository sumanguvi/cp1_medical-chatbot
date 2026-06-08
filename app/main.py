"""Main FastAPI application."""

from fastapi import FastAPI

from app.core.config.settings import settings
from app.core.logging.logger import logger

app = FastAPI(
    title=settings.PROJECT_NAME
)


@app.get('/')
async def root() -> dict:
    """Health check endpoint."""

    logger.info('Healthcare AI system started')

    return {
        'message': 'AI Healthcare System Running'
    }
