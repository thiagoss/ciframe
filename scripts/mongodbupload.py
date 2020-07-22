import pymongo
import argparse
import csv
import musica


def criar_leitor_de_argumentos():
    leitor = argparse.ArgumentParser()
    leitor.add_argument("arquivodedados", help="Arquivo com os dados")
    leitor.add_argument("dburl", help="URL do Banco de dados (formato mongodb://ip:port)")
    return leitor


class MongodbItemUploader:
    def __init__(self, url):
        self.cliente = pymongo.MongoClient(url)
        self.deciframe = self.cliente.deciframe
        self.musicas = self.deciframe.musicas

    def salvar(self, data):
        self.musicas.insert_one(data)

    def fechar(self):
        pass


def criar_entrada_musica(linha):
    id_unico = linha[musica.ARTISTA_ID] + '_' + linha[musica.MUSICA_ID]
    seq_famosa = linha[musica.SEQ_FAMOSA]
    if seq_famosa == 'NA':
        seq_famosa = None

    cifra = musica.limpa_cifra(linha[musica.CIFRA].split(";"))
    acordes = musica.acordes_da_cifra(cifra)

    return {
        "id": id_unico,
        "id-artista": linha[musica.ARTISTA_ID],
        "id-musica": linha[musica.MUSICA_ID],
        "artista": linha[musica.ARTISTA],
        "musica": linha[musica.MUSICA],
        "genero": linha[musica.GENERO],
        "popularidade": int(linha[musica.POPULARIDADE]),
        "seq-famosa": seq_famosa,
        "tom": linha[musica.TOM],
        "acordes": acordes,
        "cifra": cifra,
    }


def main():
    leitor = criar_leitor_de_argumentos()
    args = leitor.parse_args()

    uploader = MongodbItemUploader(args.dburl)

    with open(args.arquivodedados, 'r') as csvfile:
        leitorcsv = csv.reader(csvfile)
        for linha in leitorcsv:
            uploader.salvar(criar_entrada_musica(linha))
    uploader.fechar()


if __name__ == '__main__':
    main()
