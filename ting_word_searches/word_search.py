def exists_word(word, instance):
    ocorrencies = []
    inventory_words = []
    for i in instance._data:
        for line in i['linhas_do_arquivo']:
            if word.lower() in line.lower():
                ocorrencies.append({
                    'linha': i['linhas_do_arquivo'].index(line) + 1
                })
        inventory_words.append({
            "palavra": word,
            "arquivo":  i['nome_do_arquivo'],
            "ocorrencias": ocorrencies
        })

    if ocorrencies == []:
        return ocorrencies
    return inventory_words


def search_by_word(word, instance):
    ocorrencies = []
    inventory_words = []
    for i in instance._data:
        for line in i['linhas_do_arquivo']:
            if word.lower() in line.lower():
                ocorrencies.append({
                    'linha': i['linhas_do_arquivo'].index(line) + 1,
                    'conteudo': line
                })
        inventory_words.append({
            "palavra": word,
            "arquivo":  i['nome_do_arquivo'],
            "ocorrencias": ocorrencies
        })

    if ocorrencies == []:
        return ocorrencies
    return inventory_words
