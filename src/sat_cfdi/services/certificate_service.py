from pathlib import Path

from sat_cfdi.core.crypto import (
    load_certificate,
    get_certificate_info,
)

from sat_cfdi.models.certificate import CertificateInfo


class CertificateService:

    @staticmethod
    def load(path: Path) -> CertificateInfo:

        certificate = load_certificate(path)

        return get_certificate_info(certificate)