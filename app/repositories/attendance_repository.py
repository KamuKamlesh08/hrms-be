from datetime import datetime

from pymongo.results import InsertOneResult

from app.core.constants import STATUS_ABSENT, STATUS_PRESENT
from app.db.mongo import get_attendance_collection


class AttendanceRepository:
    def create_attendance(self, attendance_data: dict) -> InsertOneResult:
        return get_attendance_collection().insert_one(attendance_data)

    def get_attendance_by_employee_and_date(self, employee_id: str, date: str) -> dict | None:
        return get_attendance_collection().find_one(
            {"employee_id": employee_id, "date": date},
            {"_id": 0},
        )

    def get_attendance_by_employee_id(self, employee_id: str) -> list[dict]:
        return list(
            get_attendance_collection()
            .find({"employee_id": employee_id}, {"_id": 0})
            .sort([("date", -1), ("created_at", -1)])
        )

    def get_all_attendance(self, date: str | None = None) -> list[dict]:
        query = {"date": date} if date else {}
        return list(
            get_attendance_collection()
            .find(query, {"_id": 0})
            .sort([("date", -1), ("created_at", -1)])
        )

    def count_by_status_for_date(self, date: str, status: str) -> int:
        return get_attendance_collection().count_documents({"date": date, "status": status})

    def count_present_for_date(self, date: str) -> int:
        return self.count_by_status_for_date(date, STATUS_PRESENT)

    def count_absent_for_date(self, date: str) -> int:
        return self.count_by_status_for_date(date, STATUS_ABSENT)

    @staticmethod
    def build_attendance_document(
        employee_id: str,
        date: str,
        status: str,
    ) -> dict:
        now = datetime.utcnow()
        return {
            "employee_id": employee_id,
            "date": date,
            "status": status,
            "created_at": now,
            "updated_at": now,
        }