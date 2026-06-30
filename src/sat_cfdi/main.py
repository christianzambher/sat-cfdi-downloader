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
from sat_cfdi.services.efirma_service import EFirmaService
from sat_cfdi.security.timestamp import (
    generate_timestamp,
)

def main():
    try:
        efirma = EFirmaService.load(
            certificate_path=CERTIFICATES_DIR / "fiel.cer",
            private_key_path=CERTIFICATES_DIR / "fiel.key",
            password="Visual23"
        )

        print_certificate_summary(efirma.info)

        print("\n✓ e.firma loaded successfully")

        timestamp = generate_timestamp()

        print(timestamp)
    except SATCFDIError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
