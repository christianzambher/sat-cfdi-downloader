from pathlib import Path

from sat_cfdi.core.crypto import (
    get_certificate_info,
    load_certificate,
    load_private_key,
    validate_key_pair,
)

from sat_cfdi.models.efirma import EFirma


class EFirmaService:

    @staticmethod
    def load(
        certificate_path: Path,
        private_key_path: Path,
        password: str,
    ) -> EFirma:

        certificate = load_certificate(certificate_path)

        private_key = load_private_key(
            private_key_path,
            password,
        )

        validate_key_pair(
            certificate,
            private_key,
        )

        info = get_certificate_info(
            certificate,
        )

        return EFirma(
            certificate=certificate,
            private_key=private_key,
            info=info,
        )