from app.models import db, Breed

def seed_breeds():
    labrador = Breed(
        name='Labrador Retriever',
        breed_group= 1,
        personality=['Friendly', 'Active', 'Outgoing'],
        avg_height={
            'males': '22.5-24.5 inches',
            'females': '21.5-23.5 inches'
        },
        avg_weight={
            'males': '65-80 pounds',
            'females': '55-70 pounds'
        },
        avg_life_exp='10-12 years',
        description='The sweet-faced, lovable Labrador Retriever is America\'s most popular dog breed. Labs are friendly, outgoing, and high-spirited companions who have more than enough affection to go around for a family looking for a medium-to-large dog. The sturdy, well-balanced Labrador Retriever can, depending on the sex, stand from 21.5 to 24.5 inches at the shoulder and weigh between 55 to 80 pounds. The dense, hard coat comes in yellow, black, and a luscious chocolate. The head is wide, the eyes glimmer with kindliness, and the thick, tapering \'otter tail\' seems to be forever signaling the breed\'s innate eagerness. Labs are famously friendly. They are companionable housemates who bond with the whole family, and they socialize well with neighbor dogs and humans alike. But don\'t mistake his easygoing personality for low energy: The Lab is an enthusiastic athlete that requires lots of exercise, like swimming and marathon games of fetch, to keep physically and mentally fit.',

    )

    frenchie = Breed(
        name='French Bulldog',
        breed_group= 6,
        personality=['Playful', 'Smart', 'Adaptable'],
        avg_height={
            'males': '11-13 inches',
            'females': '11-13 inches'
        },
        avg_weight={
            'males': 'under 28 pounds',
            'females': 'under 28 pounds'
        },
        avg_life_exp='10-12 years',
        description="The one-of-a-kind French Bulldog, with his large bat ears and even disposition, is one of the world's most popular small-dog breeds, especially among city dwellers. The Frenchie is playful, alert, adaptable, and completely irresistible. The French Bulldog resembles a Bulldog in miniature, except for the large, erect 'bat ears' that are the breed's trademark feature. The head is large and square, with heavy wrinkles rolled above the extremely short nose. The body beneath the smooth, brilliant coat is compact and muscular. The bright, affectionate Frenchie is a charmer. Dogs of few words, Frenchies don't bark much'but their alertness makes them excellent watchdogs. They happily adapt to life with singles, couples, or families, and do not require a lot of outdoor exercise. They get on well with other animals and enjoy making new friends of the human variety. It is no wonder that city folk from Paris to Peoria swear by this vastly amusing and companionable breed.",

    )

    gsd = Breed(
        name='German Shepherd Dog',
        breed_group= 7,
        personality=['Smart', 'Confident', 'Courageous'],
        avg_height={
            'males': '24-26 inches',
            'females': '22-24 inches'
        },
        avg_weight={
            'males': '65-90 pounds',
            'females': '50-70 pounds'
        },
        avg_life_exp='7-10 years',
        description="Generally considered dogkind's finest all-purpose worker, the German Shepherd Dog is a large, agile, muscular dog of noble character and high intelligence. Loyal, confident, courageous, and steady, the German Shepherd is truly a dog lover's delight. German Shepherd Dogs can stand as high as 26 inches at the shoulder and, when viewed in outline, presents a picture of smooth, graceful curves rather than angles. The natural gait is a free-and-easy trot, but they can turn it up a notch or two and reach great speeds. There are many reasons why German Shepherds stand in the front rank of canine royalty, but experts say their defining attribute is character: loyalty, courage, confidence, the ability to learn commands for many tasks, and the willingness to put their life on the line in defense of loved ones. German Shepherds will be gentle family pets and steadfast guardians, but, the breed standard says, there's a 'certain aloofness that does not lend itself to immediate and indiscriminate friendships.'",

    )

    golden = Breed(
        name='Golden Retriever',
        breed_group= 1,
        personality=['Intelligent', 'Friendly', 'Devoted'],
        avg_height={
            'males': '23-24 inches',
            'females': '21.5-22.5 inches'
        },
        avg_weight={
            'males': '65-75 pounds',
            'females': '55-65 pounds'
        },
        avg_life_exp='10-12 years',
        description="The Golden Retriever, an exuberant Scottish gundog of great beauty, stands among America's most popular dog breeds. They are serious workers at hunting and field work, as guides for the blind, and in search-and-rescue, enjoy obedience and other competitive events, and have an endearing love of life when not at work. The Golden Retriever is a sturdy, muscular dog of medium size, famous for the dense, lustrous coat of gold that gives the breed its name. The broad head, with its friendly and intelligent eyes, short ears, and straight muzzle, is a breed hallmark. In motion, Goldens move with a smooth, powerful gait, and the feathery tail is carried, as breed fanciers say, with a 'merry action.' The most complete records of the development of the Golden Retriever are included in the record books that were kept from 1835 until about 1890 by the gamekeepers at the Guisachan (pronounced Gooeesicun) estate of Lord Tweedmouth at Inverness-Shire, Scotland. These records were released to public notice in Country Life in 1952, when Lord Tweedmouth's great-nephew, the sixth Earl of Ilchester, historian and sportsman, published material that had been left by his ancestor. They provided factual confirmation to the stories that had been handed down through generations. Goldens are outgoing, trustworthy, and eager-to-please family dogs, and relatively easy to train. They take a joyous and playful approach to life and maintain this puppyish behavior into adulthood. These energetic, powerful gundogs enjoy outdoor play. For a breed built to retrieve waterfowl for hours on end, swimming and fetching are natural pastimes.",

    )
    bulldog = Breed(
        name='Bulldog',
        breed_group= 6,
        personality=['Calm', 'Courageous', 'Friendly'],
        avg_height={
            'males': '14-15 inches',
            'females': '14-15 inches'
        },
        avg_weight={
            'males': '50 pounds',
            'females': '40 pounds'
        },
        avg_life_exp='8-10 years',
        description="Kind but courageous, friendly but dignified, the Bulldog is a thick-set, low-slung, well-muscled bruiser whose 'sourmug' face is the universal symbol of courage and tenacity. These docile, loyal companions adapt well to town or country. You can't mistake a Bulldog for any other breed. The loose skin of the head, furrowed brow, pushed-in nose, small ears, undershot jaw with hanging chops on either side, and the distinctive rolling gait all practically scream 'I'm a Bulldog!' The coat, seen in a variety of colors and patterns, is short, smooth, and glossy. Bulldogs can weigh up to 50 pounds, but that won't stop them from curling up in your lap, or at least trying to. But don't mistake their easygoing ways for laziness'Bulldogs enjoy brisk walks and need regular moderate exercise, along with a careful diet, to stay trim. Summer afternoons are best spent in an air-conditioned room as a Bulldog's short snout can cause labored breathing in hot and humid weather.",

    )

    poodle = Breed(
        name='Standard Poodle',
        breed_group= 6,
        personality=['Proud', 'Active', 'Very Smart'],
        avg_height={
            'males': 'over 15 inches',
            'females': 'over 15 inches'
        },
        avg_weight={
            'males': '60-70 pounds',
            'females': '40-50 pounds'
        },
        avg_life_exp='10 -18 years',
        description="Whether Standard, Miniature, or Toy, and either black, white, or apricot, the Poodle stands proudly among dogdom’s true aristocrats. Beneath the curly, low-allergen coat is an elegant athlete and companion for all reasons and seasons. Poodles come in three size varieties: Standards should be more than 15 inches tall at the shoulder; Miniatures are 15 inches or under; Toys stand no more than 10 inches. All three varieties have the same build and proportions. At dog shows, Poodles are usually seen in the elaborate Continental Clip. Most pet owners prefer the simpler Sporting Clip, in which the coat is shorn to follow the outline of the squarely built, smoothly muscled body. Forget those old stereotypes of Poodles as sissy dogs. Poodles are eager, athletic, and wickedly smart “real dogs” of remarkable versatility. The Standard, with his greater size and strength, is the best all-around athlete of the family, but all Poodles can be trained with great success.",

    )

    beagle = Breed(
        name='Beagle',
        breed_group= 2,
        personality=['Merry', 'Friendly', 'Curious'],
        avg_height={
            'males': 'under 15 inches',
            'females': 'under 15 inches'
        },
        avg_weight={
            'males': 'under 30 minutes',
            'females': 'under 30 minutes'
        },
        avg_life_exp='10-15 years',
        description="Not only is the Beagle an excellent hunting dog and loyal companion, it is also happy-go-lucky, funny, and'thanks to its pleading expression'cute. They were bred to hunt in packs, so they enjoy company and are generally easygoing. There are two Beagle varieties: those standing under 13 inches at the shoulder, and those between 13 and 15 inches. Both varieties are sturdy, solid, and 'big for their inches,' as dog folks say. They come in such pleasing colors as lemon, red and white, and tricolor. The Beagle's fortune is in his adorable face, with its big brown or hazel eyes set off by long, houndy ears set low on a broad head. A breed described as 'merry' by its fanciers, Beagles are loving and lovable, happy, and companionable'all qualities that make them excellent family dogs. No wonder that for years the Beagle has been the most popular hound dog among American pet owners. These are curious, clever, and energetic hounds who require plenty of playtime.",

    )
    rottweiler = Breed(
        name='Rottweiler',
        breed_group= 3,
        personality=['Loyal', 'Loving', 'Confident Guardian'],
        avg_height={
            'males': '24-27 inches',
            'females': '22-25 inches'
        },
        avg_weight={
            'males': '95-135 pounds',
            'females': '80-100 pounds'
        },
        avg_life_exp='9-10 years',
        description="The Rottweiler is a robust working breed of great strength descended from the mastiffs of the Roman legions. A gentle playmate and protector within the family circle, the Rottie observes the outside world with a self-assured aloofness. A male Rottweiler will stand anywhere from 24 to 27 muscular inches at the shoulder; females run a bit smaller and lighter. The glistening, short black coat with smart rust markings add to the picture of imposing strength. A thickly muscled hindquarters powers the Rottie's effortless trotting gait. A well-bred and properly raised Rottie will be calm and confident, courageous but not unduly aggressive. The aloof demeanor these world-class guardians present to outsiders belies the playfulness, and downright silliness, that endear Rotties to their loved ones. (No one told the Rottie he's not a toy breed, so he is liable plop onto your lap for a cuddle.) Early training and socialization will harness a Rottie's territorial instincts in a positive way.",

    )

    gsp = Breed(
        name='German Shorthaired Pointer',
        breed_group= 1,
        personality=['Friendly', 'Smart', 'Willing to Please'],
        avg_height={
            'males': '23-25 inches',
            'females': '21-23 inches '
        },
        avg_weight={
            'males': '55-70 pounds',
            'females': '45-60 pounds'
        },
        avg_life_exp='10-12 years',
        description="The versatile, medium-sized German Shorthaired Pointer is an enthusiastic gundog of all trades who thrives on vigorous exercise, positive training, and a lot of love. GSP people call their aristocratic companions the 'perfect pointer. 'Male German Shorthaired Pointers stand between 23 and 25 inches at the shoulder and weigh anywhere from 55 to 70 pounds females run smaller. The coat is solid liver(a reddish brown), or liver and white in distinctive patterns. The dark eyes shine with enthusiasm and friendliness. Built to work long days in the field or at the lake, GSPs are known for power, speed, agility, and endurance. 'Noble' and 'aristocratic' are words often used to describe the overall look. GSPs make happy, trainable pets who bond firmly to their family. They are always up for physical activities like running, swimming, organized dog sports'in fact, anything that will burn some of their boundless energy while spending outdoors time with a human buddy.",

    )

    dachshund = Breed(
        name='Dachshund',
        breed_group= 2,
        personality=['Spunky', 'Curious', 'Friendly'],
        avg_height={
            'males': '5-9 inches',
            'females': '5-9 inches'
        },
        avg_weight={
            'males': '32 pounds and under',
            'females': '32 pounds and under'
        },
        avg_life_exp='12-16 years',
        description="The famously long, low silhouette, ever-alert expression, and bold, vivacious personality of the Dachshund have made him a superstar of the canine kingdom. Dachshunds come in two sizes and in three coat types of various colors and patterns. The word 'icon' is terribly overworked, but the Dachshund'with his unmistakable long-backed body, little legs, and big personality' is truly an icon of purebred dogdom. Dachshunds can be standard-sized(usually 16 to 32 pounds) or miniature(11 pounds or under), and come in one of three coat types: smooth, wirehaired, or longhaired. Dachshunds aren't built for distance running, leaping, or strenuous swimming, but otherwise these tireless hounds are game for anything. Smart and vigilant, with a big-dog bark, they make fine watchdogs. Bred to be an independent hunter of dangerous prey, they can be brave to the point of rashness, and a bit stubborn, but their endearing nature and unique look has won millions of hearts the world over.",

    )

    corso = Breed(
        name='Cane Corso',
        breed_group=3,
        personality=['Affectionate', 'Intelligent', 'Majestic'],
        avg_height={
            'males': '25-27.5 inches',
             'females': '23.5-26 inches'
        },
        avg_weight={
            'males': 'Proportionate to height',
            'females': 'Proportionate to height'
        },
        avg_life_exp='9-12 years',
        description="Smart, trainable, and of noble bearing, the assertive and confident Cane Corso is a peerless protector. The Corso's lineage goes back to ancient Roman times, and the breed's name roughly translates from the Latin as 'bodyguard dog.' At nearly 28 inches at the shoulder and often weighing more than 100 pounds, with a large head, alert expression, and muscles rippling beneath their short, stiff coat, Corsi are at a glance intimidating creatures. Their imposing appearance is their first line of defense against intruders. As one writer put it, 'An understated air of cool competence, the kind of demeanor you'd expect from a professional bodyguard, is the breed's trademark.' Corsi are intelligent, loyal, eager to please, versatile, and intensely loyal to their humans, but are also assertive and willful, and can end up owning an unwitting owner. As with any other big guardian dog, responsible breeding and early socialization with people and other dogs is vital.",

    )

    pit = Breed(
        name='American Staffordshire Terrier',
        breed_group=4,
        personality=['Confident', 'Smart', 'Good-Natured'],
        avg_height={
            'males': '18-19 inches',
             'females': '17-18 inches'
        },
        avg_weight={
            'males': '55-70 pounds',
            'females': '40-55 pounds'
        },
        avg_life_exp='12-16 years',
        description="The American Staffordshire Terrier, known to their fans as AmStaffs, are smart, confident, good-natured companions. Their courage is proverbial. A responsibly bred, well-socialized AmStaff is a loyal, trustworthy friend to the end. AmStaffs are stocky, muscular bull-type terriers standing 17 to 19 inches at the shoulder. The head is broad, the jaws well defined, the cheekbones pronounced, and the dark, round eyes are set wide apart. AmStaff movement is agile and graceful, with a springy gait that advertises the breed's innate confidence. The stiff, glossy coat comes in many colors and patterns. AmStaffers describe their dogs as keenly aware of their surroundings, game for anything, and lovable 'personality dogs' around the house. AmStaffs like mental and physical challenges. They are highly trainable, as their many forays into showbiz suggest. When acquiring an AmStaff, there's only one way to go: Do your homework and find a responsible AKC breeder.",

    )

    boxer = Breed(
        name='Boxer',
        breed_group=3,
        personality=['Bright', 'Fun-Loving', 'Active'],
        avg_height={
            'males': '23-25 inches',
             'females': '21.5-23.5 inches'
        },
        avg_weight={
            'males': '65-80 pounds',
            'females': 'females are about 15 pounds less than male'
        },
        avg_life_exp='10-12 years',
        description="Loyalty, affection, intelligence, work ethic, and good looks: Boxers are the whole doggy package. Bright and alert, sometimes silly, but always courageous, the Boxer has been among America's most popular dog breeds for a very long time. A well-made Boxer in peak condition is an awesome sight. A male can stand as high as 25 inches at the shoulder; females run smaller. Their muscles ripple beneath a short, tight-fitting coat. The dark brown eyes and wrinkled forehead give the face an alert, curious look. The coat can be fawn or brindle, with white markings. Boxers move like the athletes they are named for: smooth and graceful, with a powerful forward thrust. Boxers are upbeat and playful. Their patience and protective nature have earned them a reputation as a great dog with children. They take the jobs of watchdog and family guardian seriously and will meet threats fearlessly. Boxers do best when exposed to a lot of people and other animals in early puppyhood.",

    )

    pug = Breed(
        name='Pug',
        breed_group=5,
        personality=['Charming', 'Loving', 'Mischevious'],
        avg_height={
            'males': '10-13 inches',
            'females': '10-13 inches'
        },
        avg_weight={
            'males': '14-18 pounds',
            'females': '14-18 pounds'
        },
        avg_life_exp='13-15 years',
        description="Once the mischievous companion of Chinese emperors, and later the mascot of Holland's royal House of Orange, the small but solid Pug is today adored by his millions of fans around the world. Pugs live to love and to be loved in return. The Pug's motto is the Latin phrase 'multum in parvo' (a lot in a little)' an apt description of this small but muscular breed. They come in three colors: silver or apricot-fawn with a black face mask, or all black. The large round head, the big, sparkling eyes, and the wrinkled brow give Pugs a range of human-like expressions'¿surprise, happiness, curiosity'¿that have delighted owners for centuries. Pug owners say their breed is the ideal house dog. Pugs are happy in the city or country, with kids or old folks, as an only pet or in a pack. They enjoy their food, and care must be taken to keep them trim. They do best in moderate climates 'not too hot, not too cold' but, with proper care, Pugs can be their adorable selves anywhere.",

    )


    akita = Breed(
        name='Akita',
        breed_group=3,
        personality=['Courageous', 'Diginified', 'Profoundly Loyal'],
        avg_height={
            'males': '26-28 inches',
             'females': '24-26 inches'
        },
        avg_weight={
            'males': '100-130 pounds',
            'females': '70-100 pounds '
        },
        avg_life_exp='10-14 years',
        description="Akita is muscular, double-coated dogs of ancient Japanese lineage famous for her dignity, courage, and loyalty. In her native land, she's venerated as family protectors and symbols of good health, happiness, and long life. Akitas are burly, heavy-boned spitz-type dogs of imposing stature. Standing 24 to 28 inches at the shoulder, Akitas have a dense coat that comes in several colors, including white. The head is broad and massive, and is balanced in the rear by a full, curled-over tail. The erect ears and dark, shining eyes contribute to an expression of alertness, a hallmark of the breed.     Akitas are quiet, fastidious dogs. Wary of strangers and often intolerant of other animals, Akitas will gladly share their silly, affectionate side with family and friends. They thrive on human companionship. The large, independent-thinking Akita is hardwired for protecting those they love. They must be well socialized from birth with people and other dogs.",
    )


    husky = Breed(
        name='Siberian Husky',
        breed_group=3,
        personality=['Loyal', 'Outgoing', 'Mischevious'],
        avg_height={
            'males': '21-23.5 inches',
             'females': '20-22 inches'
        },
        avg_weight={
            'males': '45-60 pounds',
            'females': '35-50 pounds'
        },
        avg_life_exp='12-14 years',
        description="Siberian Husky, a thickly coated, compact sled dog of medium size and great endurance, was developed to work in packs, pulling light loads at moderate speeds over vast frozen expanses. Sibes are friendly, fastidious, and dignified. The graceful, medium-sized Siberian Husky's almond-shaped eyes can be either brown or blue'¿and sometimes one of each'¿and convey a keen but amiable and even mischievous expression. Quick and nimble-footed, Siberians are known for their powerful but seemingly effortless gait. Tipping the scales at no more than 60 pounds, they are noticeably smaller and lighter than their burly cousin, the Alaskan Malamute. As born pack dogs, they enjoy family life and get on well with other dogs. The Sibe's innate friendliness render them indifferent watchdogs. These are energetic dogs who can't resist chasing small animals, so secure running room is a must. An attractive feature of the breed: Sibes are naturally clean, with little doggy odor.",
    )

    bully = Breed(
        name='American Bully',
        breed_group=6,
        personality=['Adaptable', 'Trainable', 'Loving'],
        avg_height={
            'males': '13–20 in',
             'females': '13–20 in'
        },
        avg_weight={
            'males': '44–132 lb',
            'females': '44–132 lb'
        },
        avg_life_exp='8-13 years',
        description="The American Bully is a recently formed companion dog breed, originally recognized in 2004 by the American Bully Kennel Club (ABKC) and followed by the European Bully Kennel Club (EBKC) in 2008. It has been recognized by the United Kennel Club (UKC) since July 15, 2013.[1] The breed has not been recognized by the American Kennel Club (AKC). The American Bully is a small to large breed, which has been divided into four categories by some registering organizations, including Pocket, Standard, Classic, and XL. Other organizations, including the UKC, have one consistent size standard.",
    )

    corgi = Breed(
        name='Pembroke Welsh Corgi',
        breed_group=7,
        personality=['Affectionate', 'Smart', 'Alert'],
        avg_height={
            'males': '10-12 inches',
            'females': '10-12 inches'
        },
        avg_weight={
            'males': 'up to 30 pounds',
            'females': 'up to 28 pounds'
        },
        avg_life_exp='12-13 years',
        description="Among the most agreeable of all small housedogs, the Pembroke Welsh Corgi is a strong, athletic, and lively little herder who is affectionate and companionable without being needy. They are one the world's most popular herding breeds. At 10 to 12 inches at the shoulder and 27 to 30 pounds, a well-built male Pembroke presents a big dog in a small package. Short but powerful legs, muscular thighs, and a deep chest equip him for a hard day's work. Built long and low, Pembrokes are surprisingly quick and agile. They can be red, sable, fawn, and black and tan, with or without white markings. The Pembroke is a bright, sensitive dog who enjoys play with his human family and responds well to training. As herders bred to move cattle, they are fearless and independent. They are vigilant watchdogs, with acute senses and a 'big dog' bark. Families who can meet their bold but kindly Pembroke's need for activity and togetherness will never have a more loyal, loving pet.",
    )

    cocker = Breed(
        name='Cocker Spaniel',
        breed_group=1,
        personality=['Smart', 'Happy', 'Gentle'],
        avg_height={
            'males': '14.5-15.5 inches',
            'females': '13.5-14.5 inches'
        },
        avg_weight={
            'males': '25-30 pounds',
            'females': '20-25 pounds'
        },
        avg_life_exp='10-14 years',
        description="The merry and frolicsome Cocker Spaniel, with his big, dreamy eyes and impish personality, is one of the world's best-loved breeds. They were developed as hunting dogs, but Cockers gained their wide popularity as all-around companions. Those big, dark eyes; that sweet expression; those long, lush ears that practically demand to be touched'¿no wonder the Cocker spent years as America's most popular breed. The Cocker is the AKC's smallest sporting spaniel, standing about 14 to 15 inches. The coat comes in enough colors and patterns to please any taste. The well-balanced body is sturdy and solid, and these quick, durable gundogs move with a smooth, easy gait. Cockers are eager playmates for kids and are easily trained as companions and athletes. They are big enough to be sporty, but compact enough to be portable. A Cocker in full coat rewards extra grooming time by being the prettiest dog on the block. These energetic sporting dogs love playtime and brisk walks.",
    )

    mastiff = Breed(
        name='Bullmastiff',
        breed_group=3,
        personality=['Affectionate', 'Loyal', 'Brave'],
        avg_height={
            'males': '25-27 inches',
            'females': '24-26 inches'
        },
        avg_weight={
            'males': '110-130 pounds',
            'females': '100-120 pounds'
        },
        avg_life_exp='7-9 years',
        description="Fearless at work, docile at home, the Bullmastiff is a large, muscular guarder who pursued and held poachers in Merry Old England'¿merry, we suppose, for everyone but poachers. Bullmastiffs are the result of Bulldog and Mastiff crosses. The Bullmastiff isn't quite as large as his close cousin the Mastiff. Still, standing as high as 27 inches at the shoulder and weighing between 100 and 130 pounds, this is still a whole lot of dog. After the first impression made by the Bullmastiff's size, it is the large, broad head that conveys the breed's essence: the dark eyes, high-set V-shaped ears, and broad, deep muzzle all combine to present the intelligence, alertness, and confidence that make the Bullmastiff a world-class protector and family companion. Coats come in fawn, red, or brindle. These are biddable and reliable creatures, but as with any large guarding dog, owners must begin training and socialization early, while the puppy is still small enough to control.",
        )


            





    db.session.add(labrador)
    db.session.add(frenchie)
    db.session.add(gsd)
    db.session.add(golden)
    db.session.add(bulldog)
    db.session.add(poodle)
    db.session.add(beagle)
    db.session.add(rottweiler)
    db.session.add(gsp)
    db.session.add(dachshund)
    db.session.add(corso)
    db.session.add(pit)
    db.session.add(boxer)
    db.session.add(pug)

    db.session.add(akita)
    db.session.add(husky)
    db.session.add(bully)
    db.session.add(corgi)
    db.session.add(cocker)
    db.session.add(mastiff)





    db.session.commit()

def undo_breeds():
    db.session.execute('TRUNCATE breeds RESTART IDENTITY CASCADE;')
    db.session.commit()


        
    # = Breed(
    #     name='',
    #     breed_group= ,
    #     personality=[],
    #     avg_height={
    #         'males': '',
    #         'females': ''
    #     },
    #     avg_weight={
    #         'males': '',
    #         'females': ''
    #     },
    #     avg_life_exp='',
    #     description="",

    # )

   