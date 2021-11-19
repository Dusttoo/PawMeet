from app.models import db, Breed_Answer

def seed_breed_answers():
    #Lab
    lab1= Breed_Answer(
        breed_id=1,
        trait_id=1,
        answer=5,
    )
    lab2= Breed_Answer(
        breed_id=1,
        trait_id=2,
        answer=5,
    )
    lab3= Breed_Answer(
        breed_id=1,
        trait_id=3,
        answer=5,
    )
    lab4= Breed_Answer(
        breed_id=1,
        trait_id=4,
        answer=4,
    ) 
    lab5= Breed_Answer(
        breed_id=1,
        trait_id=5,
        answer=2,
    )
    lab6= Breed_Answer(
        breed_id=1,
        trait_id=6,
        answer=2,
    ) 
    lab7= Breed_Answer(
        breed_id=1,
        trait_id=7,
        answer=8,
    )
    lab8= Breed_Answer(
        breed_id=1,
        trait_id=8,
        answer=1,
    ) 
    lab9= Breed_Answer(
        breed_id=1,
        trait_id=9,
        answer=5,
    )
    lab10= Breed_Answer(
        breed_id=1,
        trait_id=10,
        answer=5,
    ) 
    lab11= Breed_Answer(
        breed_id=1,
        trait_id=11,
        answer=3,
    )
    lab12= Breed_Answer(
        breed_id=1,
        trait_id=12,
        answer=5,
    ) 
    lab13= Breed_Answer(
        breed_id=1,
        trait_id=13,
        answer=5,
    )
    lab14= Breed_Answer(
        breed_id=1,
        trait_id=14,
        answer=5,
    ) 
    lab15= Breed_Answer(
        breed_id=1,
        trait_id=15,
        answer=3,
    )
    lab16= Breed_Answer(
        breed_id=1,
        trait_id=16,
        answer=4,
    )

    #Frenchie
    frenchie1 = Breed_Answer(
        breed_id=2,
        trait_id=1,
        answer=5,
    )
    frenchie2 = Breed_Answer(
        breed_id=2,
        trait_id=2,
        answer=5,
    )
    frenchie3 = Breed_Answer(
        breed_id=2,
        trait_id=3,
        answer=4,
    )
    frenchie4 = Breed_Answer(
        breed_id=2,
        trait_id=4,
        answer=3,
    )
    frenchie5 = Breed_Answer(
        breed_id=2,
        trait_id=5,
        answer=1,
    )
    frenchie6 = Breed_Answer(
        breed_id=2,
        trait_id=6,
        answer=3,
    )
    frenchie7 = Breed_Answer(
        breed_id=2,
        trait_id=7,
        answer=7,
    )
    frenchie8 = Breed_Answer(
        breed_id=2,
        trait_id=8,
        answer=1,
    )
    frenchie9 = Breed_Answer(
        breed_id=2,
        trait_id=9,
        answer=5,
    )
    frenchie10 = Breed_Answer(
        breed_id=2,
        trait_id=10,
        answer=5,
    )
    frenchie11 = Breed_Answer(
        breed_id=2,
        trait_id=11,
        answer=3,
    )
    frenchie12 = Breed_Answer(
        breed_id=2,
        trait_id=12,
        answer=5,
    )
    frenchie13 = Breed_Answer(
        breed_id=2,
        trait_id=13,
        answer=4,
    )
    frenchie14 = Breed_Answer(
        breed_id=2,
        trait_id=14,
        answer=3,
    )
    frenchie15 = Breed_Answer(
        breed_id=2,
        trait_id=15,
        answer=1,
    )
    frenchie16 = Breed_Answer(
        breed_id=2,
        trait_id=16,
        answer=3,
    )
    
    # GSD
    gsd1 = Breed_Answer(
        breed_id=3,
        trait_id=1,
        answer=5,
    )
    gsd2 = Breed_Answer(
        breed_id=3,
        trait_id=2,
        answer=5,
    )
    gsd3 = Breed_Answer(
        breed_id=3,
        trait_id=3,
        answer=3,
    )
    gsd4 = Breed_Answer(
        breed_id=3,
        trait_id=4,
        answer=4,
    )
    gsd5 = Breed_Answer(
        breed_id=3,
        trait_id=5,
        answer=2,
    )
    gsd6 = Breed_Answer(
        breed_id=3,
        trait_id=6,
        answer=2,
    )
    gsd7 = Breed_Answer(
        breed_id=3,
        trait_id=7,
        answer=8,
    )
    gsd8 = Breed_Answer(
        breed_id=3,
        trait_id=8,
        answer=2,
    )
    gsd9 = Breed_Answer(
        breed_id=3,
        trait_id=9,
        answer=3,
    )
    gsd10 = Breed_Answer(
        breed_id=3,
        trait_id=10,
        answer=4,
    )
    gsd11 = Breed_Answer(
        breed_id=3,
        trait_id=11,
        answer=5,
    )
    gsd12 = Breed_Answer(
        breed_id=3,
        trait_id=12,
        answer=5,
    )
    gsd13 = Breed_Answer(
        breed_id=3,
        trait_id=13,
        answer=5,
    )
    gsd14 = Breed_Answer(
        breed_id=3,
        trait_id=14,
        answer=5,
    )
    gsd15 = Breed_Answer(
        breed_id=3,
        trait_id=15,
        answer=3,
    )
    gsd16 = Breed_Answer(
        breed_id=3,
        trait_id=16,
        answer=5,
    )
    # Golden
    golden1 = Breed_Answer(
        breed_id=4,
        trait_id=1,
        answer=5,
    )
    golden2 = Breed_Answer(
        breed_id=4,
        trait_id=2,
        answer=5,
    )
    golden3 = Breed_Answer(
        breed_id=4,
        trait_id=3,
        answer=5,
    )
    golden4 = Breed_Answer(
        breed_id=4,
        trait_id=4,
        answer=4,
    )
    golden5 = Breed_Answer(
        breed_id=4,
        trait_id=5,
        answer=2,
    )
    golden6 = Breed_Answer(
        breed_id=4,
        trait_id=6,
        answer=2,
    )
    golden7 = Breed_Answer(
        breed_id=4,
        trait_id=7,
        answer=8,
    )
    golden8 = Breed_Answer(
        breed_id=4,
        trait_id=8,
        answer=2,
    )
    golden9 = Breed_Answer(
        breed_id=4,
        trait_id=9,
        answer=5,
    )
    golden10 = Breed_Answer(
        breed_id=4,
        trait_id=10,
        answer=4,
    )
    golden11 = Breed_Answer(
        breed_id=4,
        trait_id=11,
        answer=3,
    )
    golden12 = Breed_Answer(
        breed_id=4,
        trait_id=12,
        answer=5,
    )
    golden13 = Breed_Answer(
        breed_id=4,
        trait_id=13,
        answer=5,
    )
    golden14 = Breed_Answer(
        breed_id=4,
        trait_id=14,
        answer=3,
    )
    golden15 = Breed_Answer(
        breed_id=4,
        trait_id=15,
        answer=1,
    )
    golden16 = Breed_Answer(
        breed_id=4,
        trait_id=16,
        answer=4,
    )
    # Bulldog
    bull1 = Breed_Answer(
        breed_id=5,
        trait_id=1,
        answer=4,
    )
    bull2 = Breed_Answer(
        breed_id=5,
        trait_id=2,
        answer=3,
    )
    bull3 = Breed_Answer(
        breed_id=5,
        trait_id=3,
        answer=3,
    )
    bull4 = Breed_Answer(
        breed_id=5,
        trait_id=4,
        answer=3,
    )
    bull5 = Breed_Answer(
        breed_id=5,
        trait_id=5,
        answer=3,
    )
    bull6 = Breed_Answer(
        breed_id=5,
        trait_id=6,
        answer=3,
    )
    bull7 = Breed_Answer(
        breed_id=5,
        trait_id=7,
        answer=7,
    )
    bull8 = Breed_Answer(
        breed_id=5,
        trait_id=8,
        answer=1,
    )
    bull9 = Breed_Answer(
        breed_id=5,
        trait_id=9,
        answer=4,
    )
    bull10 = Breed_Answer(
        breed_id=5,
        trait_id=10,
        answer=4,
    )
    bull11 = Breed_Answer(
        breed_id=5,
        trait_id=11,
        answer=3,
    )
    bull12 = Breed_Answer(
        breed_id=5,
        trait_id=12,
        answer=3,
    )
    bull13 = Breed_Answer(
        breed_id=5,
        trait_id=13,
        answer=4,
    )
    bull14 = Breed_Answer(
        breed_id=5,
        trait_id=14,
        answer=3,
    )
    bull15 = Breed_Answer(
        breed_id=5,
        trait_id=15,
        answer=2,
    )
    bull16 = Breed_Answer(
        breed_id=5,
        trait_id=16,
        answer=3,
    )
    # Poodle
    poodle1 = Breed_Answer(
        breed_id=6,
        trait_id=1,
        answer=5,
    )
    poodle2 = Breed_Answer(
        breed_id=6,
        trait_id=2,
        answer=5,
    )
    poodle3 = Breed_Answer(
        breed_id=6,
        trait_id=3,
        answer=3,
    )
    poodle4 = Breed_Answer(
        breed_id=6,
        trait_id=4,
        answer=1,
    )
    poodle5 = Breed_Answer(
        breed_id=6,
        trait_id=5,
        answer=4,
    )
    poodle6 = Breed_Answer(
        breed_id=6,
        trait_id=6,
        answer=1,
    )
    poodle7 = Breed_Answer(
        breed_id=6,
        trait_id=7,
        answer=3,
    )
    poodle8 = Breed_Answer(
        breed_id=6,
        trait_id=8,
        answer=3,
    )
    poodle9 = Breed_Answer(
        breed_id=6,
        trait_id=9,
        answer=5,
    )
    poodle10 = Breed_Answer(
        breed_id=6,
        trait_id=10,
        answer=5,
    )
    poodle11 = Breed_Answer(
        breed_id=6,
        trait_id=11,
        answer=5,
    )
    poodle12 = Breed_Answer(
        breed_id=6,
        trait_id=12,
        answer=4,
    )
    poodle13 = Breed_Answer(
        breed_id=6,
        trait_id=13,
        answer=5,
    )
    poodle14 = Breed_Answer(
        breed_id=6,
        trait_id=14,
        answer=4,
    )
    poodle15 = Breed_Answer(
        breed_id=6,
        trait_id=15,
        answer=4,
    )
    poodle16 = Breed_Answer(
        breed_id=6,
        trait_id=16,
        answer=5,
    )
    #  Beagle
    beagle1 = Breed_Answer(
        breed_id=7,
        trait_id=1,
        answer=3,
    )
    beagle2 = Breed_Answer(
        breed_id=7,
        trait_id=2,
        answer=5,
    )
    beagle3 = Breed_Answer(
        breed_id=7,
        trait_id=3,
        answer=5,
    )
    beagle4 = Breed_Answer(
        breed_id=7,
        trait_id=4,
        answer=3,
    )
    beagle5 = Breed_Answer(
        breed_id=7,
        trait_id=5,
        answer=2,
    )
    beagle6 = Breed_Answer(
        breed_id=7,
        trait_id=6,
        answer=1,
    )
    beagle7 = Breed_Answer(
        breed_id=7,
        trait_id=7,
        answer=7,
    )
    beagle8 = Breed_Answer(
        breed_id=7,
        trait_id=8,
        answer=1,
    )
    beagle9 = Breed_Answer(
        breed_id=7,
        trait_id=9,
        answer=3,
    )
    beagle10 = Breed_Answer(
        breed_id=7,
        trait_id=10,
        answer=4,
    )
    beagle11 = Breed_Answer(
        breed_id=7,
        trait_id=11,
        answer=2,
    )
    beagle12 = Breed_Answer(
        breed_id=7,
        trait_id=12,
        answer=4,
    )
    beagle13 = Breed_Answer(
        breed_id=7,
        trait_id=13,
        answer=3,
    )
    beagle14 = Breed_Answer(
        breed_id=7,
        trait_id=14,
        answer=4,
    )
    beagle15 = Breed_Answer(
        breed_id=7,
        trait_id=15,
        answer=4,
    )
    beagle16 = Breed_Answer(
        breed_id=7,
        trait_id=16,
        answer=4,
    )
    #  Rottweiler
    rott1 = Breed_Answer(
        breed_id=8,
        trait_id=1,
        answer=5,
    )
    rott2 = Breed_Answer(
        breed_id=8,
        trait_id=2,
        answer=3,
    )
    rott3 = Breed_Answer(
        breed_id=8,
        trait_id=3,
        answer=3,
    )
    rott4 = Breed_Answer(
        breed_id=8,
        trait_id=4,
        answer=3,
    )
    rott5 = Breed_Answer(
        breed_id=8,
        trait_id=5,
        answer=1,
    )
    rott6 = Breed_Answer(
        breed_id=8,
        trait_id=6,
        answer=3,
    )
    rott7 = Breed_Answer(
        breed_id=8,
        trait_id=7,
        answer=7,
    )
    rott8 = Breed_Answer(
        breed_id=8,
        trait_id=8,
        answer=1,
    )
    rott9 = Breed_Answer(
        breed_id=8,
        trait_id=9,
        answer=3,
    )
    rott10 = Breed_Answer(
        breed_id=8,
        trait_id=10,
        answer=4,
    )
    rott11 = Breed_Answer(
        breed_id=8,
        trait_id=11,
        answer=5,
    )
    rott12 = Breed_Answer(
        breed_id=8,
        trait_id=12,
        answer=4,
    )
    rott13 = Breed_Answer(
        breed_id=8,
        trait_id=13,
        answer=5,
    )
    rott14 = Breed_Answer(
        breed_id=8,
        trait_id=14,
        answer=3,
    )
    rott15 = Breed_Answer(
        breed_id=8,
        trait_id=15,
        answer=1,
    )
    rott16 = Breed_Answer(
        breed_id=8,
        trait_id=16,
        answer=5,
    )
    # GSD
    gsp1 = Breed_Answer(
        breed_id=9,
        trait_id=1,
        answer=5,
    )
    gsp2 = Breed_Answer(
        breed_id=9,
        trait_id=2,
        answer=5,
    )
    gsp3 = Breed_Answer(
        breed_id=9,
        trait_id=3,
        answer=4,
    )
    gsp4 = Breed_Answer(
        breed_id=9,
        trait_id=4,
        answer=3,
    )
    gsp5 = Breed_Answer(
        breed_id=9,
        trait_id=5,
        answer=2,
    )
    gsp6 = Breed_Answer(
        breed_id=9,
        trait_id=6,
        answer=2,
    )
    gsp7 = Breed_Answer(
        breed_id=9,
        trait_id=7,
        answer=7,
    )
    gsp8 = Breed_Answer(
        breed_id=9,
        trait_id=8,
        answer=1,
    )
    gsp9 = Breed_Answer(
        breed_id=9,
        trait_id=9,
        answer=4,
    )
    gsp10 = Breed_Answer(
        breed_id=9,
        trait_id=10,
        answer=4,
    )
    gsp11 = Breed_Answer(
        breed_id=9,
        trait_id=11,
        answer=4,
    )
    gsp12 = Breed_Answer(
        breed_id=9,
        trait_id=12,
        answer=4,
    )
    gsp13 = Breed_Answer(
        breed_id=9,
        trait_id=13,
        answer=5,
    )
    gsp14 = Breed_Answer(
        breed_id=9,
        trait_id=14,
        answer=5,
    )
    gsp15 = Breed_Answer(
        breed_id=9,
        trait_id=15,
        answer=3,
    )
    gsp16 = Breed_Answer(
        breed_id=9,
        trait_id=16,
        answer=5,
    )
    # Dachshund
    dox1 = Breed_Answer(
        breed_id=10,
        trait_id=1,
        answer=5,
    )
    dox2 = Breed_Answer(
        breed_id=10,
        trait_id=2,
        answer=3,
    )
    dox3 = Breed_Answer(
        breed_id=10,
        trait_id=3,
        answer=4,
    )
    dox4 = Breed_Answer(
        breed_id=10,
        trait_id=4,
        answer=2,
    )
    dox5 = Breed_Answer(
        breed_id=10,
        trait_id=5,
        answer=2,
    )
    dox6 = Breed_Answer(
        breed_id=10,
        trait_id=6,
        answer=2,
    )
    dox7 = Breed_Answer(
        breed_id=10,
        trait_id=7,
        answer=7,
    )
    dox8 = Breed_Answer(
        breed_id=10,
        trait_id=8,
        answer=2,
    )
    dox9 = Breed_Answer(
        breed_id=10,
        trait_id=9,
        answer=4,
    )
    dox10 = Breed_Answer(
        breed_id=10,
        trait_id=10,
        answer=4,
    )
    dox11 = Breed_Answer(
        breed_id=10,
        trait_id=11,
        answer=4,
    )
    dox12 = Breed_Answer(
        breed_id=10,
        trait_id=12,
        answer=4,
    )
    dox13 = Breed_Answer(
        breed_id=10,
        trait_id=13,
        answer=4,
    )
    dox14 = Breed_Answer(
        breed_id=10,
        trait_id=14,
        answer=3,
    )
    dox15 = Breed_Answer(
        breed_id=10,
        trait_id=15,
        answer=5,
    )
    dox16 = Breed_Answer(
        breed_id=10,
        trait_id=16,
        answer=3,
    )

    # CORSO

    corso1 = Breed_Answer(
        breed_id=11,
        trait_id=1,
        answer=4,
    )
    corso2 = Breed_Answer(
        breed_id=11,
        trait_id=2,
        answer=3,
    )
    corso3 = Breed_Answer(
        breed_id=11,
        trait_id=3,
        answer=3,
    )
    corso4 = Breed_Answer(
        breed_id=11,
        trait_id=4,
        answer=2,
    )
    corso5 = Breed_Answer(
        breed_id=11,
        trait_id=5,
        answer=1,
    )
    corso6 = Breed_Answer(
        breed_id=11,
        trait_id=6,
        answer=3,
    )
    corso7 = Breed_Answer(
        breed_id=11,
        trait_id=7,
        answer=7,
    )
    corso8 = Breed_Answer(
        breed_id=11,
        trait_id=8,
        answer=1,
    )
    corso9 = Breed_Answer(
        breed_id=11,
        trait_id=9,
        answer=3,
    )
    corso10 = Breed_Answer(
        breed_id=11,
        trait_id=10,
        answer=3,
    )
    corso11 = Breed_Answer(
        breed_id=11,
        trait_id=11,
        answer=5,
    )
    corso12 = Breed_Answer(
        breed_id=11,
        trait_id=12,
        answer=3,
    )
    corso13 = Breed_Answer(
        breed_id=11,
        trait_id=13,
        answer=4,
    )
    corso14 = Breed_Answer(
        breed_id=11,
        trait_id=14,
        answer=4,
    )
    corso15 = Breed_Answer(
        breed_id=11,
        trait_id=15,
        answer=3,
    )
    corso16 = Breed_Answer(
        breed_id=11,
        trait_id=16,
        answer=3,
    )

    # AMSTAFF
    amstaff1= Breed_Answer(
        breed_id=12,
        trait_id=1,
        answer=5,
    )
    amstaff2 = Breed_Answer(
        breed_id=12,
        trait_id=2,
        answer=3,
    )
    amstaff3 = Breed_Answer(
        breed_id=12,
        trait_id=3,
        answer=3,
    )
    amstaff4 = Breed_Answer(
        breed_id=12,
        trait_id=4,
        answer=2,
    )
    amstaff5 = Breed_Answer(
        breed_id=12,
        trait_id=5,
        answer=1,
    )
    amstaff6 = Breed_Answer(
        breed_id=12,
        trait_id=6,
        answer=1,
    )
    amstaff7 = Breed_Answer(
        breed_id=12,
        trait_id=7,
        answer=7,
    )
    amstaff8 = Breed_Answer(
        breed_id=12,
        trait_id=8,
        answer=1,
    )
    amstaff9 = Breed_Answer(
        breed_id=12,
        trait_id=9,
        answer=4,
    )
    amstaff10 = Breed_Answer(
        breed_id=12,
        trait_id=10,
        answer=3,
    )
    amstaff11 = Breed_Answer(
        breed_id=12,
        trait_id=11,
        answer=5,
    )
    amstaff12 = Breed_Answer(
        breed_id=12,
        trait_id=12,
        answer=3,
    )
    amstaff13 = Breed_Answer(
        breed_id=12,
        trait_id=13,
        answer=3,
    )
    amstaff14 = Breed_Answer(
        breed_id=12,
        trait_id=14,
        answer=3,
    )
    amstaff15 = Breed_Answer(
        breed_id=12,
        trait_id=15,
        answer=3,
    )
    amstaff16 = Breed_Answer(
        breed_id=12,
        trait_id=16,
        answer=3,
    )
    # BOXER
    boxer1 = Breed_Answer(
        breed_id=13,
        trait_id=1,
        answer=4,
    )
    boxer2 = Breed_Answer(
        breed_id=13,
        trait_id=2,
        answer=5,
    )
    boxer3 = Breed_Answer(
        breed_id=13,
        trait_id=3,
        answer=3,
    )
    boxer4 = Breed_Answer(
        breed_id=13,
        trait_id=4,
        answer=2,
    )
    boxer5 = Breed_Answer(
        breed_id=13,
        trait_id=5,
        answer=2,
    )
    boxer6 = Breed_Answer(
        breed_id=13,
        trait_id=6,
        answer=3,
    )
    boxer7 = Breed_Answer(
        breed_id=13,
        trait_id=7,
        answer=7,
    )
    boxer8 = Breed_Answer(
        breed_id=13,
        trait_id=8,
        answer=1,
    )
    boxer9 = Breed_Answer(
        breed_id=13,
        trait_id=9,
        answer=4,
    )
    boxer10 = Breed_Answer(
        breed_id=13,
        trait_id=10,
        answer=4,
    )
    boxer11 = Breed_Answer(
        breed_id=13,
        trait_id=11,
        answer=4,
    )
    boxer12 = Breed_Answer(
        breed_id=13,
        trait_id=12,
        answer=3,
    )
    boxer13 = Breed_Answer(
        breed_id=13,
        trait_id=13,
        answer=4,
    )
    boxer14 = Breed_Answer(
        breed_id=13,
        trait_id=14,
        answer=4,
    )
    boxer15 = Breed_Answer(
        breed_id=13,
        trait_id=15,
        answer=3,
    )
    boxer16 = Breed_Answer(
        breed_id=13,
        trait_id=16,
        answer=4,
    )
    # PUG
    pug1 = Breed_Answer(
        breed_id=14,
        trait_id=1,
        answer=5,
    )
    pug2 = Breed_Answer(
        breed_id=14,
        trait_id=2,
        answer=5,
    )
    pug3 = Breed_Answer(
        breed_id=14,
        trait_id=3,
        answer=4,
    )
    pug4 = Breed_Answer(
        breed_id=14,
        trait_id=4,
        answer=4,
    )
    pug5 = Breed_Answer(
        breed_id=14,
        trait_id=5,
        answer=2,
    )
    pug6 = Breed_Answer(
        breed_id=14,
        trait_id=6,
        answer=1,
    )
    pug7 = Breed_Answer(
        breed_id=14,
        trait_id=7,
        answer=7,
    )
    pug8 = Breed_Answer(
        breed_id=14,
        trait_id=8,
        answer=1,
    )
    pug9 = Breed_Answer(
        breed_id=14,
        trait_id=9,
        answer=5,
    )
    pug10 = Breed_Answer(
        breed_id=14,
        trait_id=10,
        answer=5,
    )
    pug11 = Breed_Answer(
        breed_id=14,
        trait_id=11,
        answer=3,
    )
    pug12 = Breed_Answer(
        breed_id=14,
        trait_id=12,
        answer=5,
    )
    pug13 = Breed_Answer(
        breed_id=14,
        trait_id=13,
        answer=4,
    )
    pug14 = Breed_Answer(
        breed_id=14,
        trait_id=14,
        answer=3,
    )
    pug15 = Breed_Answer(
        breed_id=14,
        trait_id=15,
        answer=1,
    )
    pug16 = Breed_Answer(
        breed_id=14,
        trait_id=16,
        answer=3,
    )









    db.session.add(lab1)
    db.session.add(lab2)
    db.session.add(lab3)
    db.session.add(lab4)
    db.session.add(lab5)
    db.session.add(lab6)
    db.session.add(lab7)
    db.session.add(lab8)
    db.session.add(lab9)
    db.session.add(lab10)
    db.session.add(lab11)
    db.session.add(lab12)
    db.session.add(lab13)
    db.session.add(lab14)
    db.session.add(lab15)
    db.session.add(lab16)
    db.session.add(frenchie1)
    db.session.add(frenchie2)
    db.session.add(frenchie3)
    db.session.add(frenchie4)
    db.session.add(frenchie5)
    db.session.add(frenchie6)
    db.session.add(frenchie7)
    db.session.add(frenchie8)
    db.session.add(frenchie9)
    db.session.add(frenchie10)
    db.session.add(frenchie11)
    db.session.add(frenchie12)
    db.session.add(frenchie13)
    db.session.add(frenchie14)
    db.session.add(frenchie15)
    db.session.add(frenchie16)
    db.session.add(gsd1)
    db.session.add(gsd2)
    db.session.add(gsd3)
    db.session.add(gsd4)
    db.session.add(gsd5)
    db.session.add(gsd6)
    db.session.add(gsd7)
    db.session.add(gsd8)
    db.session.add(gsd9)
    db.session.add(gsd10)
    db.session.add(gsd11)
    db.session.add(gsd12)
    db.session.add(gsd13)
    db.session.add(gsd14)
    db.session.add(gsd15)
    db.session.add(gsd16)
    db.session.add(golden1)
    db.session.add(golden2)
    db.session.add(golden3)
    db.session.add(golden4)
    db.session.add(golden5)
    db.session.add(golden6)
    db.session.add(golden7)
    db.session.add(golden8)
    db.session.add(golden9)
    db.session.add(golden10)
    db.session.add(golden11)
    db.session.add(golden12)
    db.session.add(golden13)
    db.session.add(golden14)
    db.session.add(golden15)
    db.session.add(golden16)
    db.session.add(bull1)
    db.session.add(bull2)
    db.session.add(bull3)
    db.session.add(bull4)
    db.session.add(bull5)
    db.session.add(bull6)
    db.session.add(bull7)
    db.session.add(bull8)
    db.session.add(bull9)
    db.session.add(bull10)
    db.session.add(bull11)
    db.session.add(bull12)
    db.session.add(bull13)
    db.session.add(bull14)
    db.session.add(bull15)
    db.session.add(bull16)
    db.session.add(poodle1)
    db.session.add(poodle2)
    db.session.add(poodle3)
    db.session.add(poodle4)
    db.session.add(poodle5)
    db.session.add(poodle6)
    db.session.add(poodle7)
    db.session.add(poodle8)
    db.session.add(poodle9)
    db.session.add(poodle10)
    db.session.add(poodle11)
    db.session.add(poodle12)
    db.session.add(poodle13)
    db.session.add(poodle14)
    db.session.add(poodle15)
    db.session.add(poodle16)
    db.session.add(beagle1)
    db.session.add(beagle2)
    db.session.add(beagle3)
    db.session.add(beagle4)
    db.session.add(beagle5)
    db.session.add(beagle6)
    db.session.add(beagle7)
    db.session.add(beagle8)
    db.session.add(beagle9)
    db.session.add(beagle10)
    db.session.add(beagle11)
    db.session.add(beagle12)
    db.session.add(beagle13)
    db.session.add(beagle14)
    db.session.add(beagle15)
    db.session.add(beagle16)
    db.session.add(rott1)
    db.session.add(rott2)
    db.session.add(rott3)
    db.session.add(rott4)
    db.session.add(rott5)
    db.session.add(rott6)
    db.session.add(rott7)
    db.session.add(rott8)
    db.session.add(rott9)
    db.session.add(rott10)
    db.session.add(rott11)
    db.session.add(rott12)
    db.session.add(rott13)
    db.session.add(rott14)
    db.session.add(rott15)
    db.session.add(rott16)
    db.session.add(gsp1)
    db.session.add(gsp2)
    db.session.add(gsp3)
    db.session.add(gsp4)
    db.session.add(gsp5)
    db.session.add(gsp6)
    db.session.add(gsp7)
    db.session.add(gsp8)
    db.session.add(gsp9)
    db.session.add(gsp10)
    db.session.add(gsp11)
    db.session.add(gsp12)
    db.session.add(gsp13)
    db.session.add(gsp14)
    db.session.add(gsp15)
    db.session.add(gsp16)
    db.session.add(dox1)
    db.session.add(dox2)
    db.session.add(dox3)
    db.session.add(dox4)
    db.session.add(dox5)
    db.session.add(dox6)
    db.session.add(dox7)
    db.session.add(dox8)
    db.session.add(dox9)
    db.session.add(dox10)
    db.session.add(dox11)
    db.session.add(dox12)
    db.session.add(dox13)
    db.session.add(dox14)
    db.session.add(dox15)
    db.session.add(dox16)
    db.session.add(corso1)
    db.session.add(corso2)
    db.session.add(corso3)
    db.session.add(corso4)
    db.session.add(corso5)
    db.session.add(corso6)
    db.session.add(corso7)
    db.session.add(corso8)
    db.session.add(corso9)
    db.session.add(corso10)
    db.session.add(corso11)
    db.session.add(corso12)
    db.session.add(corso13)
    db.session.add(corso14)
    db.session.add(corso15)
    db.session.add(corso16)
    db.session.add(amstaff1)
    db.session.add(amstaff2)
    db.session.add(amstaff3)
    db.session.add(amstaff4)
    db.session.add(amstaff5)
    db.session.add(amstaff6)
    db.session.add(amstaff7)
    db.session.add(amstaff8)
    db.session.add(amstaff9)
    db.session.add(amstaff10)
    db.session.add(amstaff11)
    db.session.add(amstaff12)
    db.session.add(amstaff13)
    db.session.add(amstaff14)
    db.session.add(amstaff15)
    db.session.add(amstaff16)
    db.session.add(boxer1)
    db.session.add(boxer2)
    db.session.add(boxer3)
    db.session.add(boxer4)
    db.session.add(boxer5)
    db.session.add(boxer6)
    db.session.add(boxer7)
    db.session.add(boxer8)
    db.session.add(boxer9)
    db.session.add(boxer10)
    db.session.add(boxer11)
    db.session.add(boxer12)
    db.session.add(boxer13)
    db.session.add(boxer14)
    db.session.add(boxer15)
    db.session.add(boxer16)
    db.session.add(pug1)
    db.session.add(pug2)
    db.session.add(pug3)
    db.session.add(pug4)
    db.session.add(pug5)
    db.session.add(pug6)
    db.session.add(pug7)
    db.session.add(pug8)
    db.session.add(pug9)
    db.session.add(pug10)
    db.session.add(pug11)
    db.session.add(pug12)
    db.session.add(pug13)
    db.session.add(pug14)
    db.session.add(pug15)
    db.session.add(pug16)


    db.session.commit()

def undo_breed_answers():
    db.session.execute('TRUNCATE breed_answers RESTART IDENTITY CASCADE;')
    db.session.commit()






    # Next breed
    # 1= Breed_Answer(
    #     breed_id=,
    #     trait_id=1,
    #     answer=,
    # )
    # 2= Breed_Answer(
    #     breed_id=,
    #     trait_id=2,
    #     answer=,
    # )
    # 3= Breed_Answer(
    #     breed_id=,
    #     trait_id=3,
    #     answer=,
    # )
    # 4= Breed_Answer(
    #     breed_id=,
    #     trait_id=4,
    #     answer=,
    # ) 
    # 5= Breed_Answer(
    #     breed_id=,
    #     trait_id=5,
    #     answer=,
    # )
    # 6= Breed_Answer(
    #     breed_id=,
    #     trait_id=6,
    #     answer=,
    # ) 
    # 7= Breed_Answer(
    #     breed_id=,
    #     trait_id=7,
    #     answer=,
    # )
    # 8= Breed_Answer(
    #     breed_id=,
    #     trait_id=8,
    #     answer=,
    # ) 
    # 9= Breed_Answer(
    #     breed_id=,
    #     trait_id=9,
    #     answer=,
    # )
    # 10= Breed_Answer(
    #     breed_id=,
    #     trait_id=10,
    #     answer=,
    # ) 
    # 11= Breed_Answer(
    #     breed_id=,
    #     trait_id=11,
    #     answer=,
    # )
    # 12= Breed_Answer(
    #     breed_id=,
    #     trait_id=12,
    #     answer=,
    # ) 
    # 13= Breed_Answer(
    #     breed_id=,
    #     trait_id=13,
    #     answer=,
    # )
    # 14= Breed_Answer(
    #     breed_id=,
    #     trait_id=14,
    #     answer=,
    # ) 
    # 15= Breed_Answer(
    #     breed_id=,
    #     trait_id=15,
    #     answer=,
    # )
    # 16= Breed_Answer(
    #     breed_id=,
    #     trait_id=16,
    #     answer=,
    # )

