import time
import loadJson
import keyboard

import globalVariables


def buffer_countdown():
    count = int(loadJson.read_data().get(globalVariables.buffer_timer, ""))

    while True:
        if globalVariables.buffer:
            count = count - 1

            if count <= 0:
                keys = loadJson.read_data().get(globalVariables.buffer_hotkeys, "").split(",")

                for key in keys:
                    if globalVariables.buffer:
                        keyboard.press_and_release(key)
                        time.sleep(3)

                count = int(loadJson.read_data().get(globalVariables.buffer_timer, ""))

            time.sleep(1)
        else:
            break
