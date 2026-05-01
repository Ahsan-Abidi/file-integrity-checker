import tkinter as tk
from tkinter import filedialog, messagebox
from auth import signup, login
from integrity_checker import check_integrity
from hash_utils import calculate_hash
from file_ops import load_hashes, update_hash
import datetime
import os

current_user = None
selected_file = None
history_data = []
current_hash = None


# ---------------- MAIN APP ----------------
def open_main_app():
    global current_user, selected_file, history_data, current_hash

    app = tk.Tk()
    app.title("File Integrity Dashboard")
    app.geometry("600x500")
    app.configure(bg="#1e1e2f")

    frame = tk.Frame(app, bg="#2c2c3e", padx=20, pady=20)
    frame.pack(expand=True, fill="both")

    tk.Label(frame, text=f"Welcome, {current_user}",
             bg="#2c2c3e", fg="white", font=("Arial", 14)).pack()

    status_label = tk.Label(frame, text="No file selected",
                            bg="#2c2c3e", fg="white", font=("Arial", 12))
    status_label.pack(pady=10)

    history_box = tk.Text(frame, height=10, width=60)
    history_box.pack(pady=10)

    graph_canvas = tk.Canvas(frame, height=100, bg="black")
    graph_canvas.pack(fill="x", pady=10)

    # ---------- CHECK FILE ----------
    def check_file():
        global selected_file, current_hash

        if not selected_file:
            return

        current_hash = calculate_hash(selected_file)
        stored = load_hashes()

        if selected_file in stored:
            if stored[selected_file] == current_hash:
                status = "SAFE"
                color = "green"
                save_btn.pack_forget()
            else:
                status = "MODIFIED"
                color = "red"
                save_btn.pack(pady=5)
        else:
            status = "NEW"
            color = "yellow"
            save_btn.pack(pady=5)

        now = datetime.datetime.now().strftime("%H:%M:%S")

        status_label.config(
            text=f"{os.path.basename(selected_file)} → {status} ({now})",
            fg=color
        )

        history_data.append(status)
        history_box.insert(tk.END, f"{now} → {status}\n")

        draw_graph()

    # ---------- SELECT FILE ----------
    def select_file():
        global selected_file
        selected_file = filedialog.askopenfilename()
        if selected_file:
            check_file()

    # ---------- SAVE CHANGES ----------
    def save_changes():
        global selected_file, current_hash
        if selected_file:
            update_hash(selected_file, current_hash)
            messagebox.showinfo("Saved", "Changes accepted & hash updated")
            check_file()

    # ---------- GRAPH ----------
    def draw_graph():
        graph_canvas.delete("all")

        x = 10
        for status in history_data[-20:]:
            if status == "SAFE":
                color = "green"
            elif status == "MODIFIED":
                color = "red"
            else:
                color = "yellow"

            graph_canvas.create_rectangle(x, 50, x + 10, 80, fill=color)
            x += 15

    # ---------- AUTO REFRESH ----------
    def auto_refresh():
        check_file()
        app.after(5000, auto_refresh)

    # ---------- LOGOUT ----------
    def logout():
        app.destroy()
        start_login()

    # ---------- BUTTONS ----------
    tk.Button(frame, text="Select File", command=select_file,
              bg="#4CAF50", fg="white", width=20).pack(pady=5)

    tk.Button(frame, text="Re-Check", command=check_file,
              bg="#2196F3", fg="white", width=20).pack(pady=5)

    tk.Button(frame, text="Start Auto Monitor", command=auto_refresh,
              bg="#FF9800", fg="white", width=20).pack(pady=5)

    save_btn = tk.Button(frame, text="Accept / Save Changes",
                         command=save_changes,
                         bg="#9C27B0", fg="white", width=20)

    save_btn.pack_forget()  # hidden initially

    tk.Button(frame, text="Logout", command=logout,
              bg="red", fg="white", width=20).pack(pady=5)

    app.mainloop()


# ---------------- LOGIN ----------------
def start_login():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("300x250")
    login_window.configure(bg="#1e1e2f")

    frame = tk.Frame(login_window, bg="#2c2c3e", padx=20, pady=20)
    frame.pack(expand=True)

    tk.Label(frame, text="Login", bg="#2c2c3e", fg="white",
             font=("Arial", 16)).pack(pady=10)

    user_entry = tk.Entry(frame)
    user_entry.pack(pady=5)

    pass_entry = tk.Entry(frame, show="*")
    pass_entry.pack(pady=5)

    def handle_login():
        global current_user
        if login(user_entry.get(), pass_entry.get()):
            current_user = user_entry.get()
            login_window.destroy()
            open_main_app()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def go_signup():
        login_window.destroy()
        start_signup()

    tk.Button(frame, text="Login", command=handle_login).pack(pady=5)
    tk.Button(frame, text="Signup", command=go_signup).pack()

    login_window.mainloop()


# ---------------- SIGNUP ----------------
def start_signup():
    signup_window = tk.Tk()
    signup_window.title("Signup")
    signup_window.geometry("300x250")
    signup_window.configure(bg="#1e1e2f")

    frame = tk.Frame(signup_window, bg="#2c2c3e", padx=20, pady=20)
    frame.pack(expand=True)

    user_entry = tk.Entry(frame)
    user_entry.pack(pady=5)

    pass_entry = tk.Entry(frame, show="*")
    pass_entry.pack(pady=5)

    def handle_signup():
        success, msg = signup(user_entry.get(), pass_entry.get())
        if success:
            messagebox.showinfo("Success", msg)
            signup_window.destroy()
            start_login()
        else:
            messagebox.showerror("Error", msg)

    tk.Button(frame, text="Create Account", command=handle_signup).pack(pady=10)

    signup_window.mainloop()


# ---------------- START ----------------
start_login()