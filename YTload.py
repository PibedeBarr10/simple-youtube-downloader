from pytube import YouTube

def show_options(link):
    video = YouTube(link)

    lista = video.streams.filter(file_extension = "mp4").order_by('resolution')

    return lista