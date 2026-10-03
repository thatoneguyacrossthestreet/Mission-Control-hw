import tkinter as tk
from tkinter import messagebox
from datetime import datetime

window = tk.Tk()

launch_timer = None

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

def show_about():
    messagebox.showinfo(
        "About Mission Control",
        "MISSION CONTROL\nVersion 1.0"
    )

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=window.destroy)
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)

window.title("MISSION CONTROL")

label = tk.Label(
    window,
    text="MISSION CONTROL",
    font=("Arial", 20)
)
label.pack()

label2 = tk.Label(window, text="SYSTEM STATUS: STANDBY")
label2.pack(pady=10)

mission_label = tk.Label(window, text="Mission Name:")
mission_label.pack()

mission_name = tk.Entry(window, width=30)
mission_name.pack(pady=10)

def button_clicked():

    global launch_timer

    name = mission_name.get()

    label2.config(text="SYSTEMS CHECK")
    status_message.config(text="Running pre-launch diagnostics")

    launch_timer = window.after(3000, phase_two)

def phase_two():

    global launch_timer

    label2.config(text="PHASING ROCKET")
    status_message.config(text="Rocket phasing")

    launch_timer = window.after(5000, phase_three)

def phase_three():

    label2.config(text="ROCKET IN ORBIT")
    status_message.config(text="Mission active")

def abort_clicked():
    window.after_cancel(launch_timer)
    label2.config(text="LAUNCH ABORTED")
    status_message.config(text="Launch aborted")

button = tk.Button(window, text="LAUNCH", command=button_clicked)
button.pack(pady=5)

abort_button = tk.Button(
    window,
    text="ABORT",
    command=abort_clicked
)
abort_button.pack(pady=5)

status_bar = tk.Frame(
    window,
    relief=tk.SUNKEN,
    borderwidth=1
)

status_bar.pack(
    side=tk.BOTTOM,
    fill=tk.X
)

status_message = tk.Label(
    status_bar,
    text="Ready"
)

status_message.pack(
    side=tk.LEFT,
    padx=5
)

clock_label = tk.Label(
    status_bar,
    text=""
)

clock_label.pack(
    side=tk.RIGHT,
    padx=5
)

def update_clock():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    window.after(1000, update_clock)

update_clock()

window.mainloop()