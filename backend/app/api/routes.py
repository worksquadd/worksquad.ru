from fastapi import APIRouter, Depends
from app.schemas.aura import AuraResponse
from app.services.aura_service import AuraService

router = APIRouter()


@router.get("/aura", response_model=AuraResponse)
def get_aura_level(
    service: AuraService = Depends(AuraService)
):
    result = service.calculate_aura()
    return AuraResponse(aura_number=result)
