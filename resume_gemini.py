import google.generativeai as genai
import json
from docx import Document
import PyPDF2

genai.configure(api_key="")


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


# The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
model = genai.GenerativeModel('gemini-1.5-flash')
prompt = """I will give you a resume, I wanto you to undersstand it and wite it in a json format so that I 
can store it and access any information from it I want. Do not change any information form the resume, keep it word to word as given in 
the resume and follow the fomrat that I give you. Just add the information accrodingly.
"""

resume_format="""
{
  "personal_info": {
    "name": "Your Name",
    "email": "your.email@domain.com",
    "phone": "+123-456-7890",
    "linkedin": "https://www.linkedin.com/in/your-linkedin-profile",
    "github": "https://github.com/your-github-profile",
    "location": "Your City, State",
    "website": "https://your-personal-website.com"
  },
  "summary": "A brief summary of your skills and experience. 2-3 sentences max.",
  "experience": [
    {
      "title": "Job Title",
      "company": "Company Name",
      "location": "City, State",
      "period": "Month Year - Month Year",
      "description": "Bullet points describing your responsibilities and achievements at this position."
    },
    // Add more experience entries as needed
  ],
  "education": [
    {
      "degree": "Degree Name",
      "major": "Major Field",
      "institution": "Institution Name",
      "location": "City, State",
      "graduation_date": "Month Year"
    },
    // Add more education entries as needed
  ],
  "skills": {
    "technical": [
      "Skill 1",
      "Skill 2",
      "Skill 3"
    ],
    "soft": [
      "Soft Skill 1",
      "Soft Skill 2",
      "Soft Skill 3"
    ],
    "languages": [
      "Language 1",
      "Language 2",
      "Language 3"
    ]
  },
  "awards_and_certifications": [
    {
      "name": "Award/Certification Name",
      "awarded_by": "Awarding Organization",
      "date": "Month Year"
    },
    // Add more entries as needed
  ],
  "projects": [
    {
      "name": "Project Name",
      "description": "A brief description of the project and your role."
    },
    // Add more project entries as needed
  ],
  "interests": [
    "Interest 1",
    "Interest 2",
    "Interest 3"
  ],
  "other": {
    "additional_information": "Any other relevant information you want to include, such as publications, volunteer work, or personal achievements."
  }
}
"""

resume=read_resume("/Users/namangandhi/Documents/codes/resumes/testuser1.pdf")

response = model.generate_content(prompt+resume)

print(response.text)
