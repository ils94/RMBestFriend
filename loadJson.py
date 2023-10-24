import globalVariables
import json


def read_data():
    try:
        # Read data from the JSON file
        with open(globalVariables.config_path + "keys_config.json", "r") as json_file:
            data = json.load(json_file)

        # Return the data as a dictionary
        return {
            globalVariables.heal_hotkey: data.get("heal_hotkey", ""),
            globalVariables.activate_hotkey_heal: data.get("activate_hotkey_heal", ""),
            globalVariables.buffer_hotkeys: data.get("buffer_hotkeys", ""),
            globalVariables.activate_hotkey_buffer: data.get("activate_hotkey_buffer", ""),
            globalVariables.buffer_timer: data.get("buffer_timer", ""),
            globalVariables.gt_key: data.get("gt_key", ""),
            globalVariables.activate_hotkey_gt: data.get("activate_hotkey_gt", ""),
            globalVariables.gt_timer: data.get("gt_timer", "")
        }
    except FileNotFoundError:
        # Handle the case where the JSON file doesn't exist yet
        return {}
