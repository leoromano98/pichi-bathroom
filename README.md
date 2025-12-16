# Bathroom Tracker

A simple Django app to track bathroom visits.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Run the server:
```bash
python manage.py runserver
```

4. Open your browser to: `http://127.0.0.1:8000/`

## Usage

- Enter the location in the input field
- Click "Add Entry" to record a visit
- The table will refresh and show all visits in reverse chronological order
