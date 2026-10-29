# New Portfolio Project: SkillSwap Pro

A major upgrade to the existing SkillSwap repository is available as a separate downloadable project package in this chat: `skillswap-pro.zip`.

## Included
- Django account registration, login/logout, and public member profiles
- Skill listings with categories, tags, skill levels, and search/filter
- Exchange request workflow: send, accept, decline, cancel, complete
- Member dashboard, incoming requests, and listing status controls
- Responsive HTML/CSS/JavaScript frontend
- Django admin registrations and starter automated tests
- GitHub Actions workflow for basic checks
- Setup, security, and project documentation

## Local setup
1. Extract the project ZIP.
2. Create and activate a Python virtual environment.
3. Install dependencies with `pip install -r requirements.txt`.
4. Run `python manage.py makemigrations accounts skills swaps`.
5. Run `python manage.py migrate`.
6. Run `python manage.py createsuperuser`.
7. Run `python manage.py runserver`.

Note: This is a Django learning project scaffold. Install the dependencies and run migrations/tests locally before deploying. The code package is not automatically the same as this existing repository's complete code.
