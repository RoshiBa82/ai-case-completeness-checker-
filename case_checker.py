def check_case(documents, required_documents):
    """
    Kontrollerar om dokumenten i ett ärende verkar vara kompletta.
    """

    results = []

    # Kontrollera om obligatoriska handlingar saknas
    missing_documents = []

    for document in required_documents:
        if document not in documents:
            missing_documents.append(document)

    if missing_documents:
        for document in missing_documents:
            results.append(f"Saknad handling: {document}")

    # Kontrollera om någon handling förekommer flera gånger
    if len(documents) != len(set(documents)):
        results.append("Möjlig dubblett av handling har hittats.")

    # Bedöm om ärendet verkar vara komplett
    if not results:
        results.append("Ärendet verkar vara komplett.")

    return results


def print_case_result(documents, required_documents):
    """
    Skriver ut en enkel status för ärendet.
    """

    results = check_case(documents, required_documents)

    print("AI-kontroll av ärendets fullständighet")
    print("--------------------------------------")

    if results == ["Ärendet verkar vara komplett."]:
        print("Ärendestatus: Komplett")
    else:
        print("Ärendestatus: Behöver granskas")

    for result in results:
        print(f"- {result}")


# Exempel på ett ärende

documents = [
    "examensbevis",
    "transcript",
     "översättningar",
    "identitetshandling"
]

required_documents = [
    "examensbevis",
    "transcript",
     "översättningar",
    "identitetshandling"
]

print_case_result(documents, required_documents)
