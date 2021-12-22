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
        breed_video='https://youtu.be/3__1qFlK3c0?t=10',
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
        breed_video='https://youtu.be/hakSTAofwm4?t=10',
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
        breed_video='https://youtu.be/ydrkZ5_gmWo?t=14',
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
        breed_video='https://youtu.be/rw-LOH0v0b0?t=303',
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
        breed_video='https://youtu.be/43b1JeJivCA?t=9',
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
        breed_video='https://youtu.be/yh8Bot1OfkE?t=43',
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
        breed_video='https://youtu.be/5HD-LQ4nDnk?t=50',
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
        breed_video='https://youtu.be/-wX7bFzQhHg?t=21',
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
        breed_video='https://youtu.be/sH2DE7VdFlE?t=30',
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
        breed_video='https://youtu.be/_6r_hZUHDo4?t=39',
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
        breed_video='https://youtu.be/lWT2ER5gJWA?t=10',
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
        breed_video='https://youtu.be/mVneF136Rbc?t=10',
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
        breed_video='https://youtu.be/7BSCUzx9ub8?t=19',
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
        breed_video='https://youtu.be/-5mC27mFPMI?t=10',
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
        breed_video='https://youtu.be/4YorlFHQlOw?t=10',
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
        breed_video='https://youtu.be/W3p9w-NQ4zE',
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
        breed_video='https://youtu.be/vxty0k37HR0?t=10',
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
        breed_video='https://youtu.be/BeoY-zSQvkM?t=11',
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
        breed_video='https://youtu.be/vNscIMWdcqo',
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
        breed_video='https://youtu.be/L6Xjb7iNNI4?t=10',
        description="Fearless at work, docile at home, the Bullmastiff is a large, muscular guarder who pursued and held poachers in Merry Old England'¿merry, we suppose, for everyone but poachers. Bullmastiffs are the result of Bulldog and Mastiff crosses. The Bullmastiff isn't quite as large as his close cousin the Mastiff. Still, standing as high as 27 inches at the shoulder and weighing between 100 and 130 pounds, this is still a whole lot of dog. After the first impression made by the Bullmastiff's size, it is the large, broad head that conveys the breed's essence: the dark eyes, high-set V-shaped ears, and broad, deep muzzle all combine to present the intelligence, alertness, and confidence that make the Bullmastiff a world-class protector and family companion. Coats come in fawn, red, or brindle. These are biddable and reliable creatures, but as with any large guarding dog, owners must begin training and socialization early, while the puppy is still small enough to control.",
        )

    breeds = [
        Breed(
            name='Australian Shepherd',
            breed_group=7,
            personality=['Smart', 'Work-Oriented', 'Exuberant'],
            avg_height={
                'males': '20-23 inches',
                'females': '18-21 inches'
            },
            avg_weight={
                'males': '50-65 pounds',
                'females': '40-55 pounds'
            },
            avg_life_exp='12-15 years',
            breed_video='https://youtu.be/H-KCl_cqE38?t=13',
            description="The Australian Shepherd, a lean, tough ranch dog, is one of those 'only in America' stories: a European breed perfected in California by way of Australia. Fixtures on the rodeo circuit, they are closely associated with the cowboy life. The Australian Shepherd, the cowboy's herding dog of choice, is a medium-sized worker with a keen, penetrating gaze in the eye. Aussie coats offer different looks, including merle (a mottled pattern with contrasting shades of blue or red). In all ways, they're the picture of rugged and agile movers of stock. Aussies exhibit an irresistible impulse to herd, anything: birds, dogs, kids. This strong work drive can make Aussies too much dog for a sedentary pet owner. Aussies are remarkably intelligent, quite capable of hoodwinking an unsuspecting novice owner. In short, this isn't the pet for everyone. But if you're looking for a brainy, tireless, and trainable partner for work or sport, your search might end here.",

        ),
        Breed(
            name='Yorkshire Terrier',
            breed_group=5,
            personality=['Affectionate', 'Sprightly', 'Tomboyish'],
            avg_height={
                'males': '7-8 inches',
                'females': '7-8 inches'
            },
            avg_weight={
                'males': '7 pounds',
                'females': '7 pounds'
            },
            avg_life_exp='11-15 years',
            breed_video='https://youtu.be/k4vXGmhAOPY',

            description="Beneath the dainty, glossy, floor-length coat of a Yorkshire Terrier beats the heart of a feisty, old-time terrier. Yorkies earned their living as ratters in mines and mills long before they became the beribboned lapdogs of Victorian ladies. The Yorkshire Terrier is a compact, toy-size terrier of no more than seven pounds whose crowning glory is a floor-length, silky coat of steel blue and a rich golden tan. Don't let the Yorkie's daintiness fool you. Tenacious, feisty, brave, and sometimes bossy, the Yorkie exhibits all the traits of a true terrier. Often named the most popular dog breed in various American cities, Yorkies pack lots of big-town attitude into a small but self-important package. They are favorites of urbanites the world over. Yorkies are long-lived and hypoallergenic (the coat is more like human hair than animal fur), and they make fine little watchdogs. This is a true 'personality breed,' providing years of laughs, love, and close companionship.",

        ),
        Breed(
            name='Great Dane',
            breed_group=3,
            personality=['Friendly', 'Patient', 'Dependable'],
            avg_height={
                'males': '30-32 inches',
                'females': '28-30 inches'
            },
            avg_weight={
                'males': '140-175 pounds',
                'females': '110-140 pounds'
            },
            avg_life_exp='7-10 years',
            breed_video='https://youtu.be/f9A-3IdCzMk?t=10',

            description="The easygoing Great Dane, the mighty 'Apollo of Dogs,' is a total joy to live with, but owning a dog of such imposing size, weight, and strength is a commitment not to be entered into lightly. This breed is indeed great, but not a Dane. As tall as 32 inches at the shoulder, Danes tower over most other dogs and when standing on their hind legs, they are taller than most people. These powerful giants are the picture of elegance and balance, with the smooth and easy stride of born noblemen. The coat comes in different colors and patterns, perhaps the best-known being the black-and-white patchwork pattern known as 'harlequin.' Despite their sweet nature, Danes are alert home guardians. Just the sight of these gentle giants is usually enough to make intruders think twice. But those foolish enough to mistake the breed's friendliness for softness will meet a powerful foe of true courage and spirit. Patient with kids, Danes are people pleasers who make friends easily.",

        ),
        Breed(
            name='Cavalier King Charles Spaniel',
            breed_group=5,
            personality=['Affectionate', 'Gentle', 'Graceful'],
            avg_height={
                'males': '12-13 inches',
                'females': '12-13 inches'
            },
            avg_weight={
                'males': '13-18 pounds',
                'females': '13-18 pounds'
            },
            avg_life_exp='12-15 years',
            breed_video='https://youtu.be/KuYuo6ybPg0',

            description="The Cavalier King Charles Spaniel wears his connection to British history in his breed's name. Cavaliers are the best of two worlds, combining the gentle attentiveness of a toy breed with the verve and athleticism of a sporting spaniel. The Cavalier's all-around beauty, regal grace, and even temper mark him as one of dogdom's noblemen. A toy spaniel no more than 13 inches high, the Cavalier draws you in with his face: The sweet, gentle, melting expression emanating from large, round eyes is a breed hallmark. Another is the silky, richly colored coat that can be one of four distinct varieties (described in this page's History section). Cavaliers may be aristocrats, but they gladly descend from their royal high horse for a backyard frolic or a squirrel chase. They get along nicely with children and other dogs. Adaptable Cavaliers do equally well with active owners and homebodies'¿they can be upbeat athletes or shameless couch potatoes, depending on an owner's lifestyle.",

        ),
        Breed(
            name='Doberman Pinscher',
            breed_group=3,
            personality=['Fearless', 'Loyal', 'Alert'],
            avg_height={
                'males': '26-28 inches',
                'females': '24-26 inches'
            },
            avg_weight={
                'males': '75-100 pounds',
                'females': '60-90 pounds'
            },
            avg_life_exp='10-12 years',
            breed_video='https://youtu.be/HNYyLPkUaMA?t=9',

            description="Sleek and powerful, possessing both a magnificent physique and keen intelligence, the Doberman Pinscher is one of dogkind's noblemen. This incomparably fearless and vigilant breed stands proudly among the world's finest protection dogs. Dobermans are compactly built dogs'¿muscular, fast, and powerful'¿standing between 24 to 28 inches at the shoulder. The body is sleek but substantial, and is covered with a glistening coat of black, blue, red, or fawn, with rust markings. These elegant qualities, combined with a noble wedge-shaped head and an easy, athletic way of moving, have earned Dobermans a reputation as royalty in the canine kingdom. A well-conditioned Doberman on patrol will deter all but the most foolish intruder.",

        ),
        Breed(
            name='Miniature Schnauzer',
            breed_group=4,
            personality=['Friendly', 'Smart', 'Obedient'],
            avg_height={
                'males': '12-14 inches',
                'females': '12-14 inches'
            },
            avg_weight={
                'males': '11-20 pounds',
                'females': '11-20 pounds'
            },
            avg_life_exp='12-15 years',
            breed_video='https://youtu.be/xe8gIVqjeRQ',

            description="The Miniature Schnauzer, the smallest of the three Schnauzer breeds, is a generally healthy, long-lived, and low-shedding companion. Add an outgoing personality, a portable size, and sporty good looks, and you've got an ideal family dog. Stocky, robust little dogs standing 12 to 14 inches, Miniature Schnauzers were bred down from their larger cousins, Standard Schnauzers. The bushy beard and eyebrows give Minis a charming, human-like expression. The hard, wiry coat comes in three color patterns: salt and pepper, black and silver, and solid black. Created to be all-around farm dogs and ratters, they are tough, muscular, and fearless without being aggressive. The Miniature Schnauzer is a bright, friendly, trainable companion, small enough to adapt to apartment life but tireless enough to patrol acres of farmland. They get along well with other animals and kids. Minis are sturdy little guys and enjoy vigorous play. Home and family oriented, they make great watchdogs.",

        ),
        Breed(
            name='Shih Tzu',
            breed_group=5,
            personality=['Affectionate', 'Playful', 'Outgoing'],
            avg_height={
                'males': '9-10.5 inches',
                'females': '9-10.5 inches'
            },
            avg_weight={
                'males': '9-16 pounds',
                'females': '9-16 pounds'
            },
            avg_life_exp='10-18 years',
            breed_video='https://youtu.be/XwWoYElh4lI',

            description="That face! Those big dark eyes looking up at you with that sweet expression! It's no surprise that Shih Tzu owners have been so delighted with this little 'Lion Dog' for a thousand years. Where Shih Tzu go, giggles and mischief follow. Shi Tsu (pronounced in the West 'sheed-zoo' or 'sheet-su'; the Chinese say 'sher-zer'), weighing between 9 to 16 pounds, and standing between 8 and 11 inches, are surprisingly solid for dogs their size. The coat, which comes in many colors, is worth the time you will put into it'¿few dogs are as beautiful as a well-groomed Shih Tzu. Being cute is a way of life for this lively charmer. The Shih Tzu is known to be especially affectionate with children. As a small dog bred to spend most of their day inside royal palaces, they make a great pet if you live in an apartment or lack a big backyard. Some dogs live to dig holes and chase cats, but a Shih Tzu's idea of fun is sitting in your lap acting adorable as you try to watch TV.",

        ),
        Breed(
            name='Boston Terrier',
            breed_group=6,
            personality=['Friendly', 'Bright', 'Amusing'],
            avg_height={
                'males': '15-17 inches',
                'females': '15-17 inches'
            },
            avg_weight={
                'males': '12-25 pounds',
                'females': '12-25 pounds'
            },
            avg_life_exp='11-13 years',
            breed_video='https://youtu.be/G3dWns5n21s',

            description="The Boston Terrier is a lively little companion recognized by his tight tuxedo jacket, sporty but compact body, and the friendly glow in his big, round eyes. His impeccable manners have earned him the nickname 'The American Gentleman.' Boston Terriers are compact, short-tailed, well-balanced little dogs weighing no more than 25 pounds. The stylish 'tuxedo' coat can be white and either black, brindle, or seal (dark brown). The head is square, the muzzle is short, and the large, round eyes can shine with kindness, curiosity, or mischief. Ever alert to their surroundings, Bostons move with a jaunty, rhythmic step. It's a safe bet that a breed named for a city'¿the Havanese or Brussels Griffon, for instance'¿will make an excellent urban pet. Bostons are no exception: they are sturdy but portable, people-oriented, and always up for a brisk walk to the park or outdoor cafe. A bright dog with a natural gift for comedy, the dapper Bostonian is a steady source of smiles.",

        ),
        Breed(
            name='Bernese Mountain Dog',
            breed_group=3,
            personality=['Good-Natured', 'Calm', 'Strong'],
            avg_height={
                'males': '25-27.5 inches',
                'females': '23-26 inches'
            },
            avg_weight={
                'males': '80-115 pounds',
                'females': '70-95 pounds'
            },
            avg_life_exp='7-10 years',
            breed_video='',

            description="Big, powerful, and built for hard work, the Bernese Mountain Dog is also strikingly beautiful and blessed with a sweet, affectionate nature. Berners are generally placid but are always up for a romp with the owner, whom they live to please. The Bernese Mountain Dog is a large, sturdy worker who can stand over 27 inches at the shoulder. The thick, silky, and moderately long coat is tricolored: jet black, clear white, and rust. The distinctive markings on the coat and face are breed hallmarks and, combined with the intelligent gleam in the dark eyes, add to the Berner's aura of majestic nobility. A hardy dog who thrives in cold weather, the Berner's brain and brawn helped him multitask on the farms and pastures of Switzerland. Berners get along with the entire family and are particularly gentle with children, but they will often become more attached to one lucky human. Berners are imposing but not threatening, and they maintain an aloof dignity with strangers.",

        ),
        Breed(
            name='Pomeranian',
            breed_group=5,
            personality=['Lively', 'Inquisitive', 'Bold'],
            avg_height={
                'males': '6-7 inches',
                'females': '6-7 inches'
            },
            avg_weight={
                'males': '3-7 pounds',
                'females': '3-7 pounds'
            },
            avg_life_exp='12-16 years',
            breed_video='https://youtu.be/jmaI3YWmbN0',

            description="The tiny Pomeranian, long a favorite of royals and commoners alike, has been called the ideal companion. The glorious coat, smiling, foxy face, and vivacious personality have helped make the Pom one of the world's most popular toy breeds. ¿The Pomeranian combines a tiny body (no more than seven pounds) and a commanding big-dog demeanor. The abundant double coat, with its frill extending over the chest and shoulders, comes in almost two dozen colors, and various patterns and markings, but is most commonly seen in orange or red. Alert and intelligent, Pomeranians are easily trained and make fine watchdogs and perky pets for families with children old enough to know the difference between a toy dog and a toy. Poms are active but can be exercised with indoor play and short walks, so they are content in both the city and suburbs. They will master tricks and games with ease, though their favorite activity is providing laughs and companionship to their special human.",

        ),
        Breed(
            name='Havanese',
            breed_group=5,
            personality=['Intelligent', 'Outgoing', 'Funny'],
            avg_height={
                'males': '8.5-11.5 inches',
                'females': '8.5-11.5 inches'
            },
            avg_weight={
                'males': '7-13 pounds',
                'females': '7-13 pounds'
            },
            avg_life_exp='14-16 years',
            breed_video='https://youtu.be/8VyL0SAVQ7s',

            description="Havanese, the only dog breed native to Cuba, are cheerful little dogs with a spring in their step and a gleam in their big, brown eyes. These vivacious and sociable companions are becoming especially popular with American city dwellers. ¿Distinctive features of the Havanese include a curled-over tail and a gorgeous silky coat, which comes in a variety of colors. Some owners enjoy cording the coat, in the manner of a Puli, and others clip it short to reduce grooming time. Happily, Havenese are just as cute no matter what hairdo you give them. Their small but sturdy bodies, adaptable nature, and social skills make Havanese an ideal city dog, but they are content to be anywhere that they can command the attention of admirers young and old alike. Havanese, smart and trainable extroverts with the comic instincts of a born clown, are natural trick dogs. Havanese are also excellent watchdogs and take the job seriously, but will usually keep the barking to a minimum.",

        ),
        Breed(
            name='English Springer Spaniel',
            breed_group=1,
            personality=['Friendly', 'Playful', 'Obedient'],
            avg_height={
                'males': '20 inches',
                'females': '19 inches'
            },
            avg_weight={
                'males': '50 pounds',
                'females': '40 pounds'
            },
            avg_life_exp='12-14 years',
            breed_video='https://youtu.be/kvJWumK34AI',

            description="The English Springer Spaniel is a sweet-faced, lovable bird dog of great energy, stamina, and brains. Sport hunters cherish the duality of working Springers: handsome, mannerly pets during the week, and trusty hunting buddies on weekends. Built for long days in the field, English Springer Spaniels are tough, muscular hunters standing 19 to 20 inches at the shoulder and weighing between 40 and 50 pounds. The double coat comes in several colors and patterns, the ears are long and lush, and the kindly, trusting expression of the eyes is a cherished hallmark of the breed. Springers move with a smooth, ground-covering stride. Bred to work closely with humans, Springers are highly trainable people-pleasers. They crave company and are miserable when neglected. Polite dogs, Springers are good with kids and their fellow mammals. They are eager to join in any family activity. Long walks, games of chase and fetch, and swimming are favorite pastimes of these rugged spaniels.",

        ),
        Breed(
            name='Shetland Sheepdog',
            breed_group=7,
            personality=['Playful', 'Entergetic', 'Bright'],
            avg_height={
                'males': '13-16 inches',
                'females': '13-16 inches'
            },
            avg_weight={
                'males': '15-25 pounds',
                'females': '15-25 pounds'
            },
            avg_life_exp='12-14 years',
            breed_video='https://youtu.be/yCarFtHnAeo',

            description="The Shetland Sheepdog, also known as the Sheltie, is an extremely intelligent, quick, and obedient herder from Scotland's remote and rugged Shetland Islands. Shelties bear a strong family resemblance to their bigger cousin, the Collie. The Shetland Sheepdog is a small, active, and agile herding dog standing between 13 and 16 inches at the shoulder. The long coat is harsh and straight, with a dense undercoat, and comes in black, blue merle, and sable, with white markings. The coat, along with a long, wedge-shaped head; small, three-quarter erect ears; and deep-chested, level-backed torso, give Shelties the look of a rough-coated Collie in miniature. Bright and eager Shelties are easy trainers and world-class competitors in obedience, agility, and herding trials. They are sensitive and affectionate family dogs, highly in tune with the mood of the household. They like to bark and tend to be reserved toward strangers'¿two qualifications of an excellent watchdog.",

        ),
        Breed(
            name='Brittany',
            breed_group=1,
            personality=['Bright', 'Fun-Loving', 'Upbeat'],
            avg_height={
                'males': '17.5-20.5 inches',
                'females': '17.5-20.5 inches'
            },
            avg_weight={
                'males': '30-40 pounds',
                'females': '30-40 pounds'
            },
            avg_life_exp='12-14 years',
            breed_video='https://youtu.be/yYhRKmwCGBQ',

            description="Sportsmen on both sides of the Atlantic cherish the agile, energetic Brittany as a stylish and versatile gundog. Bright and eager at home, and tireless afield, Brittanys require a lot of exercises, preferably with their favorite humans. Brittanys are smaller than setters but leggier than spaniels, standing about 20 inches at the shoulder. Their beautiful, boldly patterned coat comes in combinations of white and vivid orange and liver (reddish-brown). They are rugged and strong but smooth, clean, and quick afoot. The face has the 'softness' prized by bird-dog lovers; high-set ears convey the breed's essential eagerness. The zeal and versatility that make Brittanys peerless hunters can be channeled into dog sports. Obedience, agility, flyball, dock diving'¿you name it, this trainable breed is up for it. The Brittany is a nice fit for those seeking an all-purpose hunting partner, a dog-sport teammate, or a companion in sync with an upbeat, outdoorsy family life.",

        ),
        Breed(
            name='Miniature American Shepherd',
            breed_group=7,
            personality=['Intelligent', 'Good-Natured', 'Devoted'],
            avg_height={
                'males': '14-18 inches',
                'females': '13-17 inches'
            },
            avg_weight={
                'males': '20-40 pounds',
                'females': '20-40 pounds'
            },
            avg_life_exp='12-13 years',
            breed_video='https://youtu.be/sW5BY0gnJSA?t=14',

            description="The Miniature American Shepherd resembles a small Australian Shepherd. True herders in spite of their compact size, Minis are bright, self-motivated workers and endearingly loyal and lively companion dogs who have an affinity for horses. The Miniature American Shepherd shares many physical traits with its forebear the Australian Shepherd'¿only on a smaller scale. Females stand between 13 and 17 inches at the shoulder; males range from 14 to 18 inches. Despite their size, Minis are every inch a true herding dog: energetic, versatile, rugged, and extremely bright. The eye-catching coat comes in black, blue merle, red, and red merle. (The merle will exhibit in any amount marbling, flecks, or blotches.) Minis move with the smooth and agile step of a dog built for hard work on punishing terrain.",

        ),
        Breed(
            name='Border Collie',
            breed_group=7,
            personality=['Affectionate', 'Smart', 'Energetic'],
            avg_height={
                'males': '19-22 inches',
                'females': '18-21 inches'
            },
            avg_weight={
                'males': '30-55 pounds',
                'females': '30-55 pounds'
            },
            avg_life_exp='12-15 years',
            breed_video='https://youtu.be/NeqHSKTqffI',

            description="A remarkably bright workaholic, the Border Collie is an amazing dog'¿maybe a bit too amazing for owners without the time, energy, or means to keep it occupied. These energetic dogs will settle down for cuddle time when the workday is done. Borders are athletic, medium-sized herders standing 18 to 22 inches at the shoulder. The overall look is that of a muscular but nimble worker unspoiled by passing fads. Both the rough coat and the smooth coat come in a variety of colors and patterns. The almond eyes are the focus of an intelligent expression'¿an intense gaze, the Border's famous 'herding eye', is a breed hallmark. On the move, Borders are among the canine kingdom's most agile, balanced, and durable citizens. The intelligence, athleticism, and trainability of Borders have a perfect outlet in agility training. Having a job to perform, like agility'¿or herding or obedience work'¿is key to Border happiness. Amiable among friends, they may be reserved with strangers.",

        ),
        Breed(
            name='Chihuahua',
            breed_group=5,
            personality=['Charming', 'Graceful', 'Sassy'],
            avg_height={
                'males': '5-8 inches',
                'females': '5-8 inches'
            },
            avg_weight={
                'males': 'not exceeding 6 pounds',
                'females': 'not exceeding 6 pounds'
            },
            avg_life_exp='14-16 years',
            breed_video='https://youtu.be/dHX2xul3WEk',

            description="The Chihuahua is a tiny dog with a huge personality. A national symbol of Mexico, these alert and amusing \"purse dogs\" stand among the oldest breeds of the Americas, with a lineage going back to the ancient kingdoms of pre-Columbian times. The Chihuahua is a balanced, graceful dog of terrier-like demeanor, weighing no more than 6 pounds. The rounded \"apple\" head is a breed hallmark. The erect ears and full, luminous eyes are acutely expressive. Coats come in many colors and patterns, and can be long or short. The varieties are identical except for coat. Chihuahuas possess loyalty, charm, and big-dog attitude. Even tiny dogs require training, and without it this clever scamp will rule your household like a little Napoleon. Compact and confident, Chihuahuas are ideal city pets. They are too small for roughhousing with kids, and special care must be taken in cold weather, but Chihuahuas are adaptable'¿as long as they get lots of quality time in their preferred lap.",

        ),
        Breed(
            name='Vizsla',
            breed_group=1,
            personality=['Affectionate', 'Energetic', 'Gentle'],
            avg_height={
                'males': '22-24 inches',
                'females': '21-23 inches'
            },
            avg_weight={
                'males': '55-60 pounds',
                'females': '44-55 pounds'
            },
            avg_life_exp='12-14 years',
            breed_video='https://youtu.be/wLTdf8k5KcQ',

            description="The Vizsla is a versatile, red-coated gundog built for long days in the field. For centuries these rugged but elegant athletes have been the pride of Hungarian sportsmen, and their popularity in America increases with each passing year. The Vizsla is easily recognized by his sleek golden-rust coat. They can stand between 21 to 24 inches at the shoulder and are the picture of a lean, light-footed hunter's companion. The long, silky ears frame a facial expression that is sensitive and loving around the house and intense when at work. As a hunter expected to work closely with humans, Vizslas form a tight bond with their owners and hate to be left alone. Athletes of many talents, Vizslas excel at various sports and activities. They are eager and graceful trotters of great stamina, making them ideal jogging or biking companions. An expert on the breed tells us, 'If you don't have the time to encourage this breed's full use of its brain, you're wasting a good dog.'",

        ),
        Breed(
            name='Basset Hound',
            breed_group=2,
            personality=['Charming', 'Patient', 'Low-Key'],
            avg_height={
                'males': 'up to 15 inches',
                'females': '40-65 pounds'
            },
            avg_weight={
                'males': '40-65 pounds',
                'females': '40-65 pounds'
            },
            avg_life_exp='12-13 years',
            breed_video='https://youtu.be/pHJ8JRHAFlE',

            description="Among the most appealing of the AKC breeds, the endearing and instantly recognizable Basset Hound is a perennial favorite of dog lovers all over the world. This low-slung and low-key hound can be sometimes stubborn, but is always charming. The Basset Hound stands no higher than 14 inches at the shoulder but, with his remarkably heavy bone, powerful little legs, and massive paws, he possesses big-dog strength and stamina. Bassets are famous for a large, domed head that features extremely long, velvety ears, mournful eyes, and a wrinkled brow, which give the breed the look of a sad clown. Built more for endurance than speed, the Basset moves in a deliberate but effortless manner. The breed's scenting ability is uncanny; it's said that among dogs only the Bloodhound's nose is more accurate. Mild and agreeable at home, the Basset is stubborn on the trail and barks in a loud, ringing voice. Although they may not be wildly demonstrative in their affections, they are steadfastly loyal.",

        ),
        Breed(
            name='Belgian Malinois',
            breed_group=7,
            personality=['Confident', 'Smart', 'Hardworking'],
            avg_height={
                'males': '24-26 inches',
                'females': '22-24 inches'
            },
            avg_weight={
                'males': '60-80 pounds',
                'females': '40-60 pounds'
            },
            avg_life_exp='14-16 years',
            breed_video='https://youtu.be/roC80WTQSLM?t=11',

            description="The smart, confident, and versatile Belgian Malinois is a world-class worker who forges an unbreakable bond with his human partner. To deny a Mal activity and the pleasure of your company is to deprive him of his very reasons for being. Belgian Malinois are squarely built, proud, and alert herders standing 22 to 26 inches. Strong and well-muscled, but more elegant than bulky, there's an honest, no-frills look about them, as befit dogs built to work hard for their feed. A breed hallmark is the proud carriage of the head. Coat colors range from a rich fawn to mahogany. The black ears and mask accentuate bright, questioning eyes the color of dark Belgian chocolate. If you have ever seen a Mal perform an obedience routine, you know firsthand what a smart and eager breed this is. Problems set in, though, when this people-oriented dog is underemployed and neglected. Exercise, and plenty of it, preferably side by side with their adored owner, is key to Mal happiness.",

        ),
        Breed(
            name='Maltese',
            breed_group=5,
            personality=['Playful', 'Charming', 'Gentle'],
            avg_height={
                'males': '7-9 inches',
                'females': '7-9 inches'
            },
            avg_weight={
                'males': 'under 7 pounds',
                'females': 'under 7 pounds'
            },
            avg_life_exp='12-15 years',
            breed_video='https://youtu.be/tRA2W1D0PTc',

            description="The tiny Maltese, 'Ye Ancient Dogge of Malta,' has been sitting in the lap of luxury since the Bible was a work in progress. Famous for their show-stopping, floor-length coat, Maltese are playful, charming, and adaptable toy companions. Maltese are affectionate toy dogs weighing less than seven pounds, covered by a long, straight, silky coat. Beneath the all-white mantle is a compact body moving with a smooth and effortless gait. The overall picture depicts free-flowing elegance and balance. The irresistible Maltese face'¿with its big, dark eyes and black gumdrop nose'¿can conquer the most jaded sensibility. Despite their aristocratic bearing, Maltese are hardy and adaptable pets. They make alert watchdogs who are fearless in a charming toy-dog way, and they are game little athletes on the agility course. Maltese are low-shedding, long-lived, and happy to make new friends of all ages. Sometimes stubborn and willful, they respond well to rewards-based training.",

        ),
        Breed(
            name='Weimaraner',
            breed_group=1,
            personality=['Fearless', 'Friendly','Obedient'],
            avg_height={
                'males': '25-27 inches',
                'females': '23-25 inches'
            },
            avg_weight={
                'males': '70-90 pounds',
                'females': '55-75 pounds'
            },
            avg_life_exp='10-13 years',
            breed_video='https://youtu.be/VUxM2qEZZFU',

            description="The Weimaraner, Germany's sleek and swift 'Gray Ghost,' is beloved by hunters and pet owners alike for their friendliness, obedience, and beauty. They enjoy exercise, and plenty of it, along with lots of quality time with their humans. Instantly recognized by a distinctive silvery-gray coat, male Weimaraners stand 25 to 27 inches at the shoulder, and females 23 to 25 inches. A properly bred Weimaraner will be solid colored, with maybe a small white spot on the chest. The face, with its amber or blue-gray eyes framed by long velvety ears, is amiable and intelligent. Overall, the breed presents a picture of streamlined grace and balance. A well-conditioned Weimaraner on point is a breathtaking sight. Weimaraners are excellent with kids and yearn to be full-fledged family members. Easy grooming, trainability, a loving nature, and a can-do-attitude make them excellent pets, as long as owners are committed to keeping them physically active and mentally engaged.",

        ),
        Breed(
            name='Collie',
            breed_group=7,
            personality=['Devoted', 'Graceful', 'Proud'],
            avg_height={
                'males': '24-26 inches',
                'females': '22-24 inches'
            },
            avg_weight={
                'males': '60-75 pounds',
                'females': '50-65 pounds'
            },
            avg_life_exp='12-14 years',
            breed_video='https://youtu.be/ZoFze0O_epE?t=9',

            description="The majestic Collie, thanks to a hundred years as a pop-culture star, is among the world's most recognizable and beloved dog breeds. The full-coated 'rough' Collie is the more familiar variety, but there is also a sleek 'smooth' Collie. The Collie is a large but lithe herder standing anywhere from 22 to 26 inches tall. The rough variety boasts one of the canine kingdom's most impressively showy coats; the smooth coat's charms are subtler but no less satisfying. Coat colors in both varieties are sable and white, tricolor, blue merle, or white. Collie fanciers take pride in their breed's elegant wedge-shaped head, whose mobile ears and almond eyes convey a wide variety of expressions. Collies are famously fond of children and make wonderful family pets. These swift, athletic dogs thrive on companionship and regular exercise. With gentle training, they learn happily and rapidly. The Collie's loyalty, intelligence, and sterling character are the stuff of legend.",

        ),
        Breed(
            name='Newfoundland',
            breed_group=3,
            personality=['Sweet', 'Patient', 'Devoted'],
            avg_height={
                'males': '28 inches',
                'females': '26 inches'
            },
            avg_weight={
                'males': '130-150 pounds',
                'females': '100-120 pounds'
            },
            avg_life_exp='9-10 years',
            breed_video='https://youtu.be/OkGujZAIRnA?t=12',

            description="The massive Newfoundland is a strikingly large, powerful working dog of heavy bone and dignified bearing. The sweet-tempered Newfie is a famously good companion and has earned a reputation as a patient and watchful 'nanny dog' for kids. A male Newfoundland can weigh up to 150 pounds and stand 28 inches at the shoulder; females typically go 100 to 120 pounds. The Newf head is majestic, the expression soft and soulful. The outer coat is flat and coarse. Colors are gray, brown, black, and a black-and-white coat named for artist Sir Edwin Landseer, who popularized the look in his paintings. The Newfie breed standard says that a sweet temperament is the 'most important single characteristic of the breed.' The Newf's sterling character is expressed in their affinity for kids. Trusting and trainable, Newfs respond well to gentle guidance. These noble giants are among the world's biggest dogs, and acquiring a pet that could outweigh you comes with obvious challenges.",

        ),
        Breed(
            name='Rhodesian Ridgeback',
            breed_group=2,
            personality=['Dignified', 'Affectionate', 'Even-Tempered'],
            avg_height={
                'males': '25-27 inches',
                'females': '24-26 inches'
            },
            avg_weight={
                'males': '85 pounds',
                'females': '70 pounds'
            },
            avg_life_exp='9-10 years',
            breed_video='https://youtu.be/CvObRdhZ5L8?t=10',

            description="The Rhodesian Ridgeback is an all-purpose 'Renaissance hound' whose hallmark is the ridge, or stripe of backward-growing hair, on his back. Though the breed was made famous in its native Africa for its skill at tracking and baying '¿ but never, ever killing '¿ lions, today Ridgebacks are cherished family dogs whose owners must be prepared to deal with their independence and strong prey drive Beneath the Ridgeback's trademark ridge is a whole lot of hound: Ridgebacks are fast and powerful athletes who can weigh between 70 and 85 pounds, and oftentimes more. They come in only one color '¿ wheaten '¿ which spans every shade seen in a wheat field, from pale flaxen to the burnished red of a maturing crop. Ridgebacks also have two nose colors: black and the less commonly seen brown. The formidable Ridgeback can be strong willed, independent, and sometimes domineering. Ridgebacks must be guided with a firm but fair hand from puppyhood. They are faithful friends, protective of their loved ones and meltingly affectionate with those whom they trust. Still, a Ridgeback can be too much hound for the novice dog owner.",

        ),
        Breed(
            name='Shiba Inu',
            breed_group=6,
            personality=['Alert', 'Active', 'Attentive'],
            avg_height={
                'males': '14.5-16.5 inches',
                'females': '13.5-15.5 inches'
            },
            avg_weight={
                'males': '23 pounds',
                'females': '17 pounds'
            },
            avg_life_exp='13-16 years',
            breed_video='https://youtu.be/lSMAUTvRdwg',

            description="An ancient Japanese breed, the Shiba Inu is a little but well-muscled dog once employed as a hunter. Today, the spirited, good-natured Shiba is the most popular companion dog in Japan. The adaptable Shiba is at home in town or country. Brought to America from Japan as recently as 60 years ago, Shibas are growing in popularity in the West and are already the most popular breed in their homeland. Their white markings combined with their coloring (red, red sesame, or black and tan) and their alert expression and smooth stride makes them almost foxlike. They're sturdy, muscular dogs with a bold, confident personality to match.",

        ),
        Breed(
            name='West Highland White Terrier',
            breed_group=4,
            personality=['Loyal', 'Happy', 'Entertaining'],
            avg_height={
                'males': '11 inches ',
                'females': '10 inches'
            },
            avg_weight={
                'males': '15-20 pounds',
                'females': '15-20 pounds'
            },
            avg_life_exp='13-15 years',
            breed_video='https://youtu.be/sldzFjl5y8Y',

            description="Smart, confident, and always entertaining at play, the adorable West Highland White Terrier (Westie, for short) has charmed owners for over 300 years. This diminutive but sturdy earthdog is among the most popular of the small terriers. Standing 10 to 11 inches at the shoulder, with dark piercing eyes, compact body, and a carrot-shaped tail wagging with delight, the Westie's looks are irresistible. Beneath the plush-toy exterior, though, is a true working terrier of gameness and courage. Bred to hunt rats and other underground rodents, Westies are surprisingly strong and tough. The all-white double coat is hard to the touch, not soft and fluffy. Alert and active, Westies exhibit traits of a plucky and self-reliant ratting terrier: They require no pampering, they will chase after anything that moves, and their independence can make training a challenge. But, thanks to their faithfulness and keen intelligence, Westies will train nicely with time and patience.",

        ),
        Breed(
            name='Bichon Frise',
            breed_group=6,
            personality=['Playful', 'Curious', 'Peppy'],
            avg_height={
                'males': '9.5-11.5 inches',
                'females': '9.5-11.5 inches'
            },
            avg_weight={
                'males': '12-18 pounds',
                'females': '12-18 pounds'
            },
            avg_life_exp='14-15 years',
            breed_video='https://youtu.be/9uwW-7VzjBY',

            description="The small but sturdy and resilient Bichon Frise stands among the world's great 'personality dogs.' Since antiquity, these irresistible canine comedians have relied on charm, beauty, and intelligence to weather history's ups and downs. A good-size Bichon will stand a shade under a foot tall at the shoulder. The breed's glory is a white hypoallergenic coat, plush and velvety to the touch, featuring rounded head hair that sets off the large, dark eyes and black leathers of the nose and lips. Bichons are adaptable companions who get on well with other dogs and children. Alert and curious, Bichons make nice little watchdogs'¿but they are lovers, not fighters, and operate under the assumption that there are no strangers, just friends they haven't met yet. Their confidence and size make them ideal city dogs. Bichons train nicely and enjoy performing for their loved ones. Finally, there's the happy-go-lucky Bichon personality that draws smiles and hugs wherever they go.",

        ),
        Breed(
            name='Bloodhound',
            breed_group=2,
            personality=['Independent', 'Friendly', 'Inquisitive'],
            avg_height={
                'males': '25-27 inches',
                'females': '23-25 inches'
            },
            avg_weight={
                'males': '90-110 pounds',
                'females': '80-100 pounds'
            },
            avg_life_exp='10-12 years',
            breed_video='https://youtu.be/nFGMVsDEAXQ?t=10',

            description="The world-famous 'Sleuth Hound' does one thing better than any creature on earth: find people who are lost or hiding. An off-duty Bloodhound is among the canine kingdom's most docile citizens, but he's relentless and stubborn on a scent. Bloodhounds are large, substantial dogs standing 23 to 27 inches at the shoulder and weighing up to 110 pounds. Their most famous features are a long, wrinkled face with loose skin huge, drooping ears and warm, deep-set eyes that complete an expression of solemn dignity. Coat colors can be black and tan, liver and tan, or red. Powerful legs allow Bloodhounds to scent over miles of punishing terrain. As pack dogs, Bloodhounds enjoy company, including other dogs and kids. They are easygoing, but their nose can sometimes lead them into trouble. A strong leash and long walks in places where they can enjoy sniffing around are recommended. Bloodhounds are droolers, and obedience training these sensitive sleuths can be a challenge.",

        ),
        Breed(
            name='Portuguese Water Dog',
            breed_group=3,
            personality=['Affectionate', 'Adventurous', 'Athletic'],
            avg_height={
                'males': '20-23 inches',
                'females': '17-21 inches'
            },
            avg_weight={
                'males': '42-60 pounds',
                'females': '35-50 pounds'
            },
            avg_life_exp='11-13 years',
            breed_video='https://youtu.be/ekZq6y9GBa0',

            description="The bright and biddable Portuguese Water Dog was bred to be an all-around fisherman's helper. The robust, medium-sized body is covered by a coat of tight, low-shedding curls. PWDs are eager and athletic companions built for water work. The Portuguese Water Dog is super-smart and very 'biddable''¿meaning he's easy to train and eager to please. The Portie can be groomed in two styles: The retriever clip (the entire coat is clipped to one inch in length, with the tail tip at full length) or the more check-me-out lion clip, where the coat on the hindquarters and muzzle is clipped down to the skin.",

        ),
        Breed(
            name='Chesapeake Bay Retriever',
            breed_group=1,
            personality=['Affectionate', 'Bright', 'Sensitive'],
            avg_height={
                'males': '23-26 inches',
                'females': '21-24 inches'
            },
            avg_weight={
                'males': '65-80 pounds',
                'females': '55-70 pounds'
            },
            avg_life_exp='10-13 years',
            breed_video='https://youtu.be/DGD4CLYPCrk?t=11',

            description="The Chesapeake Bay Retriever, peerless duck dog of the Mid-Atlantic, is an American original who embodies the classic traits of a good retriever: loyal, upbeat, affectionate, and tireless. The Chessie is famous for his waterproof coat. Chessies are strong, powerfully built gundogs standing anywhere from 21 to 26 inches at the shoulder. A male can weigh up to 80 pounds. The distinctive breed trait is a wavy coat that is oily to the touch. Chessies are solid-colored, either chocolatey brown, sedge, or deadgrass, with keen yellow-amber eyes that nicely complement the coat. Chessies are more emotionally complex than the usual gundog. Chessies take to training, but they have a mind of their own and can tenaciously pursue their own path. They are protective of their humans and polite, but not overtly friendly, to strangers. Chessies make excellent watchdogs and are versatile athletes. A well-socialized Chessie is a confident companion and world-class hunting buddy.",

        ),
        Breed(
            name='Dalmatian',
            breed_group=6,
            personality=['Dignified', 'Smart', 'Outgoing'],
            avg_height={
                'males': '19-24 inches',
                'females': '19-24 inches'
            },
            avg_weight={
                'males': '45-70 pounds',
                'females': '45-70 pounds'
            },
            avg_life_exp='11-13 years',
            breed_video='https://youtu.be/N5YnYYSxjYI?t=10',

            description="The dignified Dalmatian, dogdom's citizen of the world, is famed for his spotted coat and unique job description. During their long history, these \"coach dogs\" have accompanied the horse-drawn rigs of nobles, gypsies, and firefighters. The Dalmatian's delightful, eye-catching spots of black or liver adorn one of the most distinctive coats in the animal kingdom. Beneath the spots is a graceful, elegantly proportioned trotting dog standing between 19 and 23 inches at the shoulder. Dals are muscular, built to go the distance; the powerful hindquarters provide the drive behind the smooth, effortless gait. The Dal was originally bred to guard horses and coaches, and some of the old protective instinct remains. Reserved and dignified, Dals can be aloof with strangers and are dependable watchdogs. With their preferred humans, Dals are bright, loyal, and loving house dogs. They are strong, active athletes with great stamina'¿a wonderful partner for runners and hikers.",

        ),
        Breed(
            name='Saint Bernard',
            breed_group=3,
            personality=['Playful', 'Charming', 'Inquisitive'],
            avg_height={
                'males': '28-30 inches',
                'females': '26-28 inches'
            },
            avg_weight={
                'males': '140-180 pounds',
                'females': '120-140 pounds'
            },
            avg_life_exp='8-10 years',
            breed_video='https://youtu.be/8va0ZbLM4iE',

            description="The Saint Bernard does not rank very high in AKC registrations, but the genial giant of the Swiss Alps is nonetheless among the world's most famous and beloved breeds. Saints are famously watchful and patient 'nanny dogs' for children. Not ranked particularly high in AKC registrations, this genial giant is nonetheless among the world's most famous and beloved breeds. The Saint's written standard abounds with phrases like 'very powerful,' 'extraordinarily muscular,' 'imposing,' and 'massive.' A male stands a minimum 27.5 inches at the shoulder; females will be smaller and more delicately built. The huge head features a wrinkled brow, a short muzzle, and dark eyes, combining to give Saints the intelligent, friendly expression that was such a welcome sight to stranded Alpine travelers.",

        ),
        Breed(
            name='Papillon',
            breed_group=5,
            personality=['Friendly', 'Alert', 'Happy'],
            avg_height={
                'males': '8-11 inches',
                'females': '8-11 inches'
            },
            avg_weight={
                'males': '5-10 pounds',
                'females': '5-10 pounds'
            },
            avg_life_exp='14-16 years',
            breed_video='https://youtu.be/VpphC5Y4K-4',

            description="The quick, curious Papillon is a toy dog of singular beauty and upbeat athleticism. Despite his refined appearance, the Pap is truly a 'doggy dog' blessed with a hardy constitution. Papillon fanciers describe their breed as happy, alert, and friendly. A tiny dog, measuring 8 to 11 inches at the shoulder, you can still spot a Papillon a block away thanks to the large, wing-shaped ears that give the breed its name ('papillon' is French for 'butterfly'). Some Paps have erect ears; in others, known as the Phalene type, the ears are down. Paps are dainty and elegant, with a plumed tail, and a long, silky coat of several color combinations, the base color being white. More robust than they look, Paps are little dogs for all seasons and reasons. They thrive in warm or cool climates, in town or country, and are eager to join family fun. They are excellent agility dogs and are consistent winners at the sport's highest levels; less ambitious owners can train them to do all kinds of tricks.",

        ),
        # Breed(
        #     name='',
        #     breed_group=,
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
        #     breed_video='',

        #     description="",

        # ),
        # Breed(
        #     name='',
        #     breed_group=,
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
        #     breed_video='',

        #     description="",

        # ),
        # Breed(
        #     name='',
        #     breed_group=,
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
        #     breed_video='',

        #     description="",

        # ),
        # Breed(
        #     name='',
        #     breed_group=,
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
        #     breed_video='',

        #     description="",

        # ),
        # Breed(
        #     name='',
        #     breed_group=,
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
        #     breed_video='',

        #     description="",

        # ),
        # Breed(
        #     name='',
        #     breed_group=,
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
        #     breed_video='',

        #     description="",

        # ),
        # Breed(
        #     name='',
        #     breed_group=,
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
        #     breed_video='',

        #     description="",

        # ),
        # Breed(
        #     name='',
        #     breed_group=,
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
        #     breed_video='',

        #     description="",

        # ),
        # Breed(
        #     name='',
        #     breed_group=,
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
        #     breed_video='',

        #     description="",

        # ),
        # Breed(
        #     name='',
        #     breed_group=,
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
        #     breed_video='',

        #     description="",

        # ),
        # Breed(
        #     name='',
        #     breed_group=,
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
        #     breed_video='',

        #     description="",

        # ),
        # Breed(
        #     name='',
        #     breed_group=,
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
        #     breed_video='',

        #     description="",

        # ),
        
    ]

            





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
    db.session.add_all(breeds)






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
    # breed_video = '',
# 
    #     description="",

    # )

   