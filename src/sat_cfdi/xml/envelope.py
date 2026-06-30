import xml.etree.ElementTree as ET


SOAP_NS = "http://schemas.xmlsoap.org/soap/envelope/"


def build_envelope() -> ET.Element:
    """
    Build the base SOAP envelope.
    """

    ET.register_namespace("s", SOAP_NS)

    envelope = ET.Element(
        ET.QName(SOAP_NS, "Envelope")
    )

    ET.SubElement(
        envelope,
        ET.QName(SOAP_NS, "Header"),
    )

    ET.SubElement(
        envelope,
        ET.QName(SOAP_NS, "Body"),
    )

    return envelope