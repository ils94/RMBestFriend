import detectHPBar
import time
import keyboard
import globalVariables
import loadJson
import windowsAPI


def start_detecting():
    while True:
        try:
            if detectHPBar.is_hp_low():
                if globalVariables.hp_detection:
                    if not globalVariables.pause_heal:
                        key = loadJson.read_data().get(globalVariables.heal_hotkey, "")

                        if globalVariables.is_using_firefox:
                            windowsAPI.windows_api(key)
                        else:
                            keyboard.press_and_release(key)

                    time.sleep(1)
                else:
                    break

        except Exception as e:
            print(e)
            continue
