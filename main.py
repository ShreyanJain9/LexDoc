
import json



def process_parameters_or_properties(data, title):
    documentation = ""
    if data:
        documentation += f"### {title}\n\n"
        for name, info in data.items():
            type_info = info.get("type", "unknown")
            description = info.get("description", "")
            type_description = process_type_info(info)
            documentation += f"**{name}**: *{type_info}*\n{type_description}\n{description}\n\n"
    return documentation


def process_type_info(type_info):
    type_name = type_info.get("type", "unknown")
    if type_name == "array":
        item_type = type_info["items"]["type"]
        if item_type == "union":
            item_type = process_union(type_info["items"]["refs"])
        return f"array of {item_type}"
    elif type_name == "union":
        return process_union(type_info["refs"])
    return type_name


def process_union(union_refs):
    return " or ".join(union_refs)


def process_definition(def_name, def_data):
    documentation = f"## {def_name}\n\n"
    if "description" in def_data:
        documentation += f"{def_data['description']}\n\n"
    if "type" in def_data:
        documentation += f"**Type**: {process_type_info(def_data)}\n\n"

    # Process input, if available (for procedures)
    input_info = def_data.get("input", {})
    if input_info:
        documentation += "### Input\n\n"
        input_encoding = input_info.get("encoding", "")
        input_schema = input_info.get("schema", {})
        documentation += f"**Encoding**: {input_encoding}\n\n"
        documentation += "#### Schema\n\n"
        documentation += process_parameters_or_properties(input_schema.get("properties", {}), "Parameters")

    # Process output, if available
    output = def_data.get("output", {}).get("schema", {})
    if output:
        documentation += "### Output\n\n"
        documentation += process_parameters_or_properties(output.get("properties", {}), "Properties")

    # Process parameters, if available
    parameters = def_data.get("parameters", {}).get("properties", {})
    documentation += process_parameters_or_properties(parameters, "Parameters")

    # Process properties, if available
    properties = def_data.get("properties", {})
    documentation += process_parameters_or_properties(properties, "Properties")

    # Process errors, if available
    errors = def_data.get("errors", [])
    if errors:
        documentation += "### Errors\n\n"
        for error_info in errors:
            error_name = error_info.get("name", "")
            error_desc = error_info.get("description", "")
            documentation += f"**{error_name}**: {error_desc}\n\n"

    return documentation


def generate_documentation(lexicon_json):
    lexicon_data = json.loads(lexicon_json)
    documentation = f"# {lexicon_data.get('id', 'Untitled Lexicon')}\n"
    # Process "main" definition if available
    main_definition = lexicon_data.get("defs", {}).get("main", {})

    # Process "main" definition if available
    if main_definition:
        documentation += process_definition("", main_definition)
    else:
        documentation += "No 'main' definition found."

    # Process definitions outside "main"
    defs = lexicon_data.get("defs", {})
    for def_name, def_data in defs.items():
        if def_name != "main":
            documentation += process_definition(def_name, def_data)

    return documentation


lexicon = '''
{
  "lexicon": 1,
  "id": "com.atproto.repo.applyWrites",
  "defs": {
    "main": {
      "type": "procedure",
      "description": "Apply a batch transaction of creates, updates, and deletes.",
      "input": {
        "encoding": "application/json",
        "schema": {
          "type": "object",
          "required": ["repo", "writes"],
          "properties": {
            "repo": {
              "type": "string",
              "format": "at-identifier",
              "description": "The handle or DID of the repo."
            },
            "validate": {
              "type": "boolean",
              "default": true,
              "description": "Validate the records?"
            },
            "writes": {
              "type": "array",
              "items": {
                "type": "union",
                "refs": ["#create", "#update", "#delete"],
                "closed": true
              }
            },
            "swapCommit": {
              "type": "string",
              "format": "cid"
            }
          }
        }
      },
      "errors": [{ "name": "InvalidSwap" }]
    },
    "create": {
      "type": "object",
      "description": "Create a new record.",
      "required": ["collection", "value"],
      "properties": {
        "collection": { "type": "string", "format": "nsid" },
        "rkey": { "type": "string", "maxLength": 15 },
        "value": { "type": "unknown" }
      }
    },
    "update": {
      "type": "object",
      "description": "Update an existing record.",
      "required": ["collection", "rkey", "value"],
      "properties": {
        "collection": { "type": "string", "format": "nsid" },
        "rkey": { "type": "string" },
        "value": { "type": "unknown" }
      }
    },
    "delete": {
      "type": "object",
      "description": "Delete an existing record.",
      "required": ["collection", "rkey"],
      "properties": {
        "collection": { "type": "string", "format": "nsid" },
        "rkey": { "type": "string" }
      }
    }
  }
}
'''

print(generate_documentation(lexicon))