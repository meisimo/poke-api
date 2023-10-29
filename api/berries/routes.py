from typing import TYPE_CHECKING

from .berry_stats import BerryStats


if TYPE_CHECKING:
    from fastapi import FastAPI

def route(app: 'FastAPI'):

    @app.get("/allBerryStats")
    async def read_all_berry_stats():
        return {}
