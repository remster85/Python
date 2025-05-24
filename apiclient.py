from .client_credentials import ClientCredentialsClient

class ApiClient:
    BASE_URL = "https://api.system.com"

    def __init__(self, token_url, client_id, client_secret, scope=None):
        self.auth_client = ClientCredentialsClient(
            token_url=token_url,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope
        )

    def get_resource(self, params=None):
        url = f"{self.BASE_URL}/resource"
        query = {
            "parameter": "value"
        }
        if params:
            query.update(params)
        response = self.auth_client.get(url, params=query)
        response.raise_for_status()
        return response.json()
