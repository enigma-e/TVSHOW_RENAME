# Description
Rename TV show subtitle files with corresponding video file names by matching the episode number.
A string pattern before the episode number is required to pass as an argument to the script.

*As of now, mani.py script must be placed at the parent folder containing video files.*

### Usage
```bash
python main.py <pattern1> <pattern2> [extension1] [extension2]
```
- pattern1: A string pattern before the episode number in the video file name.
- pattern2: A string pattern before the episode number in the subtitle file name.
- extension1[optional]: Video file extension. Default is '.mp4'.
- extension2[optional]: Subtitle file extension. Default is '.srt'.

#### Example
```bash
python main.py 'S01E' 'S01E' '.mkv' '.srt'
```