from sat_cfdi.core.paths import CERTIFICATES_DIR
from sat_cfdi.core.crypto import load_private_key
from sat_cfdi.exceptions import SATCFDIError
from sat_cfdi.services.certificate_service import CertificateService
from sat_cfdi.ui.display import print_certificate_summary


def main():
    try:
        certificate = CertificateService.load(CERTIFICATES_DIR / "fiel.cer")

        print_certificate_summary(certificate)

        private_key = load_private_key(
            CERTIFICATES_DIR / "fiel.key",
            "Visual23"
        )

        print(type(private_key))
    except SATCFDIError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
