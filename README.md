# elasticSearch:

hello there 

__Elasticsearch__ is a distributed, free and open search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured.

#steps :
you need to have elasticsearch installed in your pc 

this : https://linuxize.com/post/how-to-install-elasticsearch-on-ubuntu-20-04/ how I have installed it in my ubuntu 20.04 machine 



create new django project and install  django-elasticsearch-dsl
using : 

pip install django-elasticsearch-dsl

___________________________________
#the code :

1\ in __model.py__ you will find the database logic for "Post" model

2\ in __document.py__ here where our index classes are located for poth "Post" and "User" models

3\ in __settings.py__ some settings need to be added :
 add 'django_elasticsearch_dsl' for installed apps 
then add :

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}

4\ in __management\commands\populate_db.py__ here is some code can be run using 
__python manage.py populate_db__
so the database will start with some data


_________________________________________________________________________

#references 
this topic was helpful for me : https://testdriven.io/blog/django-drf-elasticsearch/

