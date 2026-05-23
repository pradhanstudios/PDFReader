import tkinter as tk
from tkinter import filedialog

from pypdf import PdfReader

window = tk.Tk()

window.title("PDF Reader")
window.geometry("1280x720")


def upload_file():
    supported_file_types = [("PDF Files", "*.pdf")]
    file_path = filedialog.askopenfilename(filetypes=supported_file_types)
    if file_path:
        print("Selected file: ", file_path)
        # process file here
        reader = PdfReader(file_path)
        text = "\n".join(p.extract_text() for p in reader.pages)
        print(text[:10000])


def handle_button_press():
    window.destroy()


upload_button = tk.Button(window, text="Upload File", command=upload_file)
upload_button.pack(pady=20)

button = tk.Button(text="Close", command=handle_button_press)
button.pack()

window.mainloop()
