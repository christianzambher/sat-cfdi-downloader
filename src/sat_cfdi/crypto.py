from pathlib import Path
from cryptography import x509


def load_certificate(path: str):
    """
    Load a DER encoded X509 certificate.
    """

    with open(path, "rb") as cert_file:
        return x509.load_der_x509_certificate(cert_file.read())