#!/usr/bin/python3
def class_to_json(obj):
    if isinstance(obj, dict):
        # If the object is already a dictionary, return it as is
        return obj

    if hasattr(obj, '__dict__'):
        # If the object has a '__dict__' attribute, use it to serialize
        data = obj.__dict__.copy()
        for key, value in data.items():
            data[key] = class_to_json(value)  # Recursively serialize nested objects
        return data

    if isinstance(obj, (list, tuple)):
        # If the object is a list or tuple, serialize its elements
        return [class_to_json(item) for item in obj]

    if isinstance(obj, bool) or isinstance(obj, int) or isinstance(obj, str):
        # If the object is a boolean, integer, or string, return it as is
        return obj

    # If the object is of an unsupported type, return None
    return None

# Example class
class SampleClass:
    def __init__(self, name, age, data):
        self.name = name
        self.age = age
        self.data = data

# Create an instance of the class
sample_obj = SampleClass("John", 30, [1, 2, 3])

# Serialize the object to a JSON-serializable dictionary
result = class_to_json(sample_obj)

print(result)
