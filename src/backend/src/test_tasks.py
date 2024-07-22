from fastapi.testclient import TestClient

from ADVSgdhmain import app


client = TestClient(app)

def test_get_all_tasks():
	response = client.get("/tasks")
	print('response', response)
	assert response.status_code == 200

