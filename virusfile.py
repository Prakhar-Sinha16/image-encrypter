import PyPDF2

def create_safe_pdf(file_path):
    pdf = PyPDF2.PdfWriter()
    pdf.add_blank_page()

    with open(file_path, "wb") as file:
        pdf.write(file)

# Usage
pdf_file_path = "C:/Users/prakh/OneDrive/Desktop/safe_file.pdf"
create_safe_pdf(pdf_file_path)
