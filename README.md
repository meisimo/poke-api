# poke-api
Sample project that contains an API to get the statistics of the berries in pokemon


**Note:** This project should run in `python 3.11`.

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

## Run Tests

First is required to install the testing dependencies

```bash
pip install '.[test]'
```

Then to run the execution run
```bash
pytest
```
