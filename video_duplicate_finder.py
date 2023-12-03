import hashlib
import os
import sys

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_video_files(directory):
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv']  # Add other video formats if needed
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in video_extensions):
                yield os.path.join(root, file)

def main(directory):
    hashes = {}
    for video_file in get_video_files(directory):
        print(video_file)
        file_hash = calculate_md5(video_file)
        if file_hash in hashes:
            print(f"Duplicate found:\n1: {hashes[file_hash]}\n2: {video_file}")
            choice = input("Do you want to delete one of these files? (y/n): ")
            if choice.lower() == 'y':
                file_to_delete = input("Enter the number of the file to delete (1 or 2): ")
                file_to_delete = hashes[file_hash] if file_to_delete == '1' else video_file
                os.remove(file_to_delete)
                print(f"File {file_to_delete} has been deleted.")
        else:
            hashes[file_hash] = video_file

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    main(directory)
