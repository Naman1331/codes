import PyPDF2
import re
from docx import Document
import nltk
from nltk.corpus import stopwords

# Step 2
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

# Step 3
def extract_personal_info(text):
    name = re.search(r'Name: (.*)', text)
    email = re.search(r'Email: (.*)', text)
    phone = re.search(r'Phone: (.*)', text)
    return name, email, phone

# Step 4
def extract_skills(text):
    skills = ['Python', 'Java', 'C++', 'JavaScript', 'SQL']  # Add more skills here
    found_skills = [skill for skill in skills if skill in text]
    return found_skills

# Step 5
def extract_education_experience(text):
    education = re.search(r'Education: (.*)', text)
    experience = re.search(r'Experience: (.*)', text)
    return education, experience

# Step 6
def main(file_path):
    text = read_resume(file_path)
    print(text)
    print("*"*100)
    name, email, phone = extract_personal_info(text)
    skills = extract_skills(text)
    education, experience = extract_education_experience(text)
    print(f'Name: {name}\nEmail: {email}\nPhone: {phone}\nSkills: {skills}\nEducation: {education}\nExperience: {experience}')

main('/Users/namangandhi/Documents/codes/resumes/testuser1.pdf')
