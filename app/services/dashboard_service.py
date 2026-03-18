from datetime import datetime

from app.core.constants import DATE_FORMAT
from app.repositories.attendance_repository import AttendanceRepository
from app.repositories.employee_repository import EmployeeRepository


class DashboardService:
    def __init__(self) -> None:
        self.employee_repository = EmployeeRepository()
        self.attendance_repository = AttendanceRepository()

    def get_summary(self) -> dict:
        today = datetime.utcnow().strftime(DATE_FORMAT)

        return {
            "total_employees": self.employee_repository.count_employees(),
            "total_present_today": self.attendance_repository.count_present_for_date(today),
            "total_absent_today": self.attendance_repository.count_absent_for_date(today),
        }