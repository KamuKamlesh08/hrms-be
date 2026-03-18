from app.core.constants import (
    ALLOWED_ATTENDANCE_STATUSES,
    ERR_ATTENDANCE_ALREADY_MARKED,
    ERR_INVALID_ATTENDANCE_STATUS,
)
from app.core.exceptions import (
    AttendanceAlreadyMarkedException,
    InvalidAttendanceStatusException,
)
from app.core.logger import get_logger
from app.repositories.attendance_repository import AttendanceRepository
from app.services.employee_service import EmployeeService

logger = get_logger(__name__)


class AttendanceService:
    def __init__(self) -> None:
        self.attendance_repository = AttendanceRepository()
        self.employee_service = EmployeeService()

    def mark_attendance(self, employee_id: str, date: str, status: str) -> dict:
        normalized_employee_id = employee_id.strip()
        normalized_date = date.strip()
        normalized_status = status.strip().upper()

        if normalized_status not in ALLOWED_ATTENDANCE_STATUSES:
            logger.warning("Invalid attendance status attempted: %s", status)
            raise InvalidAttendanceStatusException(ERR_INVALID_ATTENDANCE_STATUS, status_code=400)

        self.employee_service.ensure_employee_exists(normalized_employee_id)

        existing = self.attendance_repository.get_attendance_by_employee_and_date(
            normalized_employee_id,
            normalized_date,
        )
        if existing:
            logger.warning(
                "Duplicate attendance attempted for employee_id=%s date=%s",
                normalized_employee_id,
                normalized_date,
            )
            raise AttendanceAlreadyMarkedException(ERR_ATTENDANCE_ALREADY_MARKED, status_code=409)

        attendance_doc = self.attendance_repository.build_attendance_document(
            employee_id=normalized_employee_id,
            date=normalized_date,
            status=normalized_status,
        )
        self.attendance_repository.create_attendance(attendance_doc)
        logger.info(
            "Attendance marked successfully for employee_id=%s date=%s status=%s",
            normalized_employee_id,
            normalized_date,
            normalized_status,
        )
        return attendance_doc

    def get_all_attendance(self, date: str | None = None) -> list[dict]:
        attendance_records = self.attendance_repository.get_all_attendance(date=date)
        logger.info("Fetched %s attendance records.", len(attendance_records))
        return attendance_records

    def get_attendance_by_employee_id(self, employee_id: str) -> list[dict]:
        normalized_employee_id = employee_id.strip()
        self.employee_service.ensure_employee_exists(normalized_employee_id)
        attendance_records = self.attendance_repository.get_attendance_by_employee_id(normalized_employee_id)
        logger.info(
            "Fetched %s attendance records for employee_id=%s",
            len(attendance_records),
            normalized_employee_id,
        )
        return attendance_records