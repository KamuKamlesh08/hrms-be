from fastapi import APIRouter, status

from app.core.constants import DASHBOARD_TAG, MSG_DASHBOARD_FETCHED
from app.schemas.common_schema import SuccessResponse
from app.schemas.dashboard_schema import DashboardSummaryResponse
from app.services.dashboard_service import DashboardService

router = APIRouter(prefix="/dashboard", tags=[DASHBOARD_TAG])
dashboard_service = DashboardService()


@router.get("/summary", response_model=SuccessResponse, status_code=status.HTTP_200_OK)
def get_dashboard_summary() -> SuccessResponse:
    summary = dashboard_service.get_summary()
    return SuccessResponse(
        message=MSG_DASHBOARD_FETCHED,
        data=DashboardSummaryResponse(**summary),
    )