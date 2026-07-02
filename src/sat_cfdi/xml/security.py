import xml.etree.ElementTree as ET

SOAP_NS = "http://schemas.xmlsoap.org/soap/envelope/"

WSSE_NS = (
    "http://docs.oasis-open.org/wss/2004/01/"
    "oasis-200401-wss-wssecurity-secext-1.0.xsd"
)

ET.register_namespace(
    "o",
    WSSE_NS,
)

def build_security_header(
    envelope: ET.Element,
) -> ET.Element:
    """
    Create the WS-Security element inside SOAP Header.
    """

    header = envelope.find(
        f"{{{SOAP_NS}}}Header"
    )

    security = ET.SubElement(
        header,
        ET.QName(
            WSSE_NS,
            "Security",
        ),
    )

    return security