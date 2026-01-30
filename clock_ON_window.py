import tkinter as tk
from time import strftime

# ---- Main Window ----
root = tk.Tk()
root.title("Digital Clock Widget")

# Remove title bar and keep always on top
root.overrideredirect(True)          # No title bar
root.attributes("-topmost", True)    # Always on top
root.config(bg="black")              # Background color

# ---- Function to update time ----
def update_time():
    string = strftime('%I:%M:%S %p\n%D')
    label.config(text=string)
    label.after(1000, update_time)

# ---- Function to move window by dragging ----
def move_window(event):
    root.geometry(f"+{event.x_root}+{event.y_root}")

# ---- Clock Label ----
label = tk.Label(
    root,
    font=("Calibri", 50, "bold"),
    background="black",
    foreground="lime"  # green digital color
)
label.pack()

# ---- Bind drag, esc, and right-click exit ----
label.bind("<B1-Motion>", move_window)          # Drag with left mouse
root.bind("<Escape>", lambda e: root.destroy()) # Press Esc to exit
label.bind("<Button-3>", lambda e: root.destroy()) # Right-click to exit

# ---- Start clock ----
update_time()
root.mainloop()
