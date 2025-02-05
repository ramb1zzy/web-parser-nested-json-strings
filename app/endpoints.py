from typing import Annotated, Any

from fastapi import APIRouter, Depends, Form

router = APIRouter()

@router.post("/")
async def receive_json(decode_json: Annotated[Any, Depends(Form)]):
    pass