from fastapi import APIRouter

main_router = APIRouter(prefix="/api")


@main_router.get("/status")
def get_status():
    return {"status": "ok"}
