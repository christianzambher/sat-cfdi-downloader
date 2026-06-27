from sat_cfdi.core.paths import CERTIFICATES_DIR
from sat_cfdi.services.certificate_service import CertificateService
from sat_cfdi.ui.display import print_certificate_summary

def main():
    certificate = CertificateService.load(
        CERTIFICATES_DIR / "fiel.cer"
    )

    print_certificate_summary(certificate)


if __name__ == "__main__":
    main()