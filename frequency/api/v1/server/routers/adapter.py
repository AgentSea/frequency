# generated by fastapi-codegen:
#   filename:  server.yaml
#   timestamp: 2024-01-13T18:24:37+00:00

from __future__ import annotations

from fastapi import APIRouter

from ..dependencies import *

router = APIRouter(tags=['Adapter'])


@router.post('/v1/adapters', response_model=V1Adapter, tags=['Adapter'])
def load_adapter(body: V1Adapter = None) -> V1Adapter:
    """
    Load an adapter
    """
    pass


@router.get('/v1/adapters', response_model=V1Adapters, tags=['Adapter'])
def get_adapters() -> V1Adapters:
    """
    A list of adapters
    """
    pass


@router.get('/v1/adapters/{name}', response_model=V1Adapter, tags=['Adapter'])
def get_adapter(name: str) -> V1Adapter:
    """
    Get an adapter
    """
    pass


@router.delete('/v1/adapters/{name}', response_model=None, tags=['Adapter'])
def delete_adapter(name: str) -> None:
    """
    Delete an adapter
    """
    pass
