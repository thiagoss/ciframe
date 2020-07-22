# Constantes
# colunas do csv
ARTISTA_ID = 0
MUSICA_ID = 1
ARTISTA = 2
MUSICA = 3
GENERO = 4
POPULARIDADE = 5
TOM = 6
SEQ_FAMOSA = 7
CIFRA = 8


def limpa_cifra(raw_cifra):
    cifra = []
    for m in raw_cifra:
        if m.strip() != '':
            # filtra tablaturas
            if '|' in m:
                acorde = m.split('|')[0].split()[0]
                cifra.append(acorde)
            # lida com acordes separados por espaço
            else:
                tokens = [token for token in m.split()]
                cifra += tokens
    return cifra


def acordes_da_cifra(cifra):
    return list(set(cifra))


class Musica:

    def __init__(self, id_artista, nome_artista, id_musica, nome_musica,

            genero, popularidade, seqs_famosas, tom, cifra):

            self.id_artista = id_artista
            self.nome_artista = nome_artista

            self.id_musica = id_musica
            self.nome_musica = nome_musica

            self.genero = genero
            self.popularidade = popularidade
            self.tom = tom
            self.cifra = cifra
            self.acordes = acordes_da_cifra(cifra)
            self.seqs_famosas = seqs_famosas

            self.id_unico_musica = '%s_%s' % (id_artista, id_musica)

            self.url = 'http://www.cifraclub.com.br/%s/%s' % (id_artista, id_musica)

    def __str__(self):
        return '%s,%s,%s' % (self.id_unico_musica, self.genero, self.popularidade)
