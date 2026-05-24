import tkinter as tk
from tkinter import filedialog

from pypdf import PdfReader

window = tk.Tk()

window.title("PDF Reader")
window.geometry("1280x720")

# Text Area Frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# Vertical Scrollbar
v_scrollbar = tk.Scrollbar(frame)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Text Box
textBox = tk.Text(frame, height=8)
textBox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Scrollbar Config
textBox["yscrollcommand"] = v_scrollbar.set
v_scrollbar.config(command=textBox.yview)


def upload_file():
    supported_file_types = [("PDF Files", "*.pdf")]
    file_path = filedialog.askopenfilename(filetypes=supported_file_types)
    if file_path:
        print("Selected file: ", file_path)
        # process file here
        reader = PdfReader(file_path)
        text = "\n".join(p.extract_text() for p in reader.pages)
        textBox.insert(index="1.0", chars=text)
        # print(text[:10000])


def handle_button_press():
    window.destroy()


upload_button = tk.Button(window, text="Upload File", command=upload_file)
upload_button.pack(pady=20)

button = tk.Button(text="Close", command=handle_button_press)
button.pack()

window.mainloop()
