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

            if count <= 0:
                key = loadJson.read_data().get(globalVariables.gt_key, "")

                globalVariables.pause_heal = True

                if globalVariables.gt_buffer:
                    if globalVariables.is_using_firefox:
                        windowsAPI.windows_api(key)
                    else:
                        keyboard.press_and_release(key)

                    count = int(loadJson.read_data().get(globalVariables.gt_timer, ""))

                    globalVariables.pause_heal = False

            time.sleep(1)
        else:
            globalVariables.pause_heal = False
            break
