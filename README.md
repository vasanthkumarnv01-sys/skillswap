# SkillSwap — Student Skill Exchange Platform

SkillSwap is a Django web application for a student skill-exchange project. The repository is organized into separate apps for accounts, skills, and swaps.

## Tech Stack
- Python
- Django
- HTML, CSS, and JavaScript templates
- SQLite for local development

## Project Areas
- `accounts/` — account-related functionality
- `skills/` — skill-related functionality
- `swaps/` — skill-exchange functionality
- `templates/` and `static/` — presentation assets

## Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/vasanthkumarnv01-sys/skillswap.git
   cd skillswap
   ```
2. Create and activate a Python virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirement.txt
   ```
4. Apply migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Author
Vasanth Kumar

> Review the project locally and add screenshots or confirmed feature details before using this README as a complete project demo.
