from typing import Annotated, Any
from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from app.serivce import json_web_parser, JSONWebParser

router = APIRouter()


@router.post("/")
async def parse_json(
    json_string: Annotated[str, Form(alias="json_string")],
    serializer: Annotated[JSONWebParser, Depends(json_web_parser)],
):
    return JSONResponse(await serializer.parse_json_recursive(json_string))
