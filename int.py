import tkinter as tk

# Function to display user information
def show_info():
    output.delete(1.0, tk.END)   # Clear previous text

    output.insert(
        tk.END,
        f"""Full Name : {name_entry.get()}

School    : {school_entry.get()}

Class     : {class_entry.get()}

Hobbies   : {hobby_entry.get()}

Age       : {age_entry.get()}
"""
    )

# Main Window
window = tk.Tk()
window.title("Student Information")
window.geometry("1000x800")
window.config(bg="#1E293B")

# Heading
heading = tk.Label(
    window,
    text="Student Information Form",
    font=("Arial", 24, "bold"),
    bg="#1E293B",
    fg="#FACC15"
)
heading.pack(pady=20)

# Styles
label_style = {
    "font": ("Arial", 14, "bold"),
    "bg": "#1E293B",
    "fg": "#E2E8F0"
}

entry_style = {
    "font": ("Arial", 14),
    "bg": "#334155",
    "fg": "white",
    "insertbackground": "white",
    "width": 40
}

# Full Name
tk.Label(window, text="Full Name", **label_style).pack()
name_entry = tk.Entry(window, **entry_style)
name_entry.pack(pady=8)

# School
tk.Label(window, text="School", **label_style).pack()
school_entry = tk.Entry(window, **entry_style)
school_entry.pack(pady=8)

# Class
tk.Label(window, text="Class", **label_style).pack()
class_entry = tk.Entry(window, **entry_style)
class_entry.pack(pady=8)

# Hobbies
tk.Label(window, text="Hobbies", **label_style).pack()
hobby_entry = tk.Entry(window, **entry_style)
hobby_entry.pack(pady=8)

# Age
tk.Label(window, text="Age", **label_style).pack()
age_entry = tk.Entry(window, **entry_style)
age_entry.pack(pady=8)

# Button
button = tk.Button(
    window,
    text="Show Information",
    font=("Arial", 15, "bold"),
    bg="#FACC15",
    fg="#1E293B",
    padx=15,
    pady=8,
    command=show_info
)
button.pack(pady=20)

# Frame for Text and Scrollbar
frame = tk.Frame(window, bg="#1E293B")
frame.pack(pady=10)

# Scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Scrollable Text Box
output = tk.Text(
    frame,
    width=70,
    height=18,
    font=("Consolas", 14),
    bg="#0F172A",
    fg="#38BDF8",
    yscrollcommand=scrollbar.set
)
output.pack(side=tk.LEFT)

scrollbar.config(command=output.yview)

window.mainloop()