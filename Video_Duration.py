import os
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog

def calculate_total_duration(folder_path):
    total_duration_seconds = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith((".mp4", ".avi", ".mkv")):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                try:
                    clip = VideoFileClip(file_path)
                    total_duration_seconds += clip.duration
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    return total_duration_seconds


def convert_seconds_to_hours_minutes(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return hours, minutes

def select_folder():
    folder_path = filedialog.askdirectory(title="Select Folder")
    if folder_path:
        total_duration_seconds = calculate_total_duration(folder_path)
        total_hours, total_minutes = convert_seconds_to_hours_minutes(total_duration_seconds)
        result_label.config(text=f"Total duration of all videos: {total_duration_seconds} seconds "
                                  f"({total_hours} hours {total_minutes} minutes)")

# Create the main window
root = tk.Tk()
root.title("Video Duration Calculator")

# Create a button to select a folder
select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the main loop
root.mainloop()
