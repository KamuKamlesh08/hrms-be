from datetime import datetime

from pymongo.results import DeleteResult, InsertOneResult

from app.db.mongo import get_employee_collection


class EmployeeRepository:
    def create_employee(self, employee_data: dict) -> InsertOneResult:
        return get_employee_collection().insert_one(employee_data)

    def get_all_employees(self) -> list[dict]:
        return list(
            get_employee_collection()
            .find({}, {"_id": 0})
            .sort("created_at", -1)
        )

    def get_employee_by_employee_id(self, employee_id: str) -> dict | None:
        return get_employee_collection().find_one(
            {"employee_id": employee_id},
            {"_id": 0},
        )

    def get_employee_by_email(self, email: str) -> dict | None:
        return get_employee_collection().find_one(
            {"email": email},
            {"_id": 0},
        )

    def delete_employee_by_employee_id(self, employee_id: str) -> DeleteResult:
        return get_employee_collection().delete_one({"employee_id": employee_id})

    def count_employees(self) -> int:
        return get_employee_collection().count_documents({})

    @staticmethod
    def build_employee_document(
        employee_id: str,
        full_name: str,
        email: str,
        department: str,
    ) -> dict:
        now = datetime.utcnow()
        return {
            "employee_id": employee_id,
            "full_name": full_name,
            "email": email,
            "department": department,
            "created_at": now,
            "updated_at": now,
        }