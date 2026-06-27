from pathlib import Path

from sat_cfdi.core.crypto import get_certificate_info, load_certificate
from sat_cfdi.models.certificate import CertificateInfo


class CertificateService:

    @staticmethod
    def load(path: Path) -> CertificateInfo:

        certificate = load_certificate(path)

        return get_certificate_info(certificate)
