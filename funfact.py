import tkinter as tk
import urllib.request
import json
import threading

# ---------------- FUNCTIONS ---------------- #
def fetch_fact():
    try:
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            fact = data.get('text', 'Could not get a fact.')
            window.after(0, update_ui, fact, "")
    except Exception as e:
        window.after(0, update_ui, "Error fetching fact 😢", "Check your internet connection.")

def generate_fact():
    fact_label.config(text="Fetching fact... ⏳")
    detail_label.config(text="")
    threading.Thread(target=fetch_fact, daemon=True).start()

def update_ui(fact, detail):
    fact_label.config(text=fact)
    detail_label.config(text=detail)
    animate_text()

def animate_text():
    fact_label.place(y=140)
    move_up(140)

def move_up(y):
    if y > 100:
        y -= 2
        fact_label.place(y=y)
        window.after(10, move_up, y)

# ---------------- GUI ---------------- #
window = tk.Tk()
window.title("🎉 Fun Fact Generator")
window.geometry("500x350")
window.configure(bg="#1e1e2f")
window.resizable(False, False)

# ---------------- TITLE ---------------- #
title = tk.Label(
    window,
    text="🎲 FUN FACT GENERATOR 🎲",
    font=("Comic Sans MS", 20, "bold"),
    fg="#ffdd57",
    bg="#1e1e2f"
)
title.pack(pady=15)

# ---------------- FACT DISPLAY ---------------- #
fact_label = tk.Label(
    window,
    text="Click below for a fun fact 😄",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#1e1e2f",
    wraplength=450,
    justify="center"
)
fact_label.place(x=25, y=100)

detail_label = tk.Label(
    window,
    text="",
    font=("Arial", 11),
    fg="#a9c6ff",
    bg="#1e1e2f",
    wraplength=450,
    justify="center"
)
detail_label.place(x=25, y=180)

# ---------------- BUTTON ---------------- #
def on_enter(e):
    button.config(bg="#ffdd57", fg="black")

def on_leave(e):
    button.config(bg="#4caf50", fg="white")

button = tk.Button(
    window,
    text="✨ Generate Fun Fact ✨",
    font=("Arial", 13, "bold"),
    bg="#4caf50",
    fg="white",
    activebackground="#81c784",
    activeforeground="black",
    command=generate_fact,
    relief="flat",
    padx=20,
    pady=10
)
button.pack(side="bottom", pady=30)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

# ---------------- RUN ---------------- #
window.mainloop()
