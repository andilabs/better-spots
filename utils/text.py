import unidecode


def get_unaccented(accented_string):
    return unidecode.unidecode(accented_string)
