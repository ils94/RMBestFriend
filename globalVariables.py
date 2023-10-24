from pathlib import Path

hp_detection = False
buffer = False
gt_buffer = False

start_x = None
start_y = None
end_x = None
end_y = None

is_using_firefox = False

heal_hotkey = "heal_hotkey"
activate_hotkey_heal = "activate_hotkey_heal"
buffer_hotkeys = "buffer_hotkeys"
activate_hotkey_buffer = "activate_hotkey_buffer"
buffer_timer = "buffer_timer"
gt_key = "gt_key"
activate_hotkey_gt = "activate_hotkey_gt"
gt_timer = "gt_timer"

config_path = str(Path.home() / 'Documents') + r"/RMBestFriend/Configs/"
image_detection_path = "img/"
