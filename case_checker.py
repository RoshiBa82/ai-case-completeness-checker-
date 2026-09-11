def check_case(documents, required_documents):
    """
    Checks whether the documents in a case appear to be complete.
    """

    results = []

    # Check for required documents
    for document in required_documents:
        if document not in documents:
            results.append(f"Missing document: {document}")

    # Check for duplicates
    if len(documents) != len(set(documents)):
        results.append("Possible duplicate document found.")

    # Check whether the case appears complete
    if not results:
        results.append("The case appears complete.")

    return results


# Example
documents = [
    "examination_certificate",
    "transcript",
    "identity_document"
]

required_documents = [
    "examination_certificate",
    "transcript",
    "identity_document"
]

result = check_case(documents, required_documents)

for message in result:
    print(message)

