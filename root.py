import functions
from bs4 import BeautifulSoup
from pandas import DataFrame

# Insertamos la url
# N5: 33 páginas
# N4: 29 páginas
# N3: 89 páginas
# N2: 91 páginas
# N1: 173 páginas
# Parámetros
level = 1
n_pages = 173


final_result = []
index = 1
for i in range(n_pages):
    url = 'https://jisho.org/search/%23words%23jlpt-n' + str(level) + '?page=' + str(i+1)

    html = functions.obtain_html(url)
    bs = BeautifulSoup(html, 'lxml')

    # Obtenemos todas las palabras
    words = bs.findAll('div', {'class':'concept_light clearfix'})

    # Obtenemos la lista de términos
    print('Obteniendo página {} de {}'.format(i+1, n_pages))
    page = functions.obtain_page(words, level, index)
    index = index + len(words)

    # Lo añadimos a la lista final
    final_result = final_result + page

print(final_result)
print(len(final_result))

document = DataFrame.from_records(final_result)
document.to_csv('csv/N' + str(level) + '.txt', index=False, sep='\t')