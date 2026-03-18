from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from app.core.config import get_settings
from app.core.constants import COLLECTION_ATTENDANCE, COLLECTION_EMPLOYEES

_client: MongoClient | None = None


def connect_to_mongo() -> MongoClient:
    global _client
    if _client is None:
        settings = get_settings()
        _client = MongoClient(settings.mongodb_uri)
    return _client


def close_mongo_connection() -> None:
    global _client
    if _client is not None:
        _client.close()
        _client = None


def get_database() -> Database:
    settings = get_settings()
    client = connect_to_mongo()
    return client[settings.mongodb_db_name]


def get_employee_collection() -> Collection:
    return get_database()[COLLECTION_EMPLOYEES]


def get_attendance_collection() -> Collection:
    return get_database()[COLLECTION_ATTENDANCE]