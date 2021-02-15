from datetime import datetime
import instaloader

#carregando a biblioteca
L = instaloader.Instaloader()
# Fazendo login coma conta desejada
L.login('Seu usuario', 'Sua senha')

#Aqui você coloca o @ de quem quer saber sobre os seguidores
followers = instaloader.Profile.from_username(L.context, 'julio_mguerra').get_followers()
followees = instaloader.Profile.from_username(L.context, 'julio_mguerra').get_followees()

#Imprimindo resultados
print('\n')
print('Seguidores: ' + str(followers._data['count']))
print('Seguindo: ' + str(followees._data['count']))
print('\n')
print('Lista e informações de seguidores:')
print('\n')
print(followers._data['edges'])