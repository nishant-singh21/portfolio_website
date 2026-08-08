"""Generate the resume PDF and a placeholder profile avatar.

This is a development-only script (reportlab is NOT a runtime dependency).
It regenerates the committed static assets:

    portfolio/static/portfolio/resume/Nishant_Singh_Resume.pdf
    portfolio/static/portfolio/img/profile.jpg

Run from the project root:  python scripts/generate_assets.py
"""
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

CONTACT = {
    'email': 'Nishantsingh1721@gmail.com',
    'phone': '+91 73071 74395',
    'linkedin': 'linkedin.com/in/nishant-singh-137869275',
    'github': 'github.com/nishant-singh21',
}

SKILLS = [
    ('Backend', 'Python, Django, Django REST Framework, Django ORM, REST API Development'),
    ('Frontend', 'HTML5, CSS3, JavaScript, Bootstrap, Materialize CSS'),
    ('Database', 'MySQL'),
    ('Infrastructure', 'Redis, Celery'),
    ('Tools', 'Git, GitHub, Postman, VS Code'),
    ('Other', 'Debugging & Optimization, Teamwork & Communication'),
]

EXPERIENCE = [
    (
        'Software Developer Intern',
        'INTERNPE.in · July 2023 - August 2023',
        [
            'Built and deployed 10+ responsive web pages using HTML, CSS, JavaScript, and Bootstrap.',
            'Debugged and optimized cross-browser rendering and page-load performance.',
            'Designed relational database schemas that reduced data retrieval time by an estimated 30% in prototype applications.',
            'Collaborated with designers and senior developers to keep deliverables on schedule.',
        ],
    ),
]

PROJECTS = [
    (
        'AI Moderation Microservice',
        'Django, Django REST Framework, Celery, Redis',
        [
            'Django microservice using LLM-based classification to detect and flag unsafe text and image content',
            'REST API endpoints for low-latency moderation checks',
            'Celery + Redis asynchronous background processing',
            'Real-time Slack and email alerts; hybrid rule-based + LLM scoring pipeline',
            'Configurable confidence thresholds; false-positive reduction and threshold tuning',
        ],
    ),
    (
        'Product Recommendation Engine',
        'Python, Django ORM, NLP, TF-IDF, Cosine Similarity',
        [
            'Content-based recommendation engine using NLP, TF-IDF vectorization and cosine similarity',
            'Cold-start fallback logic; Django ORM and REST API integration',
        ],
    ),
    (
        'Polling Application',
        'Python, Django, HTML, CSS, Materialize CSS',
        [
            'Secure authenticated access with session-based user tracking',
            'One-vote-per-user enforcement and duplicate-vote protection',
            'Normalized database schemas with real-time result aggregation',
        ],
    ),
    (
        'My Shop - E-Commerce Platform',
        'Python, Django ORM, HTML, CSS, JavaScript',
        [
            'Category-based product filtering, shopping cart and order tracking',
            'Product and inventory management with scalable catalog structure',
            'Django ORM-based database models',
        ],
    ),
]

EDUCATION = [
    ('B.Tech - Computer Science & Engineering', 'GN Group of Colleges, Greater Noida', '2022 - 2026'),
    ('Higher Secondary (XII)', 'Kendriya Vidyalaya, Sonebhadra, U.P.', '2021 - 2022'),
    ('Secondary (X)', 'Kendriya Vidyalaya, Sonebhadra, U.P.', '2019 - 2020'),
]

ACHIEVEMENTS = [
    '14+ public GitHub repositories covering Django APIs, recommendation systems and microservices',
    'AI/ML Certification - GeeksforGeeks (GFG)',
]


def generate_resume_pdf():
    try:
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.lib.units import mm
        from reportlab.platypus import (
            HRFlowable,
            ListFlowable,
            ListItem,
            Paragraph,
            SimpleDocTemplate,
            Spacer,
        )
    except ImportError as exc:
        raise SystemExit(
            'reportlab is required for the generator. Install it with: '
            'pip install reportlab'
        ) from exc

    INK = colors.HexColor('#0f172a')
    MUTED = colors.HexColor('#475569')
    ACCENT = colors.HexColor('#0891b2')

    styles = {
        'name': ParagraphStyle(
            'name', fontName='Helvetica-Bold', fontSize=22, leading=26,
            textColor=INK, spaceAfter=2,
        ),
        'role': ParagraphStyle(
            'role', fontName='Helvetica', fontSize=11, leading=15,
            textColor=ACCENT, spaceAfter=6,
        ),
        'contact': ParagraphStyle(
            'contact', fontName='Helvetica', fontSize=8.5, leading=13,
            textColor=MUTED,
        ),
        'h2': ParagraphStyle(
            'h2', fontName='Helvetica-Bold', fontSize=11.5, leading=15,
            textColor=INK, spaceBefore=8, spaceAfter=3,
        ),
        'body': ParagraphStyle(
            'body', fontName='Helvetica', fontSize=9.5, leading=13.5,
            textColor=MUTED, spaceAfter=2,
        ),
        'entry_title': ParagraphStyle(
            'entry_title', fontName='Helvetica-Bold', fontSize=10, leading=14,
            textColor=INK, spaceBefore=3,
        ),
        'entry_sub': ParagraphStyle(
            'entry_sub', fontName='Helvetica-Oblique', fontSize=9, leading=13,
            textColor=ACCENT, spaceAfter=2,
        ),
    }

    def bullet(items):
        return ListFlowable(
            [
                ListItem(Paragraph(item, styles['body']), leftIndent=14, value='•')
                for item in items
            ],
            bulletType='bullet',
            start='•',
            leftIndent=12,
        )

    doc = SimpleDocTemplate(
        str(PROJECT_ROOT / 'portfolio' / 'static' / 'portfolio' / 'resume' / 'Nishant_Singh_Resume.pdf'),
        pagesize=A4,
        rightMargin=16 * mm,
        leftMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
        title='Nishant Singh - Backend Developer Resume',
        author='Nishant Singh',
    )

    story = [
        Paragraph('Nishant Singh', styles['name']),
        Paragraph('Backend Developer · Python &amp; Django Specialist', styles['role']),
        Paragraph(
            f"Email: {CONTACT['email']} &nbsp;|&nbsp; Phone: {CONTACT['phone']} "
            f"&nbsp;|&nbsp; LinkedIn: {CONTACT['linkedin']} "
            f"&nbsp;|&nbsp; GitHub: {CONTACT['github']}",
            styles['contact'],
        ),
        Spacer(1, 4),
        HRFlowable(width='100%', thickness=1.1, color=ACCENT),
        Paragraph('SUMMARY', styles['h2']),
        Paragraph(
            'Backend Developer with hands-on experience building scalable REST APIs and '
            'microservices using Python, Django and Django REST Framework. Comfortable with '
            'HTML and CSS for frontend integration and debugging, with experience in '
            'asynchronous task processing using Celery and Redis, database design using MySQL, '
            'debugging, optimization, teamwork and communication.',
            styles['body'],
        ),
        Paragraph('SKILLS', styles['h2']),
        bullet([f'<b>{name}:</b> {items}' for name, items in SKILLS]),
        Paragraph('EXPERIENCE', styles['h2']),
        Paragraph('Software Developer Intern - INTERNPE.in', styles['entry_title']),
        Paragraph('July 2023 - August 2023', styles['entry_sub']),
        bullet(EXPERIENCE[0][2]),
        Paragraph('PROJECTS', styles['h2']),
    ]

    for title, tech, items in PROJECTS:
        story.append(Paragraph(title, styles['entry_title']))
        story.append(Paragraph(tech, styles['entry_sub']))
        story.append(bullet(items))

    story.append(Paragraph('EDUCATION', styles['h2']))
    for degree, institution, period in EDUCATION:
        story.append(Paragraph(f'<b>{degree}</b> — {institution} ({period})', styles['body']))

    story.append(Paragraph('ACHIEVEMENTS', styles['h2']))
    story.append(bullet(ACHIEVEMENTS))

    doc.build(story)
    print('Generated resume PDF.')


def generate_avatar():
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        raise SystemExit('Pillow is required. Install with: pip install Pillow')

    size = 600
    img = Image.new('RGB', (size, size))
    draw = ImageDraw.Draw(img)

    top = (34, 211, 238)
    bottom = (139, 92, 246)
    for y in range(size):
        t = y / (size - 1)
        draw.line(
            [(0, y), (size, y)],
            fill=tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)),
        )

    circle = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    ImageDraw.Draw(circle).ellipse((40, 40, size - 40, size - 40), fill=(10, 14, 23, 255))
    img.paste(circle, (0, 0), circle)

    initials = 'NS'
    font_size = 210
    try:
        font = ImageFont.truetype('arialbd.ttf', font_size)
    except OSError:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), initials, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text(
        ((size - w) / 2 - bbox[0], (size - h) / 2 - bbox[1]),
        initials,
        font=font,
        fill=(226, 237, 246, 255),
    )

    out = PROJECT_ROOT / 'portfolio' / 'static' / 'portfolio' / 'img' / 'profile.jpg'
    img.save(out, 'JPEG', quality=92)
    print('Generated placeholder avatar.')


if __name__ == '__main__':
    generate_avatar()
    generate_resume_pdf()
