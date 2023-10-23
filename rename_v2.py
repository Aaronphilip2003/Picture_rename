import os
from tkinter import Tk, Label, Entry, Button
from PIL import Image, ImageTk
from moviepy.editor import VideoFileClip

# Define the entry variable globally
entry = None

# Function to rename the file
def rename_file():
    new_name = entry.get()
    if new_name:
        try:
            os.rename(file_paths[index], os.path.join(directory, f"{new_name}{os.path.splitext(file_paths[index])[1]}"))
        except Exception as e:
            print(f"An error occurred: {e}")
    next_file()

# Function to display the next file
def next_file():
    global index
    if index < len(file_paths) - 1:
        index += 1
        display_file(file_paths[index])
    else:
        label.config(text="No more files")

# Function to display the file
def display_file(file_path):
    global panel, label, entry
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        img = Image.open(file_path)
        img = img.resize((300, 300))
        img = ImageTk.PhotoImage(img)
        panel.config(image=img)
        panel.image = img
        label.config(text=f"File {index + 1} of {len(file_paths)}: {os.path.basename(file_path)}")
    else:
        label.config(text="Preview not available for this file format")
        if file_path.lower().endswith(('.mp4', '.avi', '.mov')):
            clip = VideoFileClip(file_path)
            frame = clip.get_frame(0)  # Get the first frame as thumbnail
            img = Image.fromarray(frame)
            img = img.resize((300, 300))
            img = ImageTk.PhotoImage(img)
            panel.config(image=img)
            panel.image = img
        label.config(text=f"File {index + 1} of {len(file_paths)}: {os.path.basename(file_path)}")
    if entry:
        entry.delete(0, 'end')

# Define the directory
directory = "D:/Pictures-Aaron/Recent"

# List all supported files in the directory
supported_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".mp4",".MP4", ".avi", ".mp3", ".wav", ".mov"]
file_paths = [os.path.join(directory, file) for file in os.listdir(directory) if
              os.path.isfile(os.path.join(directory, file)) and
              os.path.splitext(file)[1].lower() in supported_extensions]

index = 0

# Set up the Tkinter window
root = Tk()
root.title("File Renamer and Previewer")

# Configure the window
root.geometry("400x400")
root.resizable(width=True, height=True)

# Display the first file
panel = Label(root)
panel.pack(pady=10)
label = Label(root, text="")
label.pack(pady=5)
display_file(file_paths[index])

# Display the file name entry and rename button
entry = Entry(root, width=30)
entry.pack(pady=5)
button = Button(root, text="Rename", command=rename_file)
button.pack(pady=5)

# Display the next button
next_button = Button(root, text="Next", command=next_file)
next_button.pack(pady=5)

root.mainloop()
