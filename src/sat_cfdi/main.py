from sat_cfdi.core.paths import CERTIFICATES_DIR
from sat_cfdi.core.crypto import (
    load_certificate,
    load_private_key,
    validate_key_pair,
    get_certificate_info,
)
from sat_cfdi.exceptions import SATCFDIError
from sat_cfdi.services.certificate_service import CertificateService
from sat_cfdi.ui.display import print_certificate_summary


def main():
    try:
        certificate = load_certificate(CERTIFICATES_DIR / "fiel.cer")

        info = get_certificate_info(certificate)

        print_certificate_summary(info)

        private_key = load_private_key(
            CERTIFICATES_DIR / "fiel.key",
            "Visual23"
        )

        print(type(private_key))

        validate_key_pair(certificate, private_key)

        print("✓ Certificate and private key match")
    except SATCFDIError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
