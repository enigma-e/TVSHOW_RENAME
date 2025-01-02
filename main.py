
### This file facilitates TV show subtitle file rename according to episode names

import argparse
import os
# import re
# import shutil


def parse_arguments():
    parser = argparse.ArgumentParser(description='Rename TV show subtitle files according to episode names.')
    parser.add_argument('vid_pattern', type=str, help='The first string pattern to parse', default='S01E')
    parser.add_argument('sub_pattern', type=str, help='The second string pattern to parse', default='1xE')
    parser.add_argument('vid_ext', type=str, help='The video file extension', default='.mp4', nargs='?')
    parser.add_argument('sub_ext', type=str, help='The subtitle file extension', default='.srt', nargs='?')
    return parser.parse_args()

def print_at_end(message, start=0):
    # columns, _ = shutil.get_terminal_size()
    columns, _ = os.get_terminal_size()
    # print(message.rjust(columns), end='', flush=True)
    # print('')
    print(message.rjust(columns - start))

def get_episode_num(srcStr):
    # Check if the first character is a digit
    if not srcStr[0].isdigit():
        return None
    # Implicit else
    episode = srcStr[0]
    for i in range(1, len(srcStr)):
        if srcStr[i].isdigit():
            episode += srcStr[i]
        else:
            break
    return episode

def get_video_files(pattern, ext):
    files = [f for f in os.listdir() if f.endswith(ext) and pattern in f]
    return files

# Gets the first subtitle file that matches the episode number
def get_subtitle_file(pattern, ext, episode_number):
    files = [f for f in os.listdir() if f.endswith(ext) and pattern in f]
    for f in files:
        sub_epi_num = int(get_episode_num(f.split(pattern)[-1]))
        if int(episode_number) == sub_epi_num:
            return f
    return None

if __name__ == "__main__":
    args = parse_arguments()

    video_files = get_video_files(args.vid_pattern, args.vid_ext)
    print(f'Found {len(video_files)} video files.')
    print(*video_files, sep='\n')
    usr_in = input("\nDo you want to continue [Y/n]?") or 'y'
    if not usr_in.lower() == 'y':
        print('Exiting...')
        exit()
    
    # Implicit else
    for vid in video_files:
        episode_number = get_episode_num(vid.split(args.vid_pattern)[-1])
        print(f"\nProcessing: \"{vid}\" \t\t Episode: {episode_number}.")
        
        new_sub_name = vid.split(args.vid_ext)[0] + args.sub_ext
        if new_sub_name in os.listdir():
            msg = f"\"{new_sub_name}\" exists"
            print(msg, end='')
            print_at_end('Skipped.', start=len(msg))
            continue
        
        # Implicit else
        subtitle_file = get_subtitle_file(args.sub_pattern, args.sub_ext,
                                          episode_number)        
        if subtitle_file is not None:
            msg = f'Renaming \"{subtitle_file}\" to \"{new_sub_name}\"...'
            print(msg, end='')
            os.rename(subtitle_file, new_sub_name)
            print_at_end('Done.', start=len(msg))
        else:
            msg = f"No subtitle file found for \"{vid}\""
            print(msg, end='')
            print_at_end('Skipped.', start=len(msg))