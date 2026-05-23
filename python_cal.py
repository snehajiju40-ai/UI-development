import tkinter as tk

# =========================
# MAIN WINDOW
# =========================

window = tk.Tk()

window.title("Professional Calculator")

window.geometry("360x520")

window.configure(bg="#1E1E1E") #Eerie Black for background

window.resizable(True, True) # Allow window resizing, 
# with 2 arguments represent:window width and height

# =========================
# ENTRY DISPLAY
# =========================

entry = tk.Entry(
    window,
    font=("Arial", 28),
    bg="#252526",   # Very dark gray for entry background
    fg="white",       # White text for better contrast
    borderwidth=0,    # Remove border
    justify="right"   # Align text to the right for a calculator feel
)

entry.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,   # Adds horizontal space outside the widget, Creates left and right margin
    pady=20,   # Adds vertical space outside the widget, Creates top and bottom margin
    ipadx=8,   # increase width internally
    ipady=25,  # increase height internally
    sticky="nsew"   # Expand to fill available space in the grid cell
)

# =========================
# FUNCTIONS
# =========================

def click(value):
    current = entry.get()   # Reads existing text in entry widget
    entry.delete(0, tk.END) 
    entry.insert(0, current + str(value)) # Updates the display

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1]) # Here [:-1] starts from the beginning and stops before the last element

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# =========================
# BUTTON STYLE
# =========================

button_style = {
    "font": ("Arial", 18, "bold"),
    "width": 5,
    "height": 2,
    "bd": 0    # bd refers to border width
}

# =========================
# BUTTON CREATION FUNCTION
# =========================

def create_button(text, row, column,
                  bg_color, fg_color,
                  command):

    button = tk.Button(
        window,
        text=text,
        bg=bg_color,       # keep colour mentioned above
        fg=fg_color,
        activebackground="#555555",  # "555555" - Medium gray when button is clicked
        activeforeground="white",
        command=command,   # Links a function to the button click
        **button_style     # implements above style settings here”
    )

    button.grid(
        row=row,
        column=column,
        padx=2,
        pady=2,
        sticky="nsew"
    )

# =========================
# NUMBER BUTTONS
# =========================

create_button("7", 1, 0, "#333333", "white",   # #333333 - Dark charcoal
              lambda: click(7))

create_button("8", 1, 1, "#333333", "white",
              lambda: click(8))

create_button("9", 1, 2, "#333333", "white",
              lambda: click(9))

create_button("/", 1, 3, "#FF9500", "white",    # #FF9500 - Barcelona Orange
              lambda: click("/"))

create_button("4", 2, 0, "#333333", "white",
              lambda: click(4))

create_button("5", 2, 1, "#333333", "white",
              lambda: click(5))

create_button("6", 2, 2, "#333333", "white",
              lambda: click(6))

create_button("*", 2, 3, "#FF9500", "white",
              lambda: click("*"))

create_button("1", 3, 0, "#333333", "white",
              lambda: click(1))

create_button("2", 3, 1, "#333333", "white",
              lambda: click(2))

create_button("3", 3, 2, "#333333", "white",
              lambda: click(3))

create_button("-", 3, 3, "#FF9500", "white",
              lambda: click("-"))

create_button("0", 4, 0, "#333333", "white",
              lambda: click(0))

create_button(".", 4, 1, "#333333", "white",
              lambda: click("."))

create_button("=", 4, 2, "#00C853", "white",    # #00C853 - Bright green
              equal)

create_button("+", 4, 3, "#FF9500", "white",
              lambda: click("+"))

# =========================
# EXTRA BUTTONS
# =========================

create_button("C", 5, 0, "#D32F2F", "white",    # #D32F2F - Persian Red
              clear)

create_button("⌫", 5, 1, "#616161", "white",   # #616161 - Granite gray
              backspace)

create_button("%", 5, 2, "#616161", "white",
              lambda: click("%"))

create_button("//", 5, 3, "#616161", "white",
              lambda: click("//"))

# =========================
# GRID RESPONSIVENESS
# =========================

for i in range(6):     # Each value represents a row index in the grid
    window.grid_rowconfigure(i, weight=1)    # All rows get equal sharing of extra space when resized

for j in range(4):     # # Each value represents a column index in the grid
    window.grid_columnconfigure(j, weight=1)     # All columns get equal sharing of extra space when resized

# =========================
# RUN APPLICATION
# =========================

window.mainloop()