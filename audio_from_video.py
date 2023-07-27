import moviepy.editor


video = moviepy.editor.VideoFileClip(filename='Гоблин.mp4')
audio = video.audio
audio.write_audiofile('Тест.mp3')