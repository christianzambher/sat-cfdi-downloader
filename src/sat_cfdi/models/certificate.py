from dataclasses import dataclass
from datetime import datetime


@dataclass
class CertificateInfo:
    common_name: str
    rfc: str
    serial_number: str
    issuer: str
    valid_from: datetime
    valid_to: datetime
