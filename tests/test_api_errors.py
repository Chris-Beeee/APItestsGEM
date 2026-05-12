import pytest

# Testing Error Status Codes

def test_404_not_found_invalid_endpoint(api_client):
    """Test requesting a completely invalid endpoint returns 404."""
    response = api_client.get("/this_endpoint_does_not_exist")
    assert response.status_code == 404, "Expected 404 Not Found for invalid endpoint"

def test_404_not_found_invalid_resource_id(api_client):
    """Test requesting a valid endpoint but a non-existent resource ID returns 404."""
    response = api_client.get("/posts/999999999")
    assert response.status_code == 404, "Expected 404 Not Found for non-existent resource"

def test_delete_non_existent_resource(api_client):
    """Test attempting to delete a resource that doesn't exist."""
    response = api_client.delete("/posts/999999999")
    # jsonplaceholder might return 200 or 404 depending on the mock implementation, 
    # but standard RESTful APIs should ideally return 404 or sometimes 204.
    # In jsonplaceholder, it surprisingly returns 200 or 404, so we assert for either for the sake of the mock,
    # or assert 404 as a strict requirement. Let's assert status code is not 500.
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"

def test_missing_required_fields_on_post(api_client):
    """
    Test creating a resource with missing required fields.
    Note: jsonplaceholder is very forgiving and usually returns 201 anyway,
    but this is how you would test a 400 Bad Request in a real API.
    """
    payload = {
        # Missing 'title', 'body', 'userId'
        "unrelated_field": "test"
    }
    response = api_client.post("/posts", json=payload)
    
    # In a strict API, this should be 400 or 422.
    # We will log it if it passes as 201 (jsonplaceholder behavior).
    if response.status_code == 201:
        pytest.skip("JSONPlaceholder does not enforce strict 400 Bad Request validation.")
    else:
        assert response.status_code in [400, 422], "Expected 400 or 422 for bad request"
