from django.shortcuts import redirect, render

from .forms import ContactForm

CONTACT = {
    'email': 'Nishantsingh1721@gmail.com',
    'phone': '+91 73071 74395',
    'phone_link': '+917307174395',
    'linkedin': 'https://www.linkedin.com/in/nishant-singh-137869275',
    'github': 'https://github.com/nishant-singh21',
}

SKILL_GROUPS = [
    {
        'title': 'Backend',
        'icon': 'server',
        'skills': ['Python', 'Django', 'Django REST Framework', 'Django ORM', 'REST API Development'],
    },
    {
        'title': 'Programming',
        'icon': 'code',
        'skills': ['JavaScript', 'Debugging', 'Optimization'],
    },
    {
        'title': 'Frontend',
        'icon': 'layout',
        'skills': ['HTML5', 'CSS3', 'Bootstrap', 'Materialize CSS'],
    },
    {
        'title': 'Database',
        'icon': 'database',
        'skills': ['MySQL'],
    },
    {
        'title': 'Infrastructure',
        'icon': 'infra',
        'skills': ['Redis', 'Celery'],
    },
    {
        'title': 'Tools',
        'icon': 'tools',
        'skills': ['Git', 'GitHub', 'Postman', 'VS Code'],
    },
]

EXPERIENCE = [
    {
        'company': 'INTERNPE.in',
        'role': 'Software Developer Intern',
        'period': 'July 2023 - August 2023',
        'points': [
            'Built and deployed 10+ responsive web pages using HTML, CSS, JavaScript, and Bootstrap.',
            'Debugged and optimized cross-browser rendering and page-load performance.',
            'Designed relational database schemas that reduced data retrieval time by an estimated 30% in prototype applications.',
            'Collaborated with designers and senior developers to keep deliverables on schedule.',
        ],
    },
]

PROJECTS = [
    {
        'name': 'AI Moderation Microservice',
        'description': 'Architected a Django microservice using LLM-based classification to automatically detect and flag unsafe text and image content across multiple content categories.',
        'technologies': ['Django', 'Django REST Framework', 'Celery', 'Redis', 'LLM'],
        'features': [
            'Django-based microservice architecture',
            'REST API endpoints for low-latency moderation checks',
            'Celery + Redis for asynchronous background processing',
            'Real-time Slack and email alerts',
            'Hybrid rule-based + LLM scoring pipeline',
            'Configurable confidence thresholds',
            'False-positive reduction and threshold tuning',
        ],
        'icon': 'shield',
        'accent': 'cyan',
    },
    {
        'name': 'Product Recommendation Engine',
        'description': 'Built a real-time recommendation engine that uses NLP, TF-IDF vectorization, and cosine similarity to provide personalized product recommendations.',
        'technologies': ['Python', 'Django ORM', 'NLP', 'TF-IDF', 'Cosine Similarity'],
        'features': [
            'Content-based recommendation system',
            'TF-IDF vectorization',
            'Cosine similarity',
            'Cold-start fallback logic',
            'Django ORM integration',
            'REST API integration',
        ],
        'icon': 'spark',
        'accent': 'violet',
    },
    {
        'name': 'Polling Application',
        'description': 'A secure Django polling app with authenticated access, session tracking and duplicate-vote protection.',
        'technologies': ['Python', 'Django', 'HTML', 'CSS', 'Materialize CSS'],
        'features': [
            'Secure authenticated access',
            'Session-based user tracking',
            'One-vote-per-user enforcement',
            'Normalized database schemas',
            'Real-time result aggregation',
            'Protection against duplicate voting',
        ],
        'icon': 'chart',
        'accent': 'green',
    },
    {
        'name': 'My Shop - E-Commerce Platform',
        'description': 'A Django-based e-commerce platform with product catalog, cart, order tracking and inventory management.',
        'technologies': ['Python', 'Django ORM', 'HTML', 'CSS', 'JavaScript'],
        'features': [
            'Category-based product filtering',
            'Shopping cart management',
            'Order tracking',
            'Product and inventory management',
            'Django ORM-based database models',
            'Scalable product catalog structure',
        ],
        'icon': 'cart',
        'accent': 'amber',
    },
]

EDUCATION = [
    {
        'institution': 'GN Group of Colleges, Greater Noida',
        'degree': 'B.Tech - Computer Science & Engineering',
        'period': '2022 - 2026',
    },
    {
        'institution': 'Kendriya Vidyalaya, Sonebhadra, U.P.',
        'degree': 'Higher Secondary (XII)',
        'period': '2021 - 2022',
    },
    {
        'institution': 'Kendriya Vidyalaya, Sonebhadra, U.P.',
        'degree': 'Secondary (X)',
        'period': '2019 - 2020',
    },
]

ACHIEVEMENTS = [
    {
        'title': '14+ Public GitHub Repositories',
        'description': 'A growing open-source portfolio covering Django APIs, recommendation systems and microservices.',
        'icon': 'git',
    },
    {
        'title': 'AI/ML Certification - GeeksforGeeks',
        'description': 'Certified in core Artificial Intelligence and Machine Learning concepts.',
        'icon': 'cert',
    },
]

HERO_TAGS = ['Python', 'Django', 'DRF', 'Celery', 'Redis', 'MySQL', 'REST API']


def home(request):
    form = ContactForm()
    return render(request, 'portfolio/home.html', {
        'active_nav': 'home',
        'contact': CONTACT,
        'skill_groups': SKILL_GROUPS,
        'experience': EXPERIENCE,
        'projects': PROJECTS,
        'education': EDUCATION,
        'achievements': ACHIEVEMENTS,
        'hero_tags': HERO_TAGS,
        'form': form,
    })


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # Email/notification delivery is intentionally not wired to an external
        # SMTP server. The submitted data is logged to the server console via
        # the console email backend configured in settings.
        from django.core.mail import send_mail
        send_mail(
            subject=form.cleaned_data['subject'],
            message=(
                f"From: {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n"
                f"{form.cleaned_data['message']}"
            ),
            from_email=form.cleaned_data['email'],
            recipient_list=[CONTACT['email']],
            fail_silently=True,
        )
        return redirect('/#contact?sent=1')
    return render(request, 'portfolio/home.html', {
        'active_nav': 'contact',
        'contact': CONTACT,
        'skill_groups': SKILL_GROUPS,
        'experience': EXPERIENCE,
        'projects': PROJECTS,
        'education': EDUCATION,
        'achievements': ACHIEVEMENTS,
        'hero_tags': HERO_TAGS,
        'form': form,
    })
