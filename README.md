# django-showcase-quiz

A quiz app showcasing Django.

## Requirements

* Python >=3.6, with `pip`.
* (Optionally) MySQL >=5.6. 

## Setup

1. Install `pip` requirements:
   ```
   $ pip install -r requirements.txt
   ```

2. If you want to use MySQL, create a database and user for the project like this:
   ```sql
   CREATE DATABASE quiz CHARACTER SET utf8;
   CREATE USER 'quiz'@'localhost' IDENTIFIED BY 'qu1z';  -- Weak password, suitable only for testing!
   GRANT ALL ON quiz.* TO 'quiz'@'localhost';
   ```
    And change the `DATABASES` setting in `settings.py` like this:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'quiz',
           'USER': 'quiz',
           'PASSWORD': 'qu1z',  # The password you've set above.
       }
   }
   ```
   In the repository, the engine is set to SQLite, which doesn't require any setup.

3. Run migrations:
   ```
   $ python manage.py migrate
   ```
4. Create superuser:
   ```
   $ python manage.py createsuperuser
   ```
## Usage

Add questions and choices at `/admin` with the superuser.

Take the quiz at `/quiz`.

## Excercises

1. What happens when you visit the `/quiz` page and there are no questions yet? Fix that behavior by returning a 404 
   page.
    
2. Modify the admin so that questions and choices can be handled on one page.

3. Add a constraint allowing only one correct choice per question.

4. Make the order of the questions customizable.
