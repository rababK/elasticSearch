#my own experiance 

in 31 march  I was assigned by Kashta company to create a django project and connect it with elastic search as apart of my internaship

I had no Idea at that time what elasticsearch is , so I start reading and watching vedios about it , by the time I was tring to install it flowing this topic 

https://linuxize.com/post/how-to-install-elasticsearch-on-ubuntu-20-04/


in 3 april it finally work with me 

before that I was gitting this error continucly :

__Job for elasticsearch.service failed because a timeout was exceeded__

and here I found the salution which work for me :

https://blog.sleeplessbeastie.eu/2020/02/29/how-to-prevent-systemd-service-start-operation-from-timing-out/
 now elasticsearch run with no error and I had to connect it to django project 

first I follow up with this topic 

https://testdriven.io/blog/django-drf-elasticsearch/

doing everysingle command litterly wasn,t the best Idea to learn so I delete every thing and try to re write what I learn with simple "post" model.


in 8 april I start doing some improvements to the code adding  the django "User" model to documents,

what I didn,t understand with the above tobic is to populate the database I never use this before 
after doing some research it was really reasonable for me ,

I end up with some simple code in __commands.py__ file .

now every thing finally  work !


elasticsearch is still mistry for me , although using commands in console whith queries and search method give a good response at the real time but elasticsearch could be more useful I think,

next step I intend to do some work with views ,

and to read more about using __elasticsearch__
