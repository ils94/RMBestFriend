import detectHPBar
import time
import keyboard
import globalVariables
import loadJson


def start_detecting():
    while True:
        try:
            if detectHPBar.is_hp_low():
                if globalVariables.hp_detection:
                    data = loadJson.read_data()
                    keyboard.press_and_release(data.get(globalVariables.heal_hotkey, ""))

                    time.sleep(1)
                else:
                    break

        except Exception as e:
            print(e)
            continue
