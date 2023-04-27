import PyPDF2

def scan_pdf(file_path):
    virus_signatures = [
        "malware_signature_1",
        "malware_signature_2",
        "malware_signature_3"
        # Add more virus signatures as needed
    ]

    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        content = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            content += page.extract_text()

        for signature in virus_signatures:
            if signature in content:
                return True

    return False

# Usage
pdf_file_path = "C:/Users/prakh/Downloads/Assignment-1.pdf"
if scan_pdf(pdf_file_path):
    print("Virus detected in the PDF file.")
else:
    print("No virus detected in the PDF file.")
