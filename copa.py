import requests 
from time import sleep 
from datetime import datetime

def get_match_date():
    return requests.get(
        url='https://temporeal.lance.com.br/storage/matches/copa-do-mundo-2022-28-11-2022-camaroesxservia.json'
    ).json()

update = None 
while True:
    dados = get_match_date()

    narracoes = dados['match']['narrations']
    ultima_narracao = narracoes[len(narracoes)-1]
    time =datetime.strptime(ultima_narracao['created_at'], '%Y-%m-%dT%H:%M:%S.000000Z')

    if(not update) or (time > update):
        update = time
        momento = narracoes[len(narracoes)-1]['moment']
        narracao_text = narracoes[len(narracoes)-1]['text']
        print (f'.\n.\n.\n{momento}" - {narracao_text}')

    sleep(30)
