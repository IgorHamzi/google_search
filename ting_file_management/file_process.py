from ting_file_management.file_management import txt_importer


def process(path_file, instance):

    print(instance)

    for i in instance._data:
        if i['nome_do_arquivo'] == path_file:
            return ('arquivo já adicionado anteriomente')

    lines = txt_importer(path_file)

    file = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines
    }

    instance.enqueue(file)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
