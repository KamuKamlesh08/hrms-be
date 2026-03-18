from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.v1.api_router import api_router
from app.core.config import get_settings
from app.core.constants import API_HEALTH_TAG, MSG_HEALTH_OK
from app.core.exceptions import AppException
from app.core.logger import configure_logging, get_logger
from app.middleware.logging_middleware import LoggingMiddleware
from app.schemas.error_schema import ErrorResponse
from app.schemas.common_schema import SuccessResponse
from app.startup import on_shutdown, on_startup

configure_logging()
logger = get_logger(__name__)
settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI):
    on_startup()
    yield
    on_shutdown()


app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(LoggingMiddleware)


@app.exception_handler(AppException)
async def app_exception_handler(_: Request, exc: AppException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            message=exc.message,
            details=exc.details or None,
        ).model_dump(),
    )


@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(_: Request, exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=ErrorResponse(
            message="Request validation failed.",
            details=exc.errors(),
        ).model_dump(),
    )


@app.exception_handler(Exception)
async def generic_exception_handler(_: Request, exc: Exception) -> JSONResponse:
    logger.exception("Unhandled exception occurred: %s", str(exc))
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ErrorResponse(
            message="Internal server error.",
            details=None,
        ).model_dump(),
    )


@app.get("/health", response_model=SuccessResponse, tags=[API_HEALTH_TAG])
def health_check() -> SuccessResponse:
    return SuccessResponse(message=MSG_HEALTH_OK, data={"status": "UP"})


app.include_router(api_router, prefix=settings.api_v1_prefix)