import json
from app import app

def test_health_check():
    cliente = app.test_client()
    estados = set()
    for _ in range(5):
        respuesta = cliente.get('/health')
        assert respuesta.status_code in (200, 503)
        assert json.loads(respuesta.data)["app"] == "OK"
        estados.add(respuesta.status_code)
    assert len(estados) == 1, "El health check debe ser determinista"