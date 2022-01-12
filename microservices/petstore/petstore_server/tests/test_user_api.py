# coding: utf-8

from fastapi.testclient import TestClient


from common_models.models import User  # noqa: F401


def test_create_user(client: TestClient):
    """Test case for create_user

    Create user
    """
    body = {"first_name":"firstName","last_name":"lastName","password":"password","user_status":6,"phone":"phone","id":0,"email":"email","username":"username"}

    headers = {
    }
    response = client.request(
        "POST",
        "/user",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_users_with_array_input(client: TestClient):
    """Test case for create_users_with_array_input

    Creates list of users with given input array
    """
    body = [{"first_name":"firstName","last_name":"lastName","password":"password","user_status":6,"phone":"phone","id":0,"email":"email","username":"username"}]

    headers = {
    }
    response = client.request(
        "POST",
        "/user/createWithArray",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_users_with_list_input(client: TestClient):
    """Test case for create_users_with_list_input

    Creates list of users with given input array
    """
    body = [{"first_name":"firstName","last_name":"lastName","password":"password","user_status":6,"phone":"phone","id":0,"email":"email","username":"username"}]

    headers = {
    }
    response = client.request(
        "POST",
        "/user/createWithList",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_user(client: TestClient):
    """Test case for delete_user

    Delete user
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/user/{username}".format(username='username_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_user_by_name(client: TestClient):
    """Test case for get_user_by_name

    Get user by user name
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/user/{username}".format(username='username_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_login_user(client: TestClient):
    """Test case for login_user

    Logs user into the system
    """
    params = [("username", 'username_example'),     ("password", 'password_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/user/login",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_logout_user(client: TestClient):
    """Test case for logout_user

    Logs out current logged in user session
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/user/logout",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_user(client: TestClient):
    """Test case for update_user

    Updated user
    """
    body = {"first_name":"firstName","last_name":"lastName","password":"password","user_status":6,"phone":"phone","id":0,"email":"email","username":"username"}

    headers = {
    }
    response = client.request(
        "PUT",
        "/user/{username}".format(username='username_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

