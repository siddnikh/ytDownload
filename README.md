# ytDownload
Built using [MoviePy](https://github.com/Zulko/moviepy) and [PyTube](https://github.com/nficano/pytube)

All you have to do is, run the Python Script in your Terminal, with the YouTube video link, and the desired resolution of that very video. If the resolution isn't available for that video, the program will terminate itself.

For the script to work, you need to have a few libraries installed, and their installation can be done as follows:
```
pip install ffmpeg
pip install moviepy
pip install pytube
pip install imageio
```
The first time you run the program, ffmpeg.exe is installed. All the other times, the machine will find it installed and it won't occur again.

## Usage:
```
python main.py https://www.youtube.com/watch?v=v65-RkxYVUY 480p
```

The video will be saved in a folder called 'files' in your present directory, and will be in .mp4 format.
I did this script for fun and to practice xD which probably justifies why this isn't fast. But anyway, this keeps you from disgusting ads on third party websites, and just.. has a nice feel to it xD

Please report if you come across any issues :)
