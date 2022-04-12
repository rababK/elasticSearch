from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Post

''' here where we create indexes for both Post model from Models file and User model from django 
   
   we need to import registry to register new document 
   , document to define new one and fields to work with special fields such as foreign key one
   
'''

# for User : register new document
@registry.register_document
class UserDocument(Document):
    # which contain tow classes

    # the first for index
    class Index:
        # index name should be with lower case only
        name = 'users'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    # and the second for django

    class Django:
        model = User
        fields = [
            'id',
            'username',
            'email',

        ]

 # same for Post model

@registry.register_document
class PostDocument(Document):
    # that is how we index the foreign key
    author = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'username': fields.TextField(),
        'email': fields.TextField(),


    })
    class Index:
        name = 'posts'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Post
        fields = [
            'id',
            'status',
            'title',
            'slug',
            'content',
            'created_on',
            'updated_on'
        ]


