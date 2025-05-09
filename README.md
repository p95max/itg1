Fun News:
Fun News is a multilingual news website built with Django, featuring a responsive interface, likes, favorites, comments, and content filtering.

Key Features:
Articles: View, add (manually or via JSON), like, favorite, and comment.
Filtering: Search, sort by date/views/likes, filter by tags and categories.
Multilingual: Supports multiple languages with a language switcher.
Interface: Responsive design (Bootstrap), light/dark theme toggle, animations (AOS).
Map: Interactive map on the "About" page (Leaflet).
Interactivity: AJAX for likes and favorites, link copying.

Technologies:
Backend: Django, Python
Frontend: Bootstrap 5, AOS, Leaflet
Templates: Django i18n for multilingual support
Static Files: CSS, favicon

Installation:
Clone the repository:git clone https://github.com/your-repository/fun-news.git
Install dependencies:pip install -r requirements.txt
Configure database and environment variables in settings.py.
Run migrations:python manage.py migrate
Start the server:python manage.py runserver

Test Database included!

Structure:
news/templates/news/: Templates (base, catalog, articles, favorites, about).
news/static/: CSS, images, favicon.
news/: Models, views, forms, URLs.

Requirements:
Python 3.8+
Django 4.0+
PostgreSQL (recommended)

Future Plans:
Add user authentication.
Optimize database queries.


