import moviepy.editor
video_input = input("Enter video name or path : ")
#video_input1 = video_input + ".mp4"
video = moviepy.editor.VideoFileClip(video_input)
audio = video.audio
audio_output = input("Enter the name of the audio file you want to give : ")
audio_output1 = audio_output + ".mp3"
audio.write_audiofile(audio_output1)