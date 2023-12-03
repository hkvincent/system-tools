import subprocess
import os
import re

def get_video_length_ffprobe(file_path):
    """Get video duration using ffprobe."""
    cmd = [
        'ffprobe', '-v', 'error', '-show_entries',
        'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',
        file_path
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout)

def get_total_video_length(parent_folder):
    print("Scanning folder:", parent_folder)
    total_length = 0.0  # Total length in seconds
    for root, dirs, files in os.walk(parent_folder):
        for file in files:
            if re.search(r'\.(mp4|mkv|avi|mov|flv|wmv|mpeg|mpg)$', file, re.IGNORECASE):
                file_path = os.path.join(root, file)
                try:
                    video_length = get_video_length_ffprobe(file_path)
                    hours, remainder = divmod(video_length, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    print(f"{file} : length = {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds")
                    total_length += video_length
                except Exception as e:
                    print(f"Error getting duration of {file}: {e}")
    return total_length

# Prompt user for the path to the parent folder
parent_folder_path = input("Enter the path to your parent folder containing the video folders: ")

# Calculate total video length in the parent folder
total_length_in_seconds = get_total_video_length(parent_folder_path)

# Convert the total length from seconds to hours, minutes, and seconds
hours, remainder = divmod(total_length_in_seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# Print the total video length
print(f"Total video length is: {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds")
