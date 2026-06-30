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

    @property
    def rfc(self) -> str:
        return self.info.rfc

    @property
    def owner(self) -> str:
        return self.info.common_name

    @property
    def serial_number(self) -> str:
        return self.info.serial_number