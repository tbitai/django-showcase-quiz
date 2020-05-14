# django-showcase-quiz

A quiz app showcasing Django.

## Requirements

* Python >=3.6, with `pip`.
* (Optionally) MySQL >=5.6. Create a database and user for the project like this:
  ```sql
  CREATE DATABASE quiz CHARACTER SET utf8;
  CREATE USER 'quiz'@'localhost' IDENTIFIED BY 'qu1z';  -- Weak password, suitable only for testing!
  GRANT ALL ON quiz.* TO 'quiz'@'localhost';
  ```
   Change the `DATABASES` setting in `settings.py` like this:
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