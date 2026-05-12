import pytest
import time

# Performance/Timeout Testing

@pytest.mark.parametrize("endpoint", [
    "/posts",
    "/comments",
    "/albums",
    "/photos",
    "/todos",
    "/users"
])
def test_endpoint_performance(api_client, endpoint):
    """
    Test that the core GET endpoints respond within an acceptable timeframe (e.g., 1.5 seconds).
    This iterates through multiple endpoints to ensure the whole API is performant.
    """
    start_time = time.time()
    response = api_client.get(endpoint)
    end_time = time.time()
    
    duration = end_time - start_time
    
    assert response.status_code == 200, f"Failed to get {endpoint}"
    
    # Assert response time is less than 1.5 seconds
    max_allowed_time = 1.5
    assert duration < max_allowed_time, f"Endpoint {endpoint} took too long: {duration:.2f} seconds (Max: {max_allowed_time}s)"

def test_large_payload_performance(api_client):
    """
    Test the performance of submitting a large payload via POST.
    """
    large_text = "A" * 10000  # 10KB of text
    payload = {
        "title": "Performance Test",
        "body": large_text,
        "userId": 1
    }
    
    start_time = time.time()
    response = api_client.post("/posts", json=payload)
    end_time = time.time()
    
    duration = end_time - start_time
    assert response.status_code == 201
    
    # Assert response time is less than 2.0 seconds for a POST request
    assert duration < 2.0, f"POST request took too long: {duration:.2f} seconds"
