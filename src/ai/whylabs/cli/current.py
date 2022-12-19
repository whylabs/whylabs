from whylabs_client.api.log_api import LogApi, LogAsyncRequest
from client import client

org_id = "org-JpsdM6"


log = LogApi(client)
request = LogAsyncRequest(dataset_timestamp=0, segment_tag=[])
log.log_async(dataset_id="model-1", log_async_request=request, org_id=org_id)
