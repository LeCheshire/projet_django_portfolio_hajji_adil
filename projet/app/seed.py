from django_seed import Seed
from app.models import Member
import random

def run():
    seeder = Seed.seeder()
    image_urls = ['https://media.licdn.com/dms/image/D4D03AQFrCH40mWvKVg/profile-displayphoto-shrink_400_400/0/1676562019324?e=1691020800&v=beta&t=a9jeKEk595EaQVgsI9S-hX4taeGYAy2A-MlF2O-aWiA','https://wwwimage-tve.cbsstatic.com/thumbnails/photos/w425-q80/cast/bigbro17_cast_jeremy.jpg','https://cgbuchalter.com/wp-content/uploads/2020/03/christian-damico-new-bg-400.jpg']
    seeder.add_entity(Member, 1, {
        'quote' : lambda x: seeder.faker.job(),
        'nom' : lambda x: seeder.faker.name(),
        'image_url' : lambda x: image_urls[random.randint(0,2)],
    })
    inserted_pks = seeder.execute()
    print(inserted_pks)
