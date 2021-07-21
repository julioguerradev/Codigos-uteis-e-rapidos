from pytube import YouTube

link = input("Digite o link do vídeo que seja baixar: ");
path = input("Digite o diretório que seja salvar o vídeo: ");
yt = YouTube(link)

print("Título: ", yt.title);
print("Número de views: ", yt.views);
print("Tamanho do vídeo: ", yt.length, "segundos");
print("Avaliação do vídeo: ", yt.rating);

ys = yt.streams.get_highest_resolution();

print("Baixando...");
ys.download(path);
print("Download Completo!");
