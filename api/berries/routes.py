from typing import TYPE_CHECKING

from .controller import get_all_berries_stats


if TYPE_CHECKING:
    from fastapi import FastAPI

def route(app: 'FastAPI'):

    @app.get("/allBerryStats")
    async def all_berry_stats():
        return get_all_berries_stats()
