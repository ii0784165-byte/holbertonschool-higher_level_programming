#!/usr/bin/env python3
"""CSV to JSON conversion module"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON file named data.json

    Args:
        csv_filename (str): Input CSV filename

    Returns:
        bool: True if successful, False on error
    """
    try:
        data_list = []
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(row)

        with open("data.json", "w", encoding='utf-8') as jsonfile:
            json.dump(data_list, jsonfile, indent=4)
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
