![Contact Board Banner Image](/blog/static/blog/images/githeader.png)
<h2 align='center'>Cactus Garden Blog</h2>

This project is a functional web applicaction in Python and Django. This project has two applicactions. The first one is an site setup where we can create and manage a pages, posts, tags, and categor, update and/or delete them. There is also the blog frontend. 

This project was created following the project Blog of the Udemy couse Curso de Python 3 do básico ao avançado - com projetos reais.

### Blog Main Page
![Contact Board main Image](/blog/static/blog/images/blog.png)

### Usage

1. After cloning this repository, create a virtual environment and install the requirements listed in the 'requirements.txt' file:

```
pip install -r requirements.txt
```

2. In the file setting.py, configure the database settings.
3. Execute below commands:

```
python manage.py makemigrations
python manage.py migrate
```

4. Create superuser for admin access and follow instructions:

```
python manage.py createsuperuser
```

5. Running the tests

```
python manage.py runserver
```

### Tools
+ Django
+ Laragon
+ MySQL
+ Python
+ Html
+ Css
