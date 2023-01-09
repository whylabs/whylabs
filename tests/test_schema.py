def test_schema() -> None:
    pass


# import os

# os.environ["WHYLABS_API_KEY"] = ""#

# from whylabs.helpers.schema import (
#     UpdateColumnClasses, 
#     UpdateEntityDataTypes, 
#     ColumnsClasses,
#     UpdateColumnsDiscreteness,
#     ColumnsDiscreteness
# )



# classes = ColumnsClasses(
#     inputs=[],
#     outputs=["temperature"]
# )

# update_entity = UpdateColumnClasses(
#     classes=classes,
#     dataset_id="model-7",
#     org_id="org-fjx9Rz"
# )

# update_entity.update()

# print(update_entity.current_entity_schema["columns"]["temperature"]["classifier"])

# # ----


# columns_schema = {"temperature": "bool"}

# update_data_types = UpdateEntityDataTypes(
#     dataset_id="model-7",
#     columns_schema=columns_schema,
#     org_id="org-fjx9Rz"
# )

# update_data_types.update()

# print(update_data_types.current_entity_schema["columns"]["temperature"]["dataType"])

# columns_schema = {"temperature": "fractional"}

# update_data_types = UpdateEntityDataTypes(
#     dataset_id="model-7",
#     columns_schema=columns_schema,
#     org_id="org-fjx9Rz"
# )

# update_data_types.update()

# print(update_data_types.current_entity_schema["columns"]["temperature"]["dataType"])

# # ---

# columns_discrete = ColumnsDiscreteness(
#     discrete=["temperature"],
#     continuous=[]
# )

# update_discreteness = UpdateColumnsDiscreteness(
#     dataset_id="model-7",
#     classes=columns_discrete,
#     org_id="org-fjx9Rz"
# )

# update_discreteness.update()

# print(update_discreteness.current_entity_schema["columns"]["temperature"]["discreteness"])