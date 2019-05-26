DEFAULT_SCHEMA = {
    "type": "object",
    "properties": {
        "sheets": {
            "type": "array",
            "items": {
                "allOf": [
                    {
                        "type": "object",
                        "properties": {
                            "key": {"type": "string"},
                            "name": {"type": "string"},
                            "args": {
                                "type": "array",
                                "items": {
                                    "oneOf": [
                                        {"type": "string"},
                                        {"type": "integer"}
                                    ]
                                }
                            },
                            "columns": {
                                "type": "array",
                                "items": {
                                    "allOf": [
                                        {
                                            "type": "object",
                                            "properties": {
                                                "name": {"type": "string"},
                                                "width": {"type": "integer"},
                                                "args": {
                                                    "type": "array",
                                                    "items": {
                                                        "oneOf": [
                                                            {"type": "string"},
                                                            {"type": "integer"}
                                                        ]
                                                    }
                                                },
                                                "rows": {
                                                    "type": "array",
                                                    "items": {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "width": {
                                                                        "type": "integer"},
                                                                    "data": {
                                                                        "type": "string"},
                                                                    "args": {
                                                                        "type": "array"}
                                                                },
                                                                "required": [
                                                                    'data']
                                                            }
                                                        ]
                                                    }
                                                },
                                            },
                                            "required": ["rows"]
                                        }
                                    ]
                                }
                            }
                        }
                    }
                ]
            },
            "required": ["key", "columns"]
        },
        "styles": {
            "type": "array",
            "items": {
                "allOf": [{
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "style": {
                            "type": "object",
                            "additionalProperties": True
                        }
                    },
                    "required": ["name", "style"]
                }]
            }
        }
    },
    "required": ["sheets"]
}
