from dataclasses import dataclass


@dataclass(slots=True)
class SecurityTimestamp:
    """
    Represents a WS-Security Timestamp.
    """

    created: str

    expires: str

    id: str