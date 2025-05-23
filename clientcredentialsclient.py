import requests
import time

class ClientCredentialsClient:
    def __init__(self, token_url, client_id, client_secret, scope=None):
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self._token = None
        self._token_expiry = 0

    def _fetch_token(self):
        data = {
            "grant_type": "client_credentials"
        }
        if self.scope:
            data["scope"] = self.scope

        response = requests.post(
            self.token_url,
            data=data,
            auth=(self.client_id, self.client_secret),
            timeout=10
        )
        response.raise_for_status()

        token_data = response.json()
        self._token = token_data["access_token"]
        self._token_expiry = time.time() + token_data.get("expires_in", 3600) - 60  # buffer before expiry

    def get_token(self):
        if not self._token or time.time() >= self._token_expiry:
            self._fetch_token()
        return self._token

    def get(self, url, **kwargs):
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {self.get_token()}"
        return requests.get(url, headers=headers, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {self.get_token()}"
        return requests.post(url, data=data, json=json, headers=headers, **kwargs)
