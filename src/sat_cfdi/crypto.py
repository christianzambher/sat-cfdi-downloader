from pathlib import Path
from cryptography import x509


def load_certificate(path: str | Path) -> x509.Certificate:
    """
    Load a DER encoded X509 certificate.
    """

    path = Path(path)

    with open(path, "rb") as cert_file:
        return x509.load_der_x509_certificate(cert_file.read())