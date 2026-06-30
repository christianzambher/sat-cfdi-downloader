import xml.etree.ElementTree as ET

SOAP_NS = "http://schemas.xmlsoap.org/soap/envelope/"

AUTH_NS = "http://DescargaMasivaTerceros.gob.mx"

ET.register_namespace("", AUTH_NS)

def build_authentication_body(
    envelope: ET.Element,
) -> None:
    """
    Add the authentication body.
    """

    body = envelope.find(
        f"{{{SOAP_NS}}}Body"
    )

    ET.SubElement(
        body,
        ET.QName(
            AUTH_NS,
            "Autentica",
        ),
    )