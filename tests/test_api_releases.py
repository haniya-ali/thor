import pytest
# print('reached here')
import json
# print('reached here too')
from fastapi.testclient import TestClient
# print('reached here as well')
from main import app
print('didnt reach here')

client = TestClient(app)

expected_output_for_get_releases = {
  "releases": [
    {
      "version": "2021.09",
      "result": "In Progress",
      "release_id": 3
    },
    {
      "version": "2021.07",
      "result": "Completed",
      "release_id": 4
    }
  ]
}

def test_read_releases():
    response = client.get("/releases")
    assert response.status_code == 200
    assert response.json() == expected_output_for_get_releases

@pytest.mark.parametrize("release_id", [3, 4])
def test_read_single_release(release_id):
    response = client.get(f"/releases/{release_id}")
    assert response.status_code == 200
    if release_id == 3:
      # convert py dictionary to json string
      release3_payload = json.dumps(expected_output_for_get_releases['releases'][0])
      expected_output_for_get_release = f"{{ \"release\": {release3_payload} }}"
    elif release_id == 4:
      release4_payload = json.dumps(expected_output_for_get_releases['releases'][1])
      expected_output_for_get_release = f"{{ \"release\": {release4_payload} }}"
    # convert json string back to json object for comparison
    assert response.json() == json.loads(expected_output_for_get_release)


# def test_read_tasks():
#     response = client.get("/tasks")
#     assert response.status_code == 200
#     assert response.json() == expected_output_for_get_tasks

# @pytest.mark.parametrize("release_id", [8, 9, 10])
# TODO: might need to add a release_id paramter
# def test_read_single_task(task_id):
#     response = client.get(f"/releases/{release_id}/tasks/{task_id}")
#     assert response.status_code == 200
#     if task_id == 8:
#       # convert py dictionary to json string
#       task8_payload = json.dumps(expected_output_for_get_tasks['tasks'][0])
#       expected_output_for_get_task = f"{{ \"tasks\": {task8_payload} }}"
#     elif task_id == 9:
#       task9_payload = json.dumps(expected_output_for_get_tasks['tasks'][1])
#       expected_output_for_get_task = f"{{ \"tasks\": {task9_payload} }}"
#     elif task_id == 10:
#       task10_payload = json.dumps(expected_output_for_get_tasks['tasks'][2])
#       expected_output_for_get_task = f"{{ \"tasks\": {task10_payload} }}"
#     assert response.json() == json.loads(expected_output_for_get_task)

