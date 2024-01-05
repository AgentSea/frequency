# generated by fastapi-codegen:
#   filename:  server.yaml
#   timestamp: 2024-01-05T05:18:11+00:00

from __future__ import annotations

from fastapi import APIRouter

from ..dependencies import *

router = APIRouter(tags=['Model'])


@router.post('/v1/models', response_model=V1Model, tags=['Model'])
def load_model(body: V1LoadModelRequest = None) -> V1Model:
    """
    Load a model
    """
    pass


@router.get('/v1/models', response_model=V1Models, tags=['Model'])
def get_models() -> V1Models:
    """
    A list of models
    """
    pass


@router.get('/v1/models/{name}', response_model=V1Model, tags=['Model'])
def get_model(name: str) -> V1Model:
    """
    Get a model
    """
    pass


@router.delete('/v1/models/{name}', response_model=None, tags=['Model'])
def delete_model(name: str) -> None:
    """
    Delete a model
    """
    pass


@router.post('/v1/models/{name}/chat', response_model=V1ChatResponse, tags=['Model'])
def chat_model(name: str, body: V1ChatRequest = None) -> V1ChatResponse:
    """
    Chat with a model
    """
    pass
