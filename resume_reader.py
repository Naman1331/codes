from docx import Document
import PyPDF2

def read_resume(file_path):
    if file_path.endswith('.pdf'):
        pdf_file_obj = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
        num_pages = len(pdf_reader.pages)
        text = ''
        for page in range(num_pages):
            page_obj = pdf_reader.pages[page]
            text += page_obj.extract_text()
        pdf_file_obj.close()
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        text = ' '.join([paragraph.text for paragraph in doc.paragraphs])
    else:
        text = ''
    return text

print((read_resume("/Users/namangandhi/Documents/codes/resumes/testuser1.pdf")))
