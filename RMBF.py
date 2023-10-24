import tkinter as tk
from tkinter import Menu, messagebox, ttk

import keyboard

import json
import loadJson
import globalVariables
import screenCoordinatesFiles
import startThreads
import detectLowHPLoop
import buffer
import gtBuffer

rect_color = "#ffcccb"


def validate_input_buffer_timer(char):
    if char.isdigit():
        return True
    else:
        return False


def activate_deactivate_hp_detection():
    if globalVariables.hp_detection:
        globalVariables.hp_detection = False
    else:
        globalVariables.hp_detection = True

        startThreads.start_thread(lambda: detectLowHPLoop.start_detecting())


def activate_deactivate_buffer():
    if globalVariables.buffer:
        globalVariables.buffer = False
    else:
        globalVariables.buffer = True

        startThreads.start_thread(lambda: buffer.buffer_countdown())


def activate_deactivate_gt_buffer():
    if globalVariables.gt_buffer:
        globalVariables.gt_buffer = False
    else:
        globalVariables.gt_buffer = True

        startThreads.start_thread(lambda: gtBuffer.gt_buffer_countdown())


def center_window(window, min_width, min_height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates for centering
    x = (screen_width - min_width) // 2
    y = (screen_height - min_height) // 2

    # Set the window's geometry to center it on the screen
    window.geometry(f"{min_width}x{min_height}+{x}+{y}")


def keys_setup_window():
    def save_data():
        # Get data from Entry widgets
        heal_hotkey = entry1.get()
        activate_hotkey_heal = entry2.get()
        buffer_hotkeys = entry3.get()
        activate_hotkey_buffer = entry4.get()
        buffer_timer = entry5.get()
        gt_key = entry6.get()
        activate_hotkey_gt = entry7.get()
        gt_timer = entry8.get()

        # Create a dictionary with the data
        data = {
            globalVariables.heal_hotkey: heal_hotkey,
            globalVariables.activate_hotkey_heal: activate_hotkey_heal,
            globalVariables.buffer_hotkeys: buffer_hotkeys,
            globalVariables.activate_hotkey_buffer: activate_hotkey_buffer,
            globalVariables.buffer_timer: buffer_timer,
            globalVariables.gt_key: gt_key,
            globalVariables.activate_hotkey_gt: activate_hotkey_gt,
            globalVariables.gt_timer: gt_timer
        }

        try:
            keyboard.unhook_all()

            keyboard.register_hotkey(activate_hotkey_heal, activate_deactivate_hp_detection)
            keyboard.register_hotkey(activate_hotkey_buffer, activate_deactivate_buffer)
            keyboard.register_hotkey(activate_hotkey_gt, activate_deactivate_gt_buffer)

        except Exception as e:
            messagebox.showerror("Error", str(e))

        # Write the data to a JSON file
        with open(globalVariables.config_path + "keys_config.json", "w") as json_file:
            json.dump(data, json_file)

    def checkbox_state():
        if checkbox_var.get() == 1:
            globalVariables.is_using_firefox = True
        else:
            globalVariables.is_using_firefox = False

        print(globalVariables.is_using_firefox)

    top_level = tk.Toplevel(root)  # Create a new top-level window

    # Add widgets and configure the new top-level window as needed

    x = 250
    y = 570

    top_level.title("Keys setup")
    top_level.geometry(f"{x}x{y}")
    top_level.attributes("-topmost", True)

    # Create a horizontal separator
    separator = ttk.Separator(top_level, orient='horizontal')

    validation_timers = top_level.register(validate_input_buffer_timer)

    # Create a variable to store the checkbox state
    checkbox_var = tk.IntVar()

    frame_checkbutton = tk.Frame(top_level)
    frame_checkbutton.pack(fill=tk.BOTH)

    # Create a checkbox widget
    checkbox = tk.Checkbutton(frame_checkbutton, text="Is playing on Firefox?", variable=checkbox_var, command=checkbox_state)
    checkbox.pack(side=tk.LEFT)

    separator.pack(fill='x', pady=5)

    # Create Entry widgets for input
    label1 = tk.Label(top_level, text="Heal Hotkey")
    entry1 = tk.Entry(top_level)
    label1.pack(fill=tk.BOTH, padx=5, pady=5)
    entry1.pack(fill=tk.BOTH, padx=5, pady=5)

    label2 = tk.Label(top_level, text="Activate/Deactivate Hotkey")
    label2.pack(fill=tk.BOTH, padx=5, pady=5)
    entry2 = tk.Entry(top_level)
    entry2.pack(fill=tk.BOTH, padx=5, pady=5)

    label3 = tk.Label(top_level, text="Buffer Hotkey(s)")
    label3.pack(fill=tk.BOTH, padx=5, pady=5)
    entry3 = tk.Entry(top_level)
    entry3.pack(fill=tk.BOTH, padx=5, pady=5)

    label4 = tk.Label(top_level, text="Key to Activate/Deactivate Buffer")
    label4.pack(fill=tk.BOTH, padx=5, pady=5)
    entry4 = tk.Entry(top_level)
    entry4.pack(fill=tk.BOTH, padx=5, pady=5)

    label5 = tk.Label(top_level, text="Buffer Timer (in seconds)")
    label5.pack(fill=tk.BOTH, padx=5, pady=5)
    entry5 = tk.Entry(top_level)
    entry5.config(validate="key")
    entry5.config(validatecommand=(validation_timers, "%S"))
    entry5.pack(fill=tk.BOTH, padx=5, pady=5)

    label6 = tk.Label(top_level, text="GT Key")
    label6.pack(fill=tk.BOTH, padx=5, pady=5)
    entry6 = tk.Entry(top_level)
    entry6.pack(fill=tk.BOTH, padx=5, pady=5)

    label7 = tk.Label(top_level, text="Key to Activate/Deactivate GT Buffer")
    label7.pack(fill=tk.BOTH, padx=5, pady=5)
    entry7 = tk.Entry(top_level)
    entry7.pack(fill=tk.BOTH, padx=5, pady=5)

    label8 = tk.Label(top_level, text="GT Timer (in seconds)")
    label8.pack(fill=tk.BOTH, padx=5, pady=5)
    entry8 = tk.Entry(top_level)
    entry8.config(validate="key")
    entry8.config(validatecommand=(validation_timers, "%S"))
    entry8.pack(fill=tk.BOTH, padx=5, pady=5)

    frame = tk.Frame(top_level)
    frame.pack(fill=tk.BOTH)

    # Define a bold font
    bold_font = ("Arial", 10, "bold")

    # Create a button to save data
    button = tk.Button(frame, text="Save", width=10, height=2, font=bold_font, command=save_data)
    button.pack(side=tk.LEFT, padx=5, pady=5)

    data = loadJson.read_data()

    # Display the data in Entry widgets
    entry1.delete(0, tk.END)
    entry1.insert(0, data.get(globalVariables.heal_hotkey, ""))
    entry2.delete(0, tk.END)
    entry2.insert(0, data.get(globalVariables.activate_hotkey_heal, ""))
    entry3.delete(0, tk.END)
    entry3.insert(0, data.get(globalVariables.buffer_hotkeys, ""))
    entry4.delete(0, tk.END)
    entry4.insert(0, data.get(globalVariables.activate_hotkey_buffer, ""))
    entry5.delete(0, tk.END)
    entry5.insert(0, data.get(globalVariables.buffer_timer, ""))
    entry6.delete(0, tk.END)
    entry6.insert(0, data.get(globalVariables.gt_key, ""))
    entry7.delete(0, tk.END)
    entry7.insert(0, data.get(globalVariables.activate_hotkey_gt, ""))
    entry8.delete(0, tk.END)
    entry8.insert(0, data.get(globalVariables.gt_timer, ""))

    if globalVariables.is_using_firefox:
        checkbox_var.set(1)
    else:
        checkbox_var.set(0)

    # Center the window on the screen with a minimum size
    center_window(top_level, x, y)  # Adjust the minimum size as needed


def on_press(event):
    global rect

    if event.state & 0x4:
        globalVariables.start_x = canvas.canvasx(event.x)
        globalVariables.start_y = canvas.canvasy(event.y)

        if rect:
            canvas.delete(rect)
        rect = None


def on_drag(event):
    global rect

    cur_x = canvas.canvasx(event.x)
    cur_y = canvas.canvasy(event.y)

    if event.state & 0x4:
        if rect:
            canvas.coords(rect, globalVariables.start_x,
                          globalVariables.start_y,
                          cur_x,
                          cur_y)
        else:
            rect = canvas.create_rectangle(globalVariables.start_x,
                                           globalVariables.start_y,
                                           cur_x,
                                           cur_y,
                                           fill=rect_color)


def on_release(event):
    if event.state & 0x4:
        globalVariables.end_x = canvas.canvasx(event.x)
        globalVariables.end_y = canvas.canvasy(event.y)

        screenCoordinatesFiles.save_coordinates(globalVariables.start_x,
                                                globalVariables.start_y,
                                                globalVariables.end_x,
                                                globalVariables.end_y)


root = tk.Tk()
root.title("RM Best Friend")
root.attributes("-alpha", 0.5)
root.attributes("-topmost", True)
root.state("zoomed")

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Keys setup", command=keys_setup_window)
canvas = tk.Canvas(root, cursor="cross")
canvas.pack(fill=tk.BOTH, expand=True)

rect = None

(globalVariables.start_x,
 globalVariables.start_y,
 globalVariables.end_x,
 globalVariables.end_y) = screenCoordinatesFiles.load_coordinates()

canvas.bind("<ButtonPress-1>", on_press)
canvas.bind("<B1-Motion>", on_drag)
canvas.bind("<ButtonRelease-1>", on_release)

if globalVariables.start_x:
    rect = canvas.create_rectangle(globalVariables.start_x,
                                   globalVariables.start_y,
                                   globalVariables.end_x,
                                   globalVariables.end_y,
                                   fill=rect_color)

root.mainloop()
