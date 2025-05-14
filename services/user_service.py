import sys
sys.path.append('./client/user-service-client')

from openapi_client.api.login_api import LoginApi
from openapi_client.models.user_login_request import UserLoginRequest
from openapi_client.models.user_login_request_bean import UserLoginRequestBean
from openapi_client.configuration import Configuration
from openapi_client.api_client import ApiClient

configuration = Configuration(
    host="http://localhost:8020/api"  # Your server URL
)


with ApiClient(configuration) as api_client:
    api_instance = LoginApi(api_client)

    # Step 3: Create Login Request Body
    login_request = UserLoginRequest(
        user_login_request_bean=UserLoginRequestBean(
            username="usman123",
            password="P@ssw0rd!"
        ),
        channel=1,
        device_id="abcd1234xyz",
        device_type="ANDROID",
        user_id=1001,
        token="a7d1fc99-bcf5-41b2-bb15-545bf310e3b5"  # A UUID string
    )


if __name__ == '__main__':
    try:
        # Step 4: Call the API
        response = api_instance.login(login_request)
        print("Login Successful:")
        print(response)
    except Exception as e:
        print("Login Failed:")
        print(e)