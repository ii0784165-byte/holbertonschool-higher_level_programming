#!/usr/bin/env python3
"""Module for serializing and deserializing Python dictionaries to/from XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): Python dictionary to serialize
        filename (str): Output XML filename

    Returns:
        bool: True if successful, False on error
    """
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): Input XML filename

    Returns:
        dict: Python dictionary with deserialized data
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text
        return result
    except Exception:
        return {}
