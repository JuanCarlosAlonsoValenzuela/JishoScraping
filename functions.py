from urllib.request import urlopen, Request
import re

# Definimos la función para eliminar las etiquetas html
def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', str(text)).strip()

def obtain_html(url):
    request = Request(url)
    response = urlopen(request)
    html = response.read()
    html.decode('utf-8')
    return html

def obtain_page(words, level, index):
    result = []
    for word in words:
        element = []

        # Identificador de nivel e índice
        element.append('JLPT-N' + str(level))
        element.append(index)
        index = index + 1

        # Obtenemos el kanji
        kanji = word.find('span', {'class': 'text'})
        kanji = remove_tags(kanji)
        element.append(kanji)

        # Obtenemos el furigana
        furigana = word.find('span', {'class': 'furigana'})
        furigana = remove_tags(furigana)
        element.append(furigana)

        # Obtenemos la categoría gramatical
        category = word.find('div', {'class': 'meaning-tags'})
        category = remove_tags(category)
        element.append(category)

        # Obtenemos las definiciones
        definitions = word.findAll('span', {'class': 'meaning-meaning'})

        i = 1
        for definition in definitions:
            definition = remove_tags(definition)
            if not ('【' in definition):
                element.append(str(i) + '.-' + definition)
                i = i + 1

        result.append(element)

    return result