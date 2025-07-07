from pytube import YouTube

def download_video(url, resolution='hd'):
    yt = YouTube(url)
    
    if resolution == 'hd':
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    elif resolution == 'fullhd':
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    
    if video:
        print(f"Baixando: {video.title} ({video.resolution})")
        video.download()
        print("Download concluído!")
    else:
        print("Nenhuma opção de download encontrada.")

if __name__ == "__main__":
    url = input("Digite a URL do vídeo do YouTube: ")
    resolution = input("Digite 'hd' para baixar em HD ou 'fullhd' para baixar em Full HD: ").lower()

    if resolution not in ['hd', 'fullhd']:
        print("Opção de resolução inválida.")
    else:
        download_video(url, resolution)
