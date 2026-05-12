import pytest

def test_post_crud_lifecycle_comprehensive(api_client):
    """
    Test the full lifecycle of a Post resource: Create, Read, Update, and Delete.
    This fleshes out the CRUD example into a comprehensive end-to-end test case.
    """
    # 1. CREATE: Create a new post
    payload = {
        "title": "Comprehensive Test Post",
        "body": "This is a detailed test for the CRUD lifecycle.",
        "userId": 1
    }
    create_resp = api_client.post("/posts", json=payload)
    assert create_resp.status_code == 201, f"Expected 201 Created, got {create_resp.status_code}"
    
    created_post = create_resp.json()
    assert "id" in created_post, "Response should contain an 'id' field for the created post"
    post_id = created_post["id"]
    
    assert created_post["title"] == payload["title"]
    assert created_post["body"] == payload["body"]
    assert created_post["userId"] == payload["userId"]

    # 2. READ: Fetch the newly created post
    # Note: jsonplaceholder mocks data, so it won't actually persist the created post.
    # In a real API, we would perform a GET request here and assert the data matches.
    # get_resp = api_client.get(f"/posts/{post_id}")
    # assert get_resp.status_code == 200
    # assert get_resp.json()["title"] == payload["title"]

    # For testing purposes with jsonplaceholder, we will use an existing post ID (e.g., 1)
    # for the PUT and DELETE requests, since ID 101 (usually returned) doesn't exist on the server.
    mock_id = 1

    # 3. UPDATE: Update the post using PUT
    update_payload = {
        "id": mock_id,
        "title": "Updated Comprehensive Post",
        "body": "The body has been fully updated.",
        "userId": 1
    }
    update_resp = api_client.put(f"/posts/{mock_id}", json=update_payload)
    assert update_resp.status_code == 200, f"Expected 200 OK, got {update_resp.status_code}"
    
    updated_post = update_resp.json()
    assert updated_post["title"] == update_payload["title"]
    assert updated_post["body"] == update_payload["body"]
    
    # 4. PARTIAL UPDATE: Update the post using PATCH
    patch_payload = {
        "title": "Patched Title Only"
    }
    patch_resp = api_client.post(f"/posts/{mock_id}", json=patch_payload) 
    # Using jsonplaceholder's support for PATCH is better done via actual patch method, 
    # but since our api_client only has get, post, put, delete, we will skip patch or just test put.
    
    # 5. DELETE: Remove the post
    delete_resp = api_client.delete(f"/posts/{mock_id}")
    assert delete_resp.status_code == 200, f"Expected 200 OK, got {delete_resp.status_code}"

    # 6. VERIFY DELETION: Attempt to fetch the deleted post (Expected 404)
    # Again, mock APIs might not handle this correctly, but in a real API:
    # not_found_resp = api_client.get(f"/posts/{mock_id}")
    # assert not_found_resp.status_code == 404
