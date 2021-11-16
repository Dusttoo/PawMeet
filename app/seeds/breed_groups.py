from app.models import db, Breed_Group


def seed_breed_groups():
    sporting = Breed_Group(
        name='Sporting',
        description='Breeds in the Sporting Group were bred to assist hunters in the capture and retrieval of feathered game. Retrievers, built for swimming, specialize on waterfowl, while the hunting grounds of setters, spaniels, and pointing breeds are grasslands where quail, pheasant, and other game birds nest. Many Sporting Group breeds possess thick, water-repellant coats resistant to harsh hunting conditions.'
    )

    hound = Breed_Group(
        name='Houd',
        description='All breeds in the Hound Group were bred to pursue warm-blooded quarry. The sleek, long-legged sighthounds use explosive speed and wide vision to chase swift prey, like jackrabbits and antelope, while tough, durable scenthounds rely on their powerful noses to trail anything from raccoons to escaped convicts. Members of the Hound Group possess strong prey drives and often will stop at nothing to catch their quarries.'
    )

    working = Breed_Group(
        name='Working',
        description='Breeds in the Working Group are dogkind’s punch-the-clock, blue-collar workers, and the group includes some of the world’s most ancient breeds. They were developed to assist humans in some capacity – including pulling sleds and carts, guarding flocks and homes, and protecting their families – and many of these breeds are still used as working dogs today. Breeds in the Working Group tend to be known for imposing stature, strength, and intelligence.'
    )

    terrier = Breed_Group(
        name='Terrier',
        description='The feisty, short-legged breeds in the Terrier Group were first bred to go underground in pursuit of rodents and other vermin. Long-legged terrier breeds dig out varmints rather than burrowing in after them, while the group’s “bully” breeds, created long ago for ghastly pursuits like bull-baiting, are popular companion dogs today. Breeds in the Terrier Group are excellent competitors in the sport of Earthdog.'
    )

    toy = Breed_Group(
        name='Toy',
        description='The diminutive breeds of the Toy Group come in enough coat types and colors to satisfy nearly any preference, but all are small enough to fit comfortably in the lap of their adored humans. In a way, toys dogs are their own version of working dogs: they work hard at being attentive, affectionate companions. Breeds in the Toy Group are popular with city dwellers, as their small size makes them a good fit for smaller yards or apartments.'
    )

    non_sporting = Breed_Group(
        name='Non-Sporting',
        description="The breeds of the Non-Sporting Group have two things in common: wet noses and four legs. After that, there’s not much shared by this patchwork group of breeds whose job descriptions defy categorization in the six other groups, though they all have fascinating histories. Today, the varied breeds of the Non-Sporting Group are largely sought after as companion animals, as they were all developed to interact with people in some capacity."
    )

    herding = Breed_Group(
        name='Herding',
        description='The Herding Group comprises breeds developed for moving livestock, including sheep, cattle, and even reindeer. Herding dogs work closely with their human shepherds, and their natural intelligence and responsiveness makes them highly trainable. Today, some Herding breeds, such as the German Shepherd Dog, are commonly trained for police work. The high levels of energy found in Herding Group breeds means finding them a job is recommended, lest they begin herding your children at home.'
    )

    db.session.add(sporting)
    db.session.add(hound)
    db.session.add(working)
    db.session.add(terrier)
    db.session.add(toy)
    db.session.add(non_sporting)
    db.session.add(herding)

    db.session.commit()

def undo_breed_groups():
    db.session.execute('TRUNCATE breed_groups RESTART IDENTITY CASCADE;')
    db.session.commit()
