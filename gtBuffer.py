import time
import loadJson
import keyboard
import windowsAPI

import globalVariables


def gt_buffer_countdown():
    count = int(loadJson.read_data().get(globalVariables.gt_timer, ""))

    while True:
        if globalVariables.gt_buffer:
            count = count - 1

            print(f"GT Timer: {count}")

            if count <= 0:
                key = loadJson.read_data().get(globalVariables.gt_key, "")

                if globalVariables.gt_buffer:
                    if globalVariables.is_using_firefox:
                        windowsAPI.windows_api(key)
                    else:
                        keyboard.press_and_release(key)

                    count = int(loadJson.read_data().get(globalVariables.gt_timer, ""))

            time.sleep(1)
        else:
            break
