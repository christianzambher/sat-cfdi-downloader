class SATCFDIError(Exception):
    """Base exception for the project."""

    pass


class CertificateError(SATCFDIError):
    """Base exception for certificate-related errors."""

    pass


class CertificateNotFoundError(CertificateError):
    """Certificate file was not found."""

    pass


class InvalidCertificateError(CertificateError):
    """Certificate file is invalid."""

    pass


class ExpiredCertificateError(CertificateError):
    """Certificate has expired."""

    pass


class PrivateKeyError(SATCFDIError):
    """Base exception for private key errors."""

    pass


class PrivateKeyNotFoundError(PrivateKeyError):
    """Private key file was not found."""

    pass


class InvalidPrivateKeyError(PrivateKeyError):
    """Private key is invalid."""

    pass


class InvalidPasswordError(PrivateKeyError):
    """Password for private key is invalid."""

    pass