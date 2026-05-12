import pytest

# Validating Response Schema

def test_todos_response_schema(api_client):
    """
    Test that the `/todos` endpoint returns a list of objects 
    matching the expected schema exactly.
    """
    response = api_client.get("/todos")
    assert response.status_code == 200
    
    todos = response.json()
    assert isinstance(todos, list), "Expected a list of todos"
    assert len(todos) > 0, "Expected at least one todo in the response"
    
    expected_keys = {"userId", "id", "title", "completed"}
    
    for todo in todos[:10]: # Validate the first 10 items to save time
        assert set(todo.keys()) == expected_keys, f"Keys do not match for todo {todo['id']}"
        assert isinstance(todo["userId"], int)
        assert isinstance(todo["id"], int)
        assert isinstance(todo["title"], str)
        assert isinstance(todo["completed"], bool)

def test_user_nested_schema(api_client):
    """
    Test a more complex nested schema from the `/users` endpoint.
    """
    response = api_client.get("/users/1")
    assert response.status_code == 200
    
    user = response.json()
    
    # Validate top-level keys
    assert "name" in user
    assert "email" in user
    assert "address" in user
    assert "company" in user
    
    # Validate nested 'address' schema
    address = user["address"]
    assert isinstance(address, dict)
    assert "street" in address
    assert "suite" in address
    assert "city" in address
    assert "zipcode" in address
    assert "geo" in address
    
    # Validate nested 'geo' schema inside 'address'
    geo = address["geo"]
    assert isinstance(geo, dict)
    assert "lat" in geo
    assert "lng" in geo
    
    # Validate types of geo coordinates (often strings in this specific mock API)
    assert isinstance(geo["lat"], str)
    assert isinstance(geo["lng"], str)
