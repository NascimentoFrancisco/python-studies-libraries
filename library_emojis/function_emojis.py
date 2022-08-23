

#Para instalar a biblioteca com o pip: pip install emoji

import emoji

def filter_emojis_in_phrase(phrase:str):
    """Busca emojis no texto e se encontrar algum faz a substituição deles por seus nomes literais"""
    new_phrase = ''
    for word in phrase.strip():
        if emoji.is_emoji(word):
            new_phrase += emoji.demojize(word,language='pt').replace('_',' ').replace(':','')+' ' 
        else:
            new_phrase += word

    return new_phrase
print(filter_emojis_in_phrase('Parabéns a todos 👏👏👏🎉🎉'))