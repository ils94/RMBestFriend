import time
import loadJson
import keyboard

import globalVariables


def gt_buffer_countdown():
    count = int(loadJson.read_data().get(globalVariables.gt_timer, ""))

    while True:
        if globalVariables.gt_buffer:
            count = count - 1

            if count <= 0:
                key = loadJson.read_data().get(globalVariables.gt_key, "")

                if globalVariables.gt_buffer:
                    keyboard.press_and_release(key)

                    count = int(loadJson.read_data().get(globalVariables.gt_timer, ""))

                else:
                    break

            time.sleep(1)
        else:
            break
