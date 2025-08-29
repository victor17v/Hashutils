# hashutils/cli.py
import argparse
from pathlib import Path
from core import hash_string, hash_file

def main():
    parser = argparse.ArgumentParser(description="Calcula el hash de un texto o archivo")
    parser.add_argument("tipo", choices=["texto", "archivo"], help="Indica si quieres hashear un texto o un archivo")
    parser.add_argument("dato", help="El texto o la ruta del archivo")
    parser.add_argument("-a", "--algoritmo", default="sha256", help="Algoritmo de hash: md5, sha1, sha256, sha512")

    args = parser.parse_args()

    if args.tipo == "texto":
        print("Hash:", hash_string(args.dato, args.algoritmo))
    elif args.tipo == "archivo":
        if Path(args.dato).exists():
            print("Hash:", hash_file(args.dato, args.algoritmo))
        else:
            print("Archivo no encontrado:", args.dato)

if __name__ == "__main__":
    main()
