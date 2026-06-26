# SAT CFDI Downloader

A Python implementation of the Mexican SAT CFDI Mass Download Web Services.

## Overview

This project aims to implement the complete CFDI Mass Download workflow provided by the Mexican Tax Administration Service (SAT), including authentication with e.firma, request generation, status verification, package download, and XML extraction.

The project is being developed incrementally, documenting each stage of the implementation to better understand the underlying technologies involved.

## Features (Planned)

* Read and validate SAT e.firma certificates
* Authenticate using WS-Security
* Request CFDI mass downloads
* Verify request status
* Download generated packages
* Extract CFDI XML files
* Command-line interface (CLI)
* FastAPI integration
* Docker support

## Project Status

| Phase | Description                  | Status |
| ----- | ---------------------------- | ------ |
| 0     | Project initialization       | ✅      |
| 1     | Read e.firma (.cer and .key) | ⏳      |
| 2     | WS-Security authentication   | ⏳      |
| 3     | Download request             | ⏳      |
| 4     | Request verification         | ⏳      |
| 5     | Package download             | ⏳      |
| 6     | XML extraction               | ⏳      |
| 7     | CLI                          | ⏳      |
| 8     | FastAPI integration          | ⏳      |
| 9     | Docker                       | ⏳      |

## Technologies

* Python 3.13+
* Cryptography
* XML
* SOAP
* WS-Security
* Requests
* lxml

## Disclaimer

This project is intended for educational and development purposes. It is not affiliated with or endorsed by the Servicio de Administración Tributaria (SAT).
