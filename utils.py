# Utility function to optimize JSON dictionary

def json_optimizer_combined(aml_dict: dict, clean: bool, abbreviate: int):
    from abbreviations import name_abbreviations, num_abbreviations

    def process_value(value):
        if isinstance(value, dict):
            new_dict = json_optimizer_combined(value, clean, abbreviate)
            return new_dict if new_dict or not clean else None
        elif isinstance(value, list):
            new_list = [process_value(entry) for entry in value if not (clean and is_empty(entry))]
            return new_list if new_list or not clean else None
        else:
            return value

    def is_empty(val):
        if clean:
            return val is None or val == "" or val == "Null" or val == "None" or val == 0
        else: 
            return False

    def get_abbreviation(key):
        if abbreviate == 1:
            return name_abbreviations.get(key, key)
        elif abbreviate == 2:
            return num_abbreviations.get(key, key)
        return key

    new_dict = {}
    for key, value in aml_dict.items():
        if not is_empty(value):
            new_key = get_abbreviation(key)
            processed_value = process_value(value)
            if not is_empty(processed_value):
                new_dict[new_key] = processed_value

    return new_dict



def json_optimizer(aml_dict: dict):
    for key, value in aml_dict.copy().items():
        if value is None or value == "" or value == "Null" or value == "None":
            del aml_dict[key]
        elif isinstance(value, list):
            if value:
                new_value_list = []
                for entry in value:
                    if isinstance(entry, str):
                        pass
                    elif isinstance(entry, dict):
                        new_value_list.append(json_optimizer(entry))
            else:
                del aml_dict[key]
        elif isinstance(value, dict):
            value = json_optimizer(value)
    return aml_dict

def parser_definition(indent_value = None):
    from xsdata.formats.dataclass.context import XmlContext
    from xsdata.formats.dataclass.parsers import XmlParser, JsonParser
    from xsdata.formats.dataclass.serializers import XmlSerializer, JsonSerializer
    from xsdata.formats.dataclass.serializers.config import SerializerConfig

    # Create XML context, parser, and serializer
    context = XmlContext()
    parser = XmlParser(context=context)
    json_parser = JsonParser(context=context)
    xml_serializer = XmlSerializer(context=context)
    config = SerializerConfig(pretty_print=False, ignore_default_attributes=True)
    json_serializer = JsonSerializer(context=XmlContext(), config=config, indent=indent_value)
    return context, parser, json_parser, xml_serializer, json_serializer

