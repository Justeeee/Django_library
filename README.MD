# Django-Library

This BACKEND API for online libraries

It currently doesn't allow to add photo of book and ratings.
Solely, it's expected to be used on a single machine or online for managers only.


username: admin
password: 1
```


Run

```python
pip install -r requirements.txt #install required packages
python manage.py migrate # run first migration
python manage.py runserver # run the server
```
Then locate http://172.0.0.1:8000

## Admin Login
When you run migrate, a superuser is created.
```bash
username: admin
password: 1
```
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

