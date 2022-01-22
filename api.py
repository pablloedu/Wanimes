import json
import requests
#search = input('Digite o nome do anime: ').replace(' ', "%20")
anime = 'slime'
offset = 0
https = f'https://kitsu.io/api/edge/anime?filter[text]={anime};page[limit]=18&page[offset]={offset}'


api = requests.get(https)


data = json.loads(api.content)['data']


animes = []
for k in data:
    lista = []

    lista.append(k['attributes']['canonicalTitle'])
    lista.append(k['attributes']['posterImage']['small'])
    animes.append(lista)
offset += 18



