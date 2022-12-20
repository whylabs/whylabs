from whylabs_client import Configuration, ApiClient
from .config import Config

# client_config.api_key = {"ApiKeyAuth":'slxFoCK7N2.eh8HOdrnlD2O5pzsm1L125iza1lRAHi4qev9UGpOgwPjUBPxdb2QT'}
def _create_client(config: Config = Config()) -> ApiClient:
    client_config = Configuration()
    client_config.host = config.get_whylabs_host()
    client_config.api_key = {"ApiKeyAuth": config.get_whylabs_api_key()}
    return ApiClient(config)


client = _create_client()
