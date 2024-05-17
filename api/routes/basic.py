# -*- coding: utf-8 -*-
from fastapi import APIRouter

from api.core.config import get_settings

router = APIRouter()


@router.get("/settings")
async def get_settings_endpoint():
    settings = get_settings()
    return {
        "status": "ok",
        "settings": settings.SETTING,
    }
