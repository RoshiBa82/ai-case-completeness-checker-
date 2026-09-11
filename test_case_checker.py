from case_checker import check_case


# Test 1: Complete case
documents_complete = [
    "examensbevis",
    "transcript",
    "identitetshandling"
]

required_documents = [
    "examensbevis",
    "transcript",
    "identitetshandling"
]

print("Test 1: Komplett ärende")
print(check_case(documents_complete, required_documents))
print()


# Test 2: Missing document
documents_missing = [
    "examensbevis",
    "identitetshandling"
]

print("Test 2: Saknad handling")
print(check_case(documents_missing, required_documents))
print()


# Test 3: Duplicate document
documents_duplicate = [
    "examensbevis",
    "transcript",
    "transcript",
    "identitetshandling"
]

print("Test 3: Dubblett")
print(check_case(documents_duplicate, required_documents))
print()


# Test 4: Missing and duplicate document
documents_problem = [
    "examensbevis",
    "examensbevis",
    "identitetshandling"
]

print("Test 4: Saknad handling och möjlig dubblett")
print(check_case(documents_problem, required_documents))
