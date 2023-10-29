from typing import TYPE_CHECKING

from fastapi.responses import HTMLResponse

from .controller import get_all_berries_stats, get_berries_histogram


if TYPE_CHECKING:
    from fastapi import FastAPI

def route(app: 'FastAPI'):

    @app.get("/allBerryStats")
    def all_berry_stats():
        return get_all_berries_stats()

    @app.get("/allBerreyHistogram", response_class=HTMLResponse)
    def all_berry_histogram():
        base64_hist = get_berries_histogram()
        return f'''\
        <div>
            <h3>Berries growth time</h3>
            <img src="data:image/png;base64, {base64_hist}" alt="Histogram" />
        </div>
        '''
