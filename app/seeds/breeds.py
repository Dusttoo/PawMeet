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

   