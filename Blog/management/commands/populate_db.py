from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from Blog.models import Post
#from core.Blog.models import Post

# here we create new objects and save it  on the databse
class Command(BaseCommand):
    help = 'Populates the database with some testing data.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Started database population process...'))

        # Create users
        rabab5 = User.objects.create_user(username='rabab5', password='really_strong_password123',email='rabab5@gmail.com',)
        rabab5.save()

        rabab3 = User.objects.create_user(username='rabab3', password='really_strong_password123',
                                          email='rabab3@gmail.com', )
        rabab3.save()
        rabab4= User.objects.create_user(username='rabab4', password='really_strong_password123',
                                          email='rabab4@gmail.com', )
        rabab4.save()

        post1 = Post.objects.create(title='post1', content='this is the content of post 1', author=rabab5,slug='slug1', )
        post1.save()


        post3 = Post.objects.create(title='post3', content='this is the content of post 3', author=rabab3,
                                         slug='slug3', )
        post3.save()



        post4 = Post.objects.create(title='post4', content='this is the content of post 4', author=rabab4,
                                         slug='slug4', )
        post4.save()


        self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))
