from pathlib import Path
from sat_cfdi.crypto import load_certificate

def main():
    project_root = Path(__file__).resolve().parents[2]

    certificate_path = project_root / "certificados" / "fiel.cer"

    certificate = load_certificate(certificate_path)

    print(certificate)


if __name__ == "__main__":
    main()