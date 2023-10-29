import json
import os

from requests import Response
from fastapi.testclient import TestClient

from api.berries import services
from api.main import app

file_path = os.path.dirname(os.path.abspath(__file__))
test_resources = os.path.join(file_path, '..', 'resources')

client = TestClient(app)

def build_response(body: dict, status: int = 200) -> Response:
    response = Response()
    response.status_code = status
    response._content = json.dumps(body)  # pylint: disable=protected-access
    response.json = lambda: body
    return response

def mock_request(mocker, monkeypatch):
    def mock_requests(url: str, *_, **kwargs):
        params = kwargs.get('params', {})

        if url.endswith('/berry/'):
            print(url, params)
            if params.get('offset', 0) == 0:
                mock_filename = 'berries_page_1.json'
            else:
                mock_filename = 'berries_page_2.json'
        else:
            _id = url.split('/')[-2]
            mock_filename = f'berry_detail_{_id}.json'

        with open(os.path.join(test_resources, mock_filename), encoding='utf8') as f:
            return build_response(json.load(f))

    mocker.patch(
        'requests.get',
        mock_requests
    )
    monkeypatch.setattr(services, 'BERRIES_PER_PAGE_LIMIT', 5)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_all_berry_stats(mocker, monkeypatch):
    mock_request(mocker, monkeypatch)

    response = client.get("/allBerryStats")
    assert response.status_code == 200

    assert response.json() == {
        'berries_names': [
            'chople',
            'kebia',
            'shuca',
            'coba',
            'payapa',
            'micle',
            'custap',
            'jaboca'
        ],
        'min_growth_time': 18,
        'max_growth_time': 24,
        'median_growth_time': 18.0,
        'variance_growth_time': 9.642857142857142,
        'mean_growth_time': 20.25,
        'frequency_growth_time': {
            '18': 5,
            '24': 3,
        }
    }
