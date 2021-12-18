import json
import jsonschema

class ValidateItems:
    @staticmethod
    def validate_items(items_dict: dict, path_to_schema: str):
        res_set = {True}
        for item in items_dict:
            res_set.add(jsonschema.validate(item, path_to_schema))
        return res_set