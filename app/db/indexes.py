from pymongo import ASCENDING

from app.core.logger import get_logger
from app.db.mongo import get_attendance_collection, get_employee_collection

logger = get_logger(__name__)


def create_indexes() -> None:
    employee_collection = get_employee_collection()
    attendance_collection = get_attendance_collection()

    employee_collection.create_index([("employee_id", ASCENDING)], unique=True, name="uq_employee_id")
    employee_collection.create_index([("email", ASCENDING)], unique=True, name="uq_employee_email")

    attendance_collection.create_index(
        [("employee_id", ASCENDING), ("date", ASCENDING)],
        unique=True,
        name="uq_employee_date",
    )
    attendance_collection.create_index([("employee_id", ASCENDING)], name="idx_attendance_employee_id")
    attendance_collection.create_index([("date", ASCENDING)], name="idx_attendance_date")

    logger.info("MongoDB indexes created successfully.")