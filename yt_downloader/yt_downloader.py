import yt_dlp
from concurrent.futures import ThreadPoolExecutor

def baixa_audio(URL):
    #Configuracao do Youtube Download
    config_yt_ops = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "320",
            }
        ],
        "outtmpl": "yt_downloader/download/%(title)s.%(ext)s",
        "noplaylist": False,
        "ffmpeg_location": r"C:\programcao\downloader_video\treino_pyspark\yt_downloader\ffmpeg\bin"
    }
    
    try:
        #Tratamento de Erro para a URL 
        if not (URL):
            print(f'{URL} url informada esta vazia ou possui um erro')
        #Inicia o processo de Download do Video para WAV
        with yt_dlp.YoutubeDL(config_yt_ops) as ydl:
            print(f'inciando o download do video: {URL}')
            ydl.download([URL])
            print(f'download concluido em: download')
    except Exception as e:
    #Exception de erro do download caso o Try n inicie
        print(f'Ocorreu um erro ao baixar: {e}')


if __name__== '__main__':
    # Inputando a URL do video que ira ser baixado
    URL = input('cole sua URL aq: ')
    baixa_audio(URL)

