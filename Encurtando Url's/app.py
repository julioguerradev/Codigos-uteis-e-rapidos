import pyshorteners

# Aqui você guarda na variável a URL que deseja encurtar
url = 'https://www.instagram.com/julio_mguerra/'

# Aqui você chama a lib
s = pyshorteners.Shortener()

# Processo para encurtar a URL
shortUrl = s.tinyurl.short(url)

# Exibindo o resultado
print(f"URL Encurtada: {shortUrl}")