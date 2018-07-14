import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

#FAKE POP SCRIPT
import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        name= fakegen.name().split()
        fake_firstname = name[0]
        fake_lastname = name[1]
        fake_mail = fakegen.email()
    
        new_user = User.objects.get_or_create(first_name=fake_firstname,last_name=fake_lastname,email=fake_mail)



if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populating complete!")

