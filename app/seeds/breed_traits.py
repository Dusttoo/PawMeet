from app.models import db, Breed_Trait

def seed_breed_traits():
     family = Breed_Trait(
        trait='Affectionate with family',
        description='How affectionate a breed is likely to be with family members, or other people he knows well. Some breeds can be aloof with everyone but their owner, while other breeds treat everyone they know like their best friend.',
     )
     children = Breed_Trait(
         trait='Good with young children',
         description="A breed's level of tolerance and patience with childrens' behavior, and overall family-friendly nature. Dogs should always be supervised around young children, or children of any age who have little exposure to dogs.",
     )
     dogs = Breed_Trait(
         trait='Good with other dogs',
         description="How generally friendly a breed is towards other dogs. Dogs should always be supervised for interactions and introductions with other dogs, but some breeds are innately more likely to get along with other dogs, both at home and in public.",
     )
     shed = Breed_Trait(
         trait="Shedding level",
         description="How much fur and hair you can expect the breed to leave behind. Breeds with high shedding will need to be brushed more frequently, are more likely to trigger certain types of allergies, and are more likely to require more consistent vacuuming and lint-rolling.",
     )
     grooming = Breed_Trait(
         trait="Coat grooming frequency",
         description="How frequently a breed requires bathing, brushing, trimming, or other kinds of coat maintenance. Consider how much time, patience, and budget you have for this type of care when looking at the grooming effort needed. All breeds require regular nail trimming.",
     )
     drool = Breed_Trait(
         trait="Drooling Level",
         description="How drool-prone a breed tends to be. If you're a neat freak, dogs that can leave ropes of slobber on your arm or big wet spots on your clothes may not be the right choice for you.",
     )
     coatType = Breed_Trait(
         trait="Coat Type",
         description="Canine coats come in many different types, depending on the breed's purpose. Each coat type comes with different grooming needs, allergen potential, and shedding level. You may also just prefer the look or feel of certain coat types over others when choosing a family pet.",
     )
     coatLength = Breed_Trait(
         trait="Coat Length",
         description="How long the breed's coat is expected to be. Some long-haired breeds can be trimmed short, but this will require additional upkeep to maintain.",
     )
     strangers = Breed_Trait(
         trait="Openness to strangers",
         description="How welcoming a breed is likely to be towards strangers. Some breeds will be reserved or cautious around all strangers, regardless of the location, while other breeds will be happy to meet a new human whenever one is around!",
     )
     playfulness = Breed_Trait(
         trait="Playfulness level",
         description="How enthusiastic about play a breed is likely to be, even past the age of puppyhood. Some breeds will continue wanting to play tug-of-war or fetch well into their adult years, while others will be happy to just relax on the couch with you most of the time.",
     )
     protective = Breed_Trait(
         trait="Watchdog/Protective Nature",
         description="A breed's tendency to alert you that strangers are around. These breeds are more likely to react to any potential threat, whether it's the mailman or a squirrel outside the window. These breeds are likely to warm to strangers who enter the house and are accepted by their family",
     )
     adaptability = Breed_Trait(
         trait="Adaptability level",
         description="How easily a breed handles change. This can include changes in living conditions, noise, weather, daily schedule, and other variations in day-to-day life.",
     )
     trainability = Breed_Trait(
         trait="Trainability level",
         description="How easy it will be to train your dog, and how willing your dog will be to learn new things. Some breeds just want to make their owner proud, while others prefer to do what they want, when they want to, wherever they want!",
     )
     energy = Breed_Trait(
         trait="Energy level",
         description="The amount of exercise and mental stimulation a breed needs. High energy breeds are ready to go and eager for their next adventure. They'll spend their time running, jumping, and playing throughout the day. Low energy breeds are like couch potatoes - they're happy to simply lay around and snooze.",
     )
     barking = Breed_Trait(
         trait="Barking Level",
         description="How often this breed vocalizes, whether it's with barks or howls. While some breeds will bark at every passer-by or bird in the window, others will only bark in particular situations. Some barkless breeds can still be vocal, using other sounds to express themselves.",
     )
     mentalStim = Breed_Trait(
         trait="Mental stimulation needs",
         description="How much mental stimulation a breed needs to stay happy and healthy. Purpose-bred dogs can have jobs that require decision-making, problem-solving, concentration, or other qualities, and without the brain exercise they need, they'll create their own projects to keep their minds busy -- and they probably won't be the kind of projects you'd like.",
     )

     db.session.add(family)
     db.session.add(children)
     db.session.add(dogs)
     db.session.add(shed)
     db.session.add(grooming)
     db.session.add(drool)
     db.session.add(coatType)
     db.session.add(coatLength)
     db.session.add(strangers)
     db.session.add(playfulness)
     db.session.add(protective)
     db.session.add(adaptability)
     db.session.add(trainability)
     db.session.add(energy)
     db.session.add(barking)
     db.session.add(mentalStim)

def undo_breed_traits():
   db.session.execute('TRUNCATE breed_traits RESTART IDENTITY CASCADE;')
   db.session.commit()




