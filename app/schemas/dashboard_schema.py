from pydantic import BaseModel


class DashboardSummaryResponse(BaseModel):
    total_employees: int
    total_present_today: int
    total_absent_today: int