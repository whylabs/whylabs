# from whylabs_client.api.
from typing import Optional, Union
from datetime import datetime
from .client import client
from .config import Config
from whylabs_client.api.dataset_profile_api import DatasetProfileApi, DeleteDatasetProfilesResponse 

date_or_millis = Union[datetime, int]


def delete_all_profiles_for_period(
    start: date_or_millis,
    end: date_or_millis,
    dataset_id: str,
    org_id: Optional[str],
) -> None:
    id = org_id or Config().get_default_org_id()
    api = DatasetProfileApi(client)

    profile_start_timestamp = start if isinstance(start, int) else int(start.timestamp() * 1000.0)
    profile_end_timestamp = end if isinstance(end, int) else int(end.timestamp() * 1000.0)

    result: DeleteDatasetProfilesResponse = api.delete_dataset_profiles(
        org_id=id,
        dataset_id=dataset_id,
        profile_start_timestamp=profile_start_timestamp,
        profile_end_timestamp=profile_end_timestamp,
    )

    print(result)

    return None
