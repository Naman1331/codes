import google.generativeai as genai


genai.configure(api_key="AIzaSyCjAgp-L_bmujjt1NulwnLbt4Xk9TUslnc")

# The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)