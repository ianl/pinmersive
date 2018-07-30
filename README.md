# Pinmersive

### A simplified Pinterest clone

## Installation

1.  Install dependencies:

```
cd pinmersive
pipenv install
```

2.  Run server on http://localhost:8000

```
pipenv shell
python manage.py runserver
```

3.  On login page, click on `Sign in as Guest`

## Key Features

- Pinterest style layout
- Able to save Pin via image urls / image files from device / re-pinning existing Pins
- Able to search for Pins
- Able to create Secret Boards
- Able to follow individual User Profiles or Boards
- `urls.py` closely modelled on Pinterest's routes
- Largely avoids N+1 queries using `select_related()` and `prefetch_related()`

## Technology

Pinmersive uses:

- [Django](https://github.com/django/django)
- SQLite (development) / PostgreSQL (production)
- [Bootstrap 3](https://github.com/twbs/bootstrap)
- [jQuery](https://github.com/jquery/jquery)
- [Isotope](https://github.com/metafizzy/isotope)

## Future TODOs

- Add Infinite Scroll to home feed
- Add Pin comments functionality
- Add Pin recommendations functionality
