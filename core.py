import hashlib
from pathlib import Path

def hash_string(text: str, algo: str = "sha256") -> str:
    """
    Devuelve el hash de una cadena usando el algoritmo especificado.
    
    Args:
        text: Cadena a hashear
        algo: Algoritmo (md5, sha1, sha256, sha512...)
    
    Returns:
        Hash en formato hexadecimal
    """
    algo = algo.lower()
    h = hashlib.new(algo)
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def hash_file(file_path: str, algo: str = "sha256") -> str:
    """
    Devuelve el hash de un archivo usando el algoritmo especificado.
    
    Args:
        file_path: Ruta del archivo
        algo: Algoritmo (md5, sha1, sha256, sha512...)
    
    Returns:
        Hash en formato hexadecimal
    """
    algo = algo.lower()
    h = hashlib.new(algo)
    path = Path(file_path)
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()
