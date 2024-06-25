from pyresparser import ResumeParser
data = ResumeParser('/Users/namangandhi/Documents/codes/resumes/testuser1.pdf').get_extracted_data()
print(data)