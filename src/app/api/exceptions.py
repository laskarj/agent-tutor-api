from collections.abc import Awaitable, Callable

from fastapi import FastAPI, HTTPException, Request, Response
from starlette import status

from app.shared.exceptions import AppError
from app.shared.logger import get_logger
from app.shared.services.livekit.exceptions import RoomNotFoundError

logger = get_logger(__name__)


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(AppError, create_app_error_handler(status.HTTP_500_INTERNAL_SERVER_ERROR))
    app.add_exception_handler(RoomNotFoundError, create_app_error_handler(status.HTTP_404_NOT_FOUND))
    app.add_exception_handler(Exception, unknown_exception_handler)


async def unknown_exception_handler(request: Request, err: Exception) -> Response:
    logger.exception("Unknown error occurred: %s", err, extra={"error_type": type(err).__name__})
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred."
    ) from err


def create_app_error_handler(status_code: int) -> Callable[[Request, AppError], Awaitable[Response]]:
    async def app_error_handler(request: Request, err: AppError) -> Response:
        logger.error(
            "Application error occurred: %s",
            err,
            exc_info=err,
            extra={"error_type": type(err).__name__},
        )
        raise HTTPException(status_code=status_code, detail=str(err)) from err

    return app_error_handler
