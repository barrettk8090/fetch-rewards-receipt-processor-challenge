from jsonschema import validate, ValidationError

# Define the required JSON schema for the receipt based on the YAML file provided
receipt_schema = {
    "type": "object",
    "required": ["retailer", "purchaseDate", "purchaseTime", "items", "total"],
    "properties": {
        "retailer": {"type": "string", "pattern": "^[\\w\\s\\-&]+$"},
        "purchaseDate": {"type": "string", "format": "date"},
        "purchaseTime": {"type": "string", "format": "time"},
        "items": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": ["shortDescription", "price"],
                "properties": {
                    "shortDescription": {"type": "string", "pattern": "^[\\w\\s\\-]+$"},
                    "price": {"type": "string", "pattern": "^\\d+\\.\\d{2}$"}
                }
            }
        },
        "total": {"type": "string", "pattern": "^\\d+\\.\\d{2}$"}
    }
}