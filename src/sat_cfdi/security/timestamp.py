from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

@dataclass(slots=True)
class SecurityTimestamp:

    created: str

    expires: str


def generate_timestamp(
    duration_minutes: int = 5,
) -> SecurityTimestamp:

    created = datetime.now(UTC)

    expires = created + timedelta(
        minutes=duration_minutes
    )

    return SecurityTimestamp(
        created=created.strftime(
            "%Y-%m-%dT%H:%M:%S.000Z"
        ),
        expires=expires.strftime(
            "%Y-%m-%dT%H:%M:%S.000Z"
        ),
    )