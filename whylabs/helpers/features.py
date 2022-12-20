import os
import json
import logging
from typing import List, Dict, Optional, Any
from dataclasses import dataclass

import requests # type: ignore

from whylabs.helpers.client import client
from whylabs.helpers.config import Config

BASE_ENDPOINT = "https://api.whylabsapp.com"
os.environ["API_KEY"] = "xtzOVJVjkW.HppUlwcPgm3dedyjbD2lZga0YfAWXRqB6b6u7vnTdbJHa9CJI2Yvx"

logger = logging.getLogger(__name__)


# TODO use internal Config to authenticate to songbird
# TODO use whylabs_client to make requests to endpoints

@dataclass
class FeatureClasses:
    inputs: List[str]
    outputs: List[str]
    
    def __post_init__(self) -> None:
        if self.inputs is None:
            self.inputs = []
        if self.outputs is None:
            self.outputs = []

# TODO add modify entity schema -> discreteness
# TODO add modify entity schema -> data_type

@dataclass
class FeatureDiscreteness:
    discrete: List[str]
    continuous: List[str]


# @dataclass
# class FeatureDataType:
#     integral:
#     fractional:
#     bool:
#     string:
#     unknown:
#     null:

def _get_entity_schema(org_id: str, dataset_id: str) -> Any:
    ENTITY_SCHEMA_URL = f"v0/organizations/{org_id}/models/{dataset_id}/schema"
    req_url = os.path.join(BASE_ENDPOINT, ENTITY_SCHEMA_URL)

    entity_schema = requests.get(
        url = req_url,
        headers={
            "accept": "application/json",
            "X-API-Key": client.configuration.api_key
        }
    )
    return entity_schema.json()
    

def _put_entity_schema(org_id: str, dataset_id: str, schema: Dict) -> None:
    ENTITY_SCHEMA_URL = f"v0/organizations/{org_id}/models/{dataset_id}/schema"
    req_url = os.path.join(BASE_ENDPOINT, ENTITY_SCHEMA_URL)
    
    resp = requests.put(
        url=req_url,
        headers={
            "accept": "application/json",
            "X-API-Key": client.configuration.api_key,
            "Content-Type": "application/json"
        },
        data=json.dumps(schema)
    )
    logger.debug(f"{resp.status_code}, {resp.content}")


def change_feature_classes(dataset_id: str, classes: FeatureClasses, org_id: Optional[str] = None) -> None:
    if classes.inputs == [] and classes.outputs == []:
        logger.warning("You must define either input or output features to use this function.")
        return
    
    org_id = org_id or Config().get_default_org_id()
    
    current_entity_schema = _get_entity_schema(org_id=org_id, dataset_id=dataset_id)

    columns_dict = current_entity_schema["columns"]
    for key in columns_dict.keys():
        if key in classes.inputs and columns_dict[key]["classifier"] == "output":
            columns_dict[key].update({"classifier": "input"})
        elif key in classes.outputs and columns_dict[key]["classifier"] == "input":
            columns_dict[key].update({"classifier": "output"})
    
    metadata_dict = current_entity_schema["metadata"]
    entity_schema_dict = {"columns": columns_dict, "metadata": metadata_dict}
    _put_entity_schema(org_id=org_id, dataset_id=dataset_id, schema=entity_schema_dict)


if __name__ == "__main__":
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)
    
    change_feature_classes(
        org_id="org-fjx9Rz", 
        dataset_id="model-7", 
        classes=FeatureClasses(inputs=[], outputs=[])
    )
