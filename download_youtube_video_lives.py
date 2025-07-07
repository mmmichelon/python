from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Ocorreu um erro.")
    print("Download concluído com sucesso.")

link = input("Digite o URL do vídeo do YouTube: ")
Download(link)
