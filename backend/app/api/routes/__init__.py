from app.api.routes.hedgehogs import router as hedgehogs_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(hedgehogs_router, prefix="/hedgehogs", tags=["hedgehogs"])
