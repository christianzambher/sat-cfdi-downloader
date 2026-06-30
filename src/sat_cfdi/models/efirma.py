from dataclasses import dataclass

from cryptography import x509
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

from sat_cfdi.models.certificate import CertificateInfo


@dataclass(slots=True)
class EFirma:
    """
    Represents a SAT e.firma.
    """

    certificate: x509.Certificate

    private_key: RSAPrivateKey

    info: CertificateInfo