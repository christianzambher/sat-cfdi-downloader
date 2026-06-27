from pathlib import Path
from sat_cfdi.services.certificate_service import CertificateService
from sat_cfdi.ui.display import print_certificate_summary

def main():
    project_root = Path(__file__).resolve().parents[2]

    certificate = CertificateService.load(
        project_root / "certificados" / "fiel.cer"
    )

    print_certificate_summary(certificate)


if __name__ == "__main__":
    main()