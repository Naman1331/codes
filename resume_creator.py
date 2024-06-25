from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def create_resume(experience):
    # Create a PDF canvas
    c = canvas.Canvas("resume.pdf", pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(1 * inch, height - 1 * inch, "Resume")

    # Personal Information
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, height - 1.5 * inch, "Name: John Doe")
    c.drawString(1 * inch, height - 1.7 * inch, "Email: johndoe@example.com")
    c.drawString(1 * inch, height - 1.9 * inch, "Phone: (123) 456-7890")

    # Experience Section Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1 * inch, height - 2.5 * inch, "Experience")

    # Experience Details
    y = height - 3 * inch
    for job in experience:
        c.setFont("Helvetica-Bold", 14)
        c.drawString(1 * inch, y, job['title'])
        c.setFont("Helvetica", 12)
        c.drawString(1 * inch, y - 0.2 * inch, f"Company: {job['company']}")
        c.drawString(1 * inch, y - 0.4 * inch, f"Dates: {job['dates']}")
        c.drawString(1 * inch, y - 0.6 * inch, f"Description: {job['description']}")
        y -= 1 * inch

    # Save the PDF
    c.save()

# Example experience data
experience = [
    {
        "title": "Software Engineer",
        "company": "ABC Tech",
        "dates": "Jan 2020 - Present",
        "description": "Worked on developing and maintaining web applications."
    },
    {
        "title": "Junior Developer",
        "company": "XYZ Solutions",
        "dates": "Jun 2018 - Dec 2019",
        "description": "Assisted in the development of internal tools and customer-facing applications."
    }
]

# Create the resume PDF
create_resume(experience)