from app.core.logger import get_logger
from app.db.indexes import create_indexes
from app.db.mongo import close_mongo_connection, connect_to_mongo

logger = get_logger(__name__)


def on_startup() -> None:
    connect_to_mongo()
    create_indexes()
    logger.info("Application startup completed successfully.")


def on_shutdown() -> None:
    close_mongo_connection()
    logger.info("Application shutdown completed successfully.")