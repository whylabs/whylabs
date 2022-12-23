import time
import whylabs_client
from whylabs_client.api import models_api
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = whylabs_client.Configuration(host="https://api.whylabsapp.com")

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key["ApiKeyAuth"] = ""

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with whylabs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = models_api.ModelsApi(api_client)
    dataset_id = "model-7"
    org_id = "org-fjx9Rz"
    include_entity_schema = True  # bool, none_type |  (optional)
    include_entity_weights = True  # bool, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the monitor config document for a given dataset.
        api_response = api_instance.get_monitor_config_v3(org_id, dataset_id)
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->get_monitor_config_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the monitor config document for a given dataset.
        api_response = api_instance.get_monitor_config_v3(
            org_id,
            dataset_id,
            include_entity_schema=include_entity_schema,
            include_entity_weights=include_entity_weights,
        )
        pprint(api_response)
    except whylabs_client.ApiException as e:
        print("Exception when calling ModelsApi->get_monitor_config_v3: %s\n" % e)
