from pathlib import Path

from cryptography import x509
from cryptography.x509.oid import NameOID

from sat_cfdi.exceptions import (CertificateNotFoundError,
                                 InvalidCertificateError)
from sat_cfdi.models.certificate import CertificateInfo

from cryptography.hazmat.primitives.serialization import load_der_private_key

from cryptography.hazmat.primitives import serialization

def load_certificate(path: str | Path) -> x509.Certificate:
    """
    Load a DER encoded X509 certificate.
    """

    path = Path(path)

    if not path.exists():
        raise CertificateNotFoundError(f"Certificate not found: {path}")

    try:
        with open(path, "rb") as cert_file:
            return x509.load_der_x509_certificate(cert_file.read())
    except ValueError as exc:
        raise InvalidCertificateError("Invalid X509 certificate.") from exc


def get_certificate_info(certificate) -> CertificateInfo:
    subject = certificate.subject

    common_name = subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value

    rfc = subject.get_attributes_for_oid(NameOID.SERIAL_NUMBER)[0].value

    issuer = certificate.issuer.rfc4514_string()

    return CertificateInfo(
        common_name=common_name,
        rfc=rfc,
        serial_number=str(certificate.serial_number),
        issuer=issuer,
        valid_from=certificate.not_valid_before_utc,
        valid_to=certificate.not_valid_after_utc,
    )

def load_private_key(path: Path, password: str):

    path = Path(path)

    with path.open("rb") as key_file:

        private_key = load_der_private_key(
            key_file.read(),
            password=password.encode(),
        )

    return private_key

def validate_key_pair(certificate, private_key) -> bool:
    """
    Validate that the certificate and private key belong together.
    """

    certificate_public_key = certificate.public_key().public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    private_public_key = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    if certificate_public_key != private_public_key:
        raise InvalidCertificateError(
            "The certificate does not match the private key."
        )

    return True