"""Generate a professional resume PDF for Tauqeer Alam."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable
)

OUT_DIR = r"E:/MySelf/Portfolios/media/resume"
os.makedirs(OUT_DIR, exist_ok=True)
PDF_PATH = os.path.join(OUT_DIR, "Tauqeer_Alam_Resume.pdf")

# Colours
ACCENT  = HexColor("#0e6ba8")
DARK    = HexColor("#14213d")
SEC     = HexColor("#526078")

doc = SimpleDocTemplate(
    PDF_PATH, pagesize=A4,
    leftMargin=0.75 * inch, rightMargin=0.75 * inch,
    topMargin=0.6 * inch, bottomMargin=0.6 * inch,
    title="Tauqeer Alam - Resume", author="Tauqeer Alam",
)

# Styles
name_s   = ParagraphStyle("nm", fontSize=26, leading=30, textColor=DARK,
                          alignment=TA_LEFT, spaceAfter=2, fontName="Helvetica-Bold")
title_s  = ParagraphStyle("ti", fontSize=13, leading=16, textColor=ACCENT,
                          alignment=TA_LEFT, spaceAfter=4, fontName="Helvetica-Bold")
loc_s    = ParagraphStyle("lc", fontSize=9, leading=12, textColor=SEC,
                          alignment=TA_LEFT, spaceAfter=10, fontName="Helvetica")
h2_s     = ParagraphStyle("h2", fontSize=14, leading=18, textColor=ACCENT,
                          alignment=TA_LEFT, spaceBefore=14, spaceAfter=6, fontName="Helvetica-Bold")
h3_s     = ParagraphStyle("h3", fontSize=11, leading=14, textColor=DARK,
                          alignment=TA_LEFT, spaceBefore=8, spaceAfter=2, fontName="Helvetica-Bold")
sub_s    = ParagraphStyle("sub", fontSize=9.5, leading=12, textColor=SEC,
                          alignment=TA_LEFT, spaceAfter=1, fontName="Helvetica-Oblique")
body_s   = ParagraphStyle("bd", fontSize=9.5, leading=13.5, textColor=DARK,
                          alignment=TA_JUSTIFY, spaceAfter=5, fontName="Helvetica")
bul_s    = ParagraphStyle("bu", fontSize=9.5, leading=13, textColor=DARK,
                          alignment=TA_LEFT, leftIndent=14, bulletIndent=4,
                          spaceBefore=1, spaceAfter=1.5, fontName="Helvetica")

story = []

# ── Header ──
story.append(Paragraph("TAUQEER ALAM", name_s))
story.append(Paragraph("Python Full Stack Developer", title_s))
story.append(Paragraph(
    "Bengaluru, Karnataka | https://github.com/alam7401 | 7079906220 | 7856025404 | tauqeeralam7401@gmail.com",
    loc_s))
story.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceBefore=2, spaceAfter=6))

# ── Summary ──
story.append(Paragraph("PROFESSIONAL SUMMARY", h2_s))
story.append(Paragraph(
    "Motivated and detail-oriented Python Full Stack Developer with hands-on experience in building web "
    "applications using Django, HTML, CSS, and JavaScript. Strong understanding of backend development, "
    "database management, and REST APIs. Passionate about solving real-world problems and building scalable applications.",
    body_s))

# ── Projects ──
story.append(Paragraph("PROJECTS", h2_s))

story.append(Paragraph("Online Exam Management System", h3_s))
story.append(Paragraph("Python / Django | HTML, CSS, JavaScript | SQLite | Deployed on Render", sub_s))
story.append(Paragraph(
    "Developed a full-stack Online Exam Management System using Python/Django with multi-role authentication "
    "(Admin, Teacher, Student), MCQ-based timed exams with AJAX auto-grading, automated result generation, "
    "and a responsive dark-themed UI.", body_s))
story.append(Paragraph("• Multi-role authentication (Admin, Teacher, Student)", bul_s))
story.append(Paragraph("• MCQ-based timed exams with AJAX auto-grading", bul_s))
story.append(Paragraph("• Automated result generation &amp; responsive dark-themed UI", bul_s))
story.append(Spacer(1, 6))

story.append(Paragraph("Exam Seating Management System", h3_s))
story.append(Paragraph("Python / Django | PDF Generation", sub_s))
story.append(Paragraph(
    "Built an Exam Seating Arrangement System using Python/Django that automates student seat allocation "
    "across multiple halls with branch-mixing logic to prevent cheating, generates printable PDF seating "
    "charts, and reduced manual arrangement time from hours to seconds for 500+ student batches.", body_s))
story.append(Paragraph("• Automated seat allocation with branch-mixing to prevent cheating", bul_s))
story.append(Paragraph("• Printable PDF seating charts for 500+ student batches", bul_s))
story.append(Paragraph("• Reduced manual arrangement time from hours to seconds", bul_s))
story.append(Spacer(1, 6))

# ── Experience ──
story.append(Paragraph("EXPERIENCE", h2_s))

story.append(Paragraph("Python Full Stack Trainee", h3_s))
story.append(Paragraph("QSpiders | Bengaluru, Karnataka | Jan 2026 – Jan 2027", sub_s))
story.append(Paragraph("• Pursuing training in Python Full Stack Development", bul_s))
story.append(Paragraph("• Learned frontend technologies: HTML, CSS, JavaScript", bul_s))
story.append(Paragraph("• Worked on backend development using Django framework", bul_s))
story.append(Paragraph("• Gained knowledge of databases (SQL, MySQL)", bul_s))
story.append(Spacer(1, 6))

story.append(Paragraph("Web Development Intern", h3_s))
story.append(Paragraph("Novem Controls Pvt. Ltd | Mohali, Chandigarh | June 2024 – July 2024", sub_s))
story.append(Paragraph("• Completed a 45-day Web Development internship", bul_s))
story.append(Paragraph("• Gained hands-on experience in full-stack development using HTML5, CSS3, JavaScript, Python, Django", bul_s))
story.append(Paragraph("• Built responsive web applications", bul_s))
story.append(Spacer(1, 6))

# ── Education ──
story.append(Paragraph("EDUCATION", h2_s))

edu = [
    ("I.K. Gujral Punjab Technical University", "B.Tech in Computer Science | 2022–2026 | CGPA: 7.42"),
    ("Millat College Darbhanga", "Intermediate (12th) | 2020–2022"),
    ("Shafi Muslim High School Darbhanga", "Matriculation (10th) | 2019–2020"),
]
for inst, det in edu:
    story.append(Paragraph(inst, h3_s))
    story.append(Paragraph(det, body_s))
    story.append(Spacer(1, 3))

# ── Skills ──
story.append(Paragraph("SKILLS", h2_s))
for s in [
    "Programming: Python, C, C++",
    "Frontend: HTML, CSS, JavaScript",
    "Backend: Django",
    "Database: SQL (SQLite / MySQL)",
    "API: Basic REST API Development",
    "Other: Debugging &amp; Problem Solving",
]:
    story.append(Paragraph(f"• {s}", bul_s))

doc.build(story)
print(f"PDF generated: {PDF_PATH}")
print(f"Size: {os.path.getsize(PDF_PATH)} bytes")
