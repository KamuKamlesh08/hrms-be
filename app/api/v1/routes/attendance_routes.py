from fastapi import APIRouter, Query, status

from app.core.constants import ATTENDANCE_TAG, MSG_ATTENDANCE_FETCHED, MSG_ATTENDANCE_MARKED
from app.schemas.attendance_schema import AttendanceResponse, MarkAttendanceRequest
from app.schemas.common_schema import SuccessResponse
from app.services.attendance_service import AttendanceService

router = APIRouter(prefix="/attendance", tags=[ATTENDANCE_TAG])
attendance_service = AttendanceService()


@router.post("", response_model=SuccessResponse, status_code=status.HTTP_201_CREATED)
def mark_attendance(payload: MarkAttendanceRequest) -> SuccessResponse:
    attendance = attendance_service.mark_attendance(
        employee_id=payload.employee_id,
        date=payload.date,
        status=payload.status,
    )
    return SuccessResponse(message=MSG_ATTENDANCE_MARKED, data=AttendanceResponse(**attendance))


@router.get("", response_model=SuccessResponse, status_code=status.HTTP_200_OK)
def get_all_attendance(date: str | None = Query(default=None)) -> SuccessResponse:
    attendance_records = attendance_service.get_all_attendance(date=date)
    data = [AttendanceResponse(**record) for record in attendance_records]
    return SuccessResponse(message=MSG_ATTENDANCE_FETCHED, data=data)


@router.get("/{employee_id}", response_model=SuccessResponse, status_code=status.HTTP_200_OK)
def get_attendance_by_employee(employee_id: str) -> SuccessResponse:
    attendance_records = attendance_service.get_attendance_by_employee_id(employee_id)
    data = [AttendanceResponse(**record) for record in attendance_records]
    return SuccessResponse(message=MSG_ATTENDANCE_FETCHED, data=data)