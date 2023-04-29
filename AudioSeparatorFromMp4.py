from moviepy.editor import *

def separate_audio(video_file, audio_file):
    # Load the video file
    video = VideoFileClip(video_file)

    # Extract the audio from the video
    audio = video.audio

    # Save the audio to a file
    audio.write_audiofile(audio_file)

    # Close the video and audio files
    video.close()
    audio.close()

# Example usage
video_path = "C:/Users/M1710/AppData/LocalLow/iTop Screen Recorder/Outputs/Terzieva3 .mp4"
audio_path = "D:/Fresh downloads/lekcia3.mp3"
separate_audio(video_path, audio_path)
