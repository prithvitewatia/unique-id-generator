import requests


def test_next_id_generation():
    odd_ids = []
    even_ids = []

    # Simulate 10 requests
    for _ in range(10):
        response = requests.get("http://localhost/next_id")
        assert response.status_code == 200
        generated_id = int(response.json()["id"])
        if generated_id % 2 == 0:
            even_ids.append(generated_id)
        else:
            odd_ids.append(generated_id)

    # Check that both odd and even IDs were generated
    assert len(odd_ids) > 0, "Odd IDs not generated"
    assert len(even_ids) > 0, "Even IDs not generated"

    # Check that IDs are unique
    all_ids = odd_ids + even_ids
    assert len(all_ids) == len(set(all_ids)), "Duplicate IDs detected"
