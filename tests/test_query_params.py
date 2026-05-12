import pytest

# Testing Query Parameters

def test_filter_comments_by_post_id(api_client):
    """
    Test filtering comments by a specific post ID using query parameters.
    """
    post_id = 2
    response = api_client.get("/comments", params={"postId": post_id})
    assert response.status_code == 200
    
    comments = response.json()
    assert len(comments) > 0, f"Expected to find comments for postId {post_id}"
    
    # Verify that EVERY returned comment actually belongs to the requested post
    for comment in comments:
        assert comment["postId"] == post_id, f"Found comment belonging to wrong postId: {comment['postId']}"

def test_filter_posts_by_user_id(api_client):
    """
    Test filtering posts by a specific user ID.
    """
    user_id = 5
    response = api_client.get("/posts", params={"userId": user_id})
    assert response.status_code == 200
    
    posts = response.json()
    assert len(posts) > 0, f"Expected to find posts for userId {user_id}"
    
    for post in posts:
        assert post["userId"] == user_id

def test_multiple_query_parameters(api_client):
    """
    Test filtering using multiple query parameters.
    e.g. GET /comments?postId=1&id=3
    """
    params = {
        "postId": 1,
        "id": 3
    }
    response = api_client.get("/comments", params=params)
    assert response.status_code == 200
    
    comments = response.json()
    # There should only be one comment that matches both criteria
    assert len(comments) == 1, f"Expected exactly 1 comment, got {len(comments)}"
    
    comment = comments[0]
    assert comment["postId"] == params["postId"]
    assert comment["id"] == params["id"]

def test_query_parameter_no_results(api_client):
    """
    Test a query parameter that should yield no results.
    """
    response = api_client.get("/comments", params={"postId": 999999})
    assert response.status_code == 200 # It should return 200 OK with an empty array
    
    comments = response.json()
    assert isinstance(comments, list)
    assert len(comments) == 0, "Expected an empty list of comments"
