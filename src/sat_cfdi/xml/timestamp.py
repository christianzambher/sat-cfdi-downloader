from datetime import UTC, datetime, timedelta
import xml.etree.ElementTree as ET

from sat_cfdi.models.security_timestamp import SecurityTimestamp

WSU_NS = (
    "http://docs.oasis-open.org/wss/2004/01/"
    "oasis-200401-wss-wssecurity-utility-1.0.xsd"
)

ET.register_namespace(
    "u",
    WSU_NS,
)

def generate_timestamp(
    minutes: int = 5,
) -> SecurityTimestamp:

    created = datetime.now(
        UTC,
    )

    expires = created + timedelta(
        minutes=minutes,
    )

    return SecurityTimestamp(

        created=created.strftime(
            "%Y-%m-%dT%H:%M:%S.000Z"
        ),

        expires=expires.strftime(
            "%Y-%m-%dT%H:%M:%S.000Z"
        ),

        id="TS-1",
    )

def build_timestamp(
    security: ET.Element,
    timestamp: SecurityTimestamp,
) -> ET.Element:

    timestamp_element = ET.SubElement(

        security,

        ET.QName(
            WSU_NS,
            "Timestamp",
        ),

        {
            ET.QName(
                WSU_NS,
                "Id",
            ): timestamp.id
        },
    )

    ET.SubElement(

        timestamp_element,

        ET.QName(
            WSU_NS,
            "Created",
        ),

    ).text = timestamp.created

    ET.SubElement(

        timestamp_element,

        ET.QName(
            WSU_NS,
            "Expires",
        ),

    ).text = timestamp.expires

    return timestamp_element