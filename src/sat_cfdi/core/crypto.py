from pathlib import Path
from cryptography import x509
from cryptography.x509.oid import NameOID
from sat_cfdi.models.certificate import CertificateInfo


def load_certificate(path: str | Path) -> x509.Certificate:
    """
    Load a DER encoded X509 certificate.
    """

    path = Path(path)

    with open(path, "rb") as cert_file:
        return x509.load_der_x509_certificate(cert_file.read())


def get_certificate_info(certificate) -> CertificateInfo:
    subject = certificate.subject

    common_name = subject.get_attributes_for_oid(
        NameOID.COMMON_NAME
    )[0].value

    rfc = subject.get_attributes_for_oid(
        NameOID.SERIAL_NUMBER
    )[0].value

    issuer = certificate.issuer.rfc4514_string()

    return CertificateInfo(
        common_name=common_name,
        rfc=rfc,
        serial_number=str(certificate.serial_number),
        issuer=issuer,
        valid_from=certificate.not_valid_before_utc,
        valid_to=certificate.not_valid_after_utc,
    )