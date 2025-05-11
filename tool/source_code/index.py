import tkinter as tk
from tkinter import messagebox, filedialog
import joblib
import os

# --- Tooltip Helper Class ---
class CreateToolTip(object):
    """Create a tooltip for a given widget"""
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        widget.bind("<Enter>", self.enter)
        widget.bind("<Leave>", self.leave)

    def enter(self, event=None):
        self.showtip()

    def leave(self, event=None):
        self.hidetip()

    def showtip(self):
        if self.tipwindow or not self.text:
            return
        x, y, _, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 30
        y = y + cy + self.widget.winfo_rooty() + 10
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(
            tw, text=self.text, justify='left',
            background="#ffffe0", relief='solid', borderwidth=1,
            font=("Georgia", 10, "normal")
        )
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

# --- Model Loader ---
def load_model():
    model_path = "model/phishing_model.pkl"
    if not os.path.exists(model_path):
        messagebox.showerror("Error", f"Model file '{model_path}' not found.")
        root.destroy()
        return None, None
    return joblib.load(model_path)

# --- Prediction Function ---
def predict_email(event=None):
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Required", "Please enter email content.")
        return
    if len(text) < 10:
        messagebox.showinfo("Warning", "Input is very short; prediction may be unreliable.")
    features = vectorizer.transform([text])
    pred = model.predict(features)[0]
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(features)[0]
        confidence = max(proba) * 100
        result = f"🔴 Phishing ({confidence:.1f}%)" if pred == 1 else f"🟢 Legitimate ({confidence:.1f}%)"
    else:
        result = "🔴 Phishing" if pred == 1 else "🟢 Legitimate"
    result_label.config(text=f"Prediction: {result}")
    status_var.set("Prediction completed.")

# --- File Loader ---
def load_file(event=None):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, f.read())
        status_var.set(f"Loaded file: {os.path.basename(file_path)}")

# --- Clear Text ---
def clear_text(event=None):
    text_box.delete("1.0", tk.END)
    result_label.config(text="Prediction: ")
    status_var.set("Cleared input.")

# --- Save Result ---
def save_result(event=None):
    text = text_box.get("1.0", tk.END).strip()
    prediction = result_label.cget("text")
    if not text or prediction == "Prediction: ":
        messagebox.showwarning("Nothing to save", "No email content or prediction to save.")
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if save_path:
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write("Email Content:\n")
            f.write(text + "\n\n")
            f.write(prediction)
        messagebox.showinfo("Saved", f"Result saved to {save_path}")
        status_var.set(f"Result saved: {os.path.basename(save_path)}")

# --- GUI Setup ---
BG_COLOR = "#E6E6FA"  # Lilac background

root = tk.Tk()
root.title("Email Phishing Detector")
root.configure(bg=BG_COLOR)
root.geometry("900x600")
root.minsize(700, 400)

# --- Load Model ---
model, vectorizer = load_model()
if model is None or vectorizer is None:
    exit()

# --- Header ---
header = tk.Label(
    root,
    text="EMAIL PHISHING DETECTOR",
    font=("Georgia", 22, "bold"),
    bg=BG_COLOR,
    fg="#4B0082",
    pady=15
)
header.pack()

# --- Frame for Text and Scrollbar ---
text_frame = tk.Frame(root, bg=BG_COLOR)
text_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# --- Text Box with Scrollbar (Georgia, white text, dark bg) ---
text_box = tk.Text(
    text_frame, height=15, width=70, font=("Georgia", 12),
    bg="#2F2F4F", fg="white", wrap=tk.WORD, insertbackground="white"
)
text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_box.config(yscrollcommand=scrollbar.set)

# --- Buttons Frame ---
btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(pady=5, fill=tk.X)

predict_btn = tk.Button(
    btn_frame, text="Predict", command=predict_email,
    font=("Georgia", 12, "bold"), bg="#D1C4E9", fg="#4B0082", width=14
)
predict_btn.grid(row=0, column=0, padx=8)
CreateToolTip(predict_btn, "Predict if the email is phishing or legitimate (Ctrl+P)")

load_btn = tk.Button(
    btn_frame, text="Load from .txt file", command=load_file,
    font=("Georgia", 12), bg="#D1C4E9", fg="#4B0082", width=18
)
load_btn.grid(row=0, column=1, padx=8)
CreateToolTip(load_btn, "Load email content from a text file (Ctrl+L)")

clear_btn = tk.Button(
    btn_frame, text="Clear", command=clear_text,
    font=("Georgia", 12), bg="#D1C4E9", fg="#4B0082", width=10
)
clear_btn.grid(row=0, column=2, padx=8)
CreateToolTip(clear_btn, "Clear the email content and prediction (Ctrl+C)")

save_btn = tk.Button(
    btn_frame, text="Save Result", command=save_result,
    font=("Georgia", 12), bg="#D1C4E9", fg="#4B0082", width=12
)
save_btn.grid(row=0, column=3, padx=8)
CreateToolTip(save_btn, "Save the email content and prediction to a file (Ctrl+S)")

# --- Result Label ---
result_label = tk.Label(
    root, text="Prediction: ", font=("Georgia", 15, "bold"),
    bg=BG_COLOR, fg="#4B0082", pady=15
)
result_label.pack()

# --- Status Bar ---
status_var = tk.StringVar()
status_var.set("Ready")
status_bar = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W, bg=BG_COLOR, font=("Georgia", 10))
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# --- Keyboard Shortcuts ---
root.bind('<Control-p>', predict_email)
root.bind('<Control-l>', load_file)
root.bind('<Control-c>', clear_text)
root.bind('<Control-s>', save_result)

# --- Responsive Layout ---
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
text_frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
