from app.models import db, Pet_Profile, Breed_Image, Breed
from faker import Faker
from random import randint, random, randrange

# get_breeds = 
# breeds = {'breeds': [breed.to_dict() for breed in get_breeds]}
# print(Breed.query.all())

breeds = [
    {'img': 'https://geniusvets.s3.amazonaws.com/gv-dog-breeds/labrador-retriever-1.jpg', 
    'name': 'Labrador Retriever'},
    {'img': 'https://images.pexels.com/photos/4587998/pexels-photo-4587998.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260', 
     'name': 'French Bulldog'},
    {'img': 'https://images.pexels.com/photos/2873382/pexels-photo-2873382.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500',
     'name': 'German Shepherd Dog'},
    {'img': 'https://images.pexels.com/photos/686094/pexels-photo-686094.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500',
     'name': 'Golden Retriever'},
    {'img': 'https://www.veterinarypracticenews.com/wp-content/uploads/2021/02/SA_Bulldogs.jpg',
     'name': 'Bulldog'},
    {'img': 'https://i.pinimg.com/736x/79/56/2a/79562af7c3e7f3363d14d0b157697278.jpg',
     'name': 'Standard Poodle'},
    {'img': 'https://www.thesprucepets.com/thmb/WxVsARRPU_8Wx8iS3iqDxP3_iK4=/3881x2911/smart/filters:no_upscale()/beagle-RolfKopfle-Photolibrary-Getty-135631212-56a26b1d3df78cf772756667.jpg',
     'name': 'Beagle'},
    {'img': 'https://vetstreet.brightspotcdn.com/dims4/default/419926a/2147483647/crop/0x0%2B0%2B0/resize/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2Fbf%2F33d570a7fb11e0a0d50050568d634f%2Ffile%2FRottweiler-3-645mk062811.jpg',
     'name': 'Rottweiler'},
    {'img': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F08%2F16%2Fgerman-shorthaired-pointer-bird-in-mouth-613909636-2000.jpg',
     'name': 'German Shorthaired Pointer'},
    {'img': 'https://www.petfirst.com/wp-content/uploads/2018/03/Breed-Hero-Dachshund-1200x1200.jpg',
     'name': 'Dachshund'},
    {'img': 'https://www.trendingbreeds.com/wp-content/uploads/2020/02/Alert-Cane-Corso.jpg',
     'name': 'Cane Corso'},
    {'img': 'https://i.pinimg.com/236x/65/fb/82/65fb82e8e4edd4c3273544de3ee565e8--dog-breeds-american-staffordshire-terriers.jpg',
     'name': 'American Staffordshire Terrier'},
    {'img': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Male_fawn_Boxer_undocked.jpg/1200px-Male_fawn_Boxer_undocked.jpg',
     'name': 'Boxer'},
    {'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7-RTwNHxoTKPZ1tgbUVp8yQC2KW8Jd6OhqA&usqp=CAU',
     'name': 'Pug'},
    {'img': 'https://image.jimcdn.com/app/cms/image/transf/none/path/s53b36d06bb1bc5e5/image/iea74cdb9a08eab13/version/1620740965/image.jpg',
     'name': 'Akita'},
    {'img': 'https://i.pinimg.com/originals/e5/8d/43/e58d43e8bbfe3713b5e039a084ec9663.jpg',
     'name': 'Siberian Husky'},
    {'img': 'https://i.pinimg.com/originals/c7/57/1e/c7571e5e2d08db5f781fc27cd0afe1e6.jpg',
     'name': 'American Bully'},
    {'img': 'https://hellobark.com/wp-content/uploads/corgi-1200.jpg',
     'name': 'Pembroke Welsh Corgi'},
    {'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeCxL4mtfGDSpVM7UN31W4SLrglGYabUuzSbwMji-dG5Lr4ELc2rNPLHRnVN5a8ME4tcs&usqp=CAU',
     'name': 'Cocker Spaniel'},
    {'img': 'https://images-ra.adoptapet.com/seo/1/ff/30_ff.jpg',
     'name': 'Bullmastiff'},
     
          
    ]


def seed_pet_profiles():
    fake = Faker()
    callie = Pet_Profile(
        owner_id=1,
        profile_img='https://images.pexels.com/photos/2679612/pexels-photo-2679612.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        name='Callie',
        breed='Dachshund',
        age='1 year',
        description='Callie loves long walks on the beach and chasing flies. She is fierce, even though she is afraid of her own farts.'
    )

    db.session.add(callie)

    for i in range(1, 35):
        num = randrange(1, 20)
        i = Pet_Profile(
            owner_id=randrange(1, 16),
            profile_img=breeds[num]['img'],
            name=fake.name(),
            breed=breeds[num]['name'],
            age=randrange(1, 16),
            description=fake.paragraph()
        )

        db.session.add(i)

    db.session.commit()

def undo_pet_profiles():
    db.session.execute('TRUNCATE pet_profiles RESTART IDENTITY CASCADE;')
    db.session.commit()
