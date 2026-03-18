from fastapi import APIRouter

from app.api.v1.routes.attendance_routes import router as attendance_router
from app.api.v1.routes.dashboard_routes import router as dashboard_router
from app.api.v1.routes.employee_routes import router as employee_router

api_router = APIRouter()
api_router.include_router(employee_router)
api_router.include_router(attendance_router)
api_router.include_router(dashboard_router)