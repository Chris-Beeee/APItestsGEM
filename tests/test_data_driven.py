import pytest

# Data-Driven Testing using @pytest.mark.parametrize

@pytest.mark.parametrize("post_id, expected_title, expected_user_id", [
    (1, "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", 1),
    (2, "qui est esse", 1),
    (15, "eveniet quod temporibus", 2),
    (50, "repellendus qui recusandae incidunt voluptates tenetur qui omnis exercitationem", 5),
    (100, "at nam consequatur ea labore ea harum", 10),
])
def test_get_post_by_id_parametrized(api_client, post_id, expected_title, expected_user_id):
    """
    Test fetching specific posts using multiple sets of data.
    Verifies that the correct post is returned with the expected title and user ID.
    """
    response = api_client.get(f"/posts/{post_id}")
    
    assert response.status_code == 200, f"Failed to fetch post {post_id}"
    data = response.json()
    
    assert data["id"] == post_id
    assert data["title"] == expected_title
    assert data["userId"] == expected_user_id

@pytest.mark.parametrize("user_id, expected_email", [
    (1, "Sincere@april.biz"),
    (2, "Shanna@melissa.tv"),
    (3, "Nathan@yesenia.net"),
])
def test_get_users_parametrized(api_client, user_id, expected_email):
    """
    Data-driven test to verify user endpoints and ensure correct emails are returned.
    """
    response = api_client.get(f"/users/{user_id}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["id"] == user_id
    assert data["email"] == expected_email
