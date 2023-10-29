# poke-api
Sample project that contains an API to get the statistics of the berries in pokemon


**Note:** This project should run in `python 3.11`.

# Endpoints 

### GET /allBerryStats

The stats of the berries growth time in json format.

### GET /allBerreyHistogram

Histogram with the berries growth time in html format.

## Execution

First is required to install the dependencies

```bash
pip install .
```

To start the application run

```bash
uvicorn api.main:app
```

## Docker execution

To execute the aplication run

```bash
docker-compose up
```

This start is configured to start by default with a `redis` cache. To turn the cache off in the docker-compose.yml, in the service `api` set the `REDIS_CACHE_ENABLED=False`.

## Run Tests

First is required to install the testing dependencies

```bash
pip install '.[test]'
```

Then to run the execution run
```bash
pytest
```
