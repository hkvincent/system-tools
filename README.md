# system-tools
These scripts are used to improve productivity  


# How to use video_duplicate_finder
The script uses a recursive method to find duplicate video files. This means that if you provide the parent folder, it will locate the leaf file until the end.

prerequisite:
1. **Install FFmpeg**:
   - Download FFmpeg from the [official website](https://ffmpeg.org/download.html).
   - Extract the downloaded files to a known location on your system.

2. **Add FFmpeg to the System PATH**:
   - On Windows, you can add FFmpeg to the PATH by searching for "Environment Variables" in the Start Menu.
   - Edit the system environment variables and append the path to the `bin` folder within the FFmpeg directory to the PATH variable.

3. **Verify Installation**:
   - Open a new command prompt and type `ffprobe -version` to check if it's correctly installed.

```bash
python video_duplicate_finder.py Z:\MultiMedia\Video
```



# How to use video_cal_length
The script recursively calculates the length of each video file by locating them within the parent folder and finally sums them up.
```bash
python cal_length.py
```
After typing the command above, you will be prompted to provide the path where you want to calculate its length.
