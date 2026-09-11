# AI Case Completeness Checker

Final project for the Building AI course.

## Summary

The idea is to use AI to help with the first check of documents in an application case. The system could help identify missing or duplicate documents, check whether documents seem to belong to the applicant, and give an indication of whether the case is complete enough to continue processing.

The purpose is not to replace the case officer. Instead, the AI would be used as a support tool for the initial document check.

## Background

When processing an application, a case can contain several different documents. Before the case can continue, the submitted documents may need to be checked to see if the required information and documents are there.

This first check can involve a lot of repetitive work. The idea of this project is to use AI to make this part of the process easier and faster.

For example, the system could help answer questions such as:

- What type of document has been submitted?
- Is an examination certificate included?
- Does the document contain information such as the education, institution and graduation year?
- Does the name or other information on a document seem to match the applicant?
- Has the same document been submitted more than once?
- Is an important document missing?
- Does the case appear to have enough documents to continue to processing?

The AI would not make the final decision. It would instead point out possible problems so that a case officer can review them.

## How is it used?

A possible workflow could be:

1. Documents are received in an application case.
2. The AI reads and analyses the documents.
3. The system identifies the type of each document.
4. It extracts relevant information from the documents.
5. It checks the documents against the information and documents expected for the case.
6. It highlights possible missing, duplicate or incorrect documents.
7. It gives an indication of whether the case appears complete.
8. A case officer reviews the result and makes the final decision.

For example, the system could show something like:

**Case status: Possible missing document**

- Examination certificate: Found
- Transcript: Found
- Identity document: Found
- Required document: Missing

The case officer can then check the information before continuing with the case.

## Data sources and AI methods

A possible prototype could use anonymised example documents and examples of different document types.

The project could use several AI techniques:

- Machine learning
- Document classification
- Optical Character Recognition (OCR)
- Natural Language Processing (NLP)
- Similarity detection for finding duplicate documents

OCR could be used to extract text from scanned documents or images.

Document classification could help identify what type of document has been submitted.

NLP could help extract information such as names, institutions, education and dates.

Similarity detection could help identify documents that are the same or very similar.

In a real implementation, the data would need to be handled carefully because application documents can contain personal information.

## Challenges

There are several challenges with this idea.

Documents can look very different from each other. They can have different formats, languages, layouts and quality. Some documents may also be scanned images or difficult to read.

It may also be difficult for an AI system to decide whether a document really belongs to the applicant. A difference in a name does not always mean that the document is incorrect.

Another challenge is deciding what makes a case complete. Different types of cases may require different documents, so the system would need clear rules and good examples.

Privacy and information security are also important. A real system would need to follow the relevant rules for handling personal information and documents.

Because of these limitations, the AI should be used as decision support. A case officer should be able to review the result and make the final decision.

## What next?

The first step could be to build a small prototype using anonymised example documents.

The prototype could start with only a few document types and a few simple checks, for example:

- Identify the document type
- Check whether required documents are present
- Detect possible duplicate documents
- Check whether basic information appears to match the applicant

If the prototype works well, it could later be expanded to handle more document types and more complex checks.

## Acknowledgments

This project idea was inspired by practical challenges related to document handling and case processing.

The project was created as a final project for the Building AI course by the University of Helsinki and Reaktor.
