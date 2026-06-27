from sat_cfdi.models.certificate import CertificateInfo


def print_certificate_summary(info: CertificateInfo) -> None:
    print("=" * 50)
    print("        SAT CFDI DOWNLOADER")
    print("=" * 50)

    print(f"RFC              : {info.rfc}")
    print(f"Razón Social     : {info.common_name}")
    print(f"Serie            : {info.serial_number}")

    print()
    print(f"Válido desde     : {info.valid_from}")
    print(f"Válido hasta     : {info.valid_to}")

    print()
    print(f"Emisor           :")
    print(info.issuer)

    print("=" * 50)
