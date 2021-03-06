from random import randint, randrange
from app.models import db, Post
from faker import Faker

from app.models.comment import Comment

titles = [
    'Acid reflux in dogs?', 'Tough toys?', 'Begging', 'Behavior Help',
    'Toilet Paper Snacks?', 'Fighting back', 'Yak Chews', 'Walking', 
    'Tiny dogs', 'Big Puppy', 'Husband or Dog?', 'Stubborn'

]

seeded_posts = [
    'Curious to know now that someone has mentioned it can a dog have acid reflux my girl has been sick off and on puking up bile the last few weeks and Friday I took her to the vet where they did an examination over her and said she was probably being picky, Friday night and Saturday she did really good taking her meds and eating the new food they told me to try out for a week. Fast forward to today and she puked up her food that was in her stomach and then puked probably another 5-6 times just acid and bile.',
    'Hi everyone!! So my dogs are Cane Corsos!! I need some opinion on chew toys for them. I just bought them new toys and they already ripped them up!!! So I’m looking to buy some more toys soon for them, any advice?',
    'Hi all.  This is two posts in one.  I have a very sweet 1 yo lab baby who recently started 1.) coming over to us while we are eating and gently puts his head on my leg and sweetly waits for food to drop/be given to him (which we don’t do and have never done, so I don’t know where this came from).  And 2.) alternates between banging on his food bowl and the pantry door when he thinks it’s time to eat (usually an hour early).  How do I work on curbing these weird (and not bad, but annoying) habits?  Could he need more food?   He definitely is in good shape and doesn’t need to gain more weight.',
    'Hi everyone! We adopted a 1.5 year old lab mix recently. This is my first dog I have adopted as an adult. The shelter had her for 4 months and it is clear she has had no real training. We were told she loves cats, dogs, kids, and adults. I know it\'s early and to expect a nervous pup until they are well adjusted, but I had a few questions. I don\'t want to do any harm to her gentle demeanor and it is clear she was abused at some point in her life. 1.) Picking up objects and walking towards her scares her(broom, vacuum hose, towel, etc.) She does not react, but looks fearful and I\'m not sure how to reassure her that she is safe in our home and we will do no harm to her. 2.) We live in a 3 story townhome. When myself or my fiancé come up or down the stairs to the floor she is on she runs and barks in the direction of the noise. Once she realizes it is us she is fine. I understand that she is scared and will take a while to adjust, but I am not sure how to gently curb this behavior. I want to assure her she/we are ok especially if we have friends over so she is not running and barking at them. 3.) My third question is she is supposedly good with all adults however, a male family friend came over last night, he has a beard, and she stood up on our couch barking and growling at him. She is only fearful of men with facial hair. What is the best way to redirect this behavior? Thank you for your advice! We are never going to give up on her and she is staying with us for life. We just need to work out a few little kinks',
    'My dachshund loves to eat toilet paper. We do a pretty good job keeping him out of the bathroom, but once in awhile, I forget and have a tissue in my picket. Any training tips?',
    "Long text, sorry in advanced lol. So if tl:dr basically my friend's small 10-15lbs dog has always growled/snapped at my larger 40-50lbs dog since we got her as a puppy and last night she finally had enough and started to fight back. No injuries, but now I'm worried. What would you do if this was your dog? - -- My friend has 2 tiny dogs(10-15 lbs ish) and I have 2 medium dogs(40-50 lbs). Back when my friend got their first tiny dog as a puppy(male) I already had one of my dogs(also male) and he's incredibly maturnal so he does amazing with puppies and small dogs so they became fast friends. Then they got their second dog (female) and same thing: great friends. But their older dog would growl and snap at their puppy until she got older and he got used to her and now they're fine. Then I got a second puppy(also female) not long after they got their second puppy and the 2 puppies were also fast friends to the point where they play together and it's super cute watching a tiny dog jump up on my bigger dog and she'll lay down for her, etc. But their first dog hates my younger dog from the beginning, just like how he used to treat their puppy. So every time we get together with our dogs their older dog is growling at my younger dog and snapped at her a few times, especially over toys/bones/etc. They just said oh yeah, he's really possessive but our puppy will take things right out of his mouth and he doesn't do anything about it so it's fine 🤨. I thought okay... As long as it's just all growl and no bite I guess? Then 2 visits ago in my house he really went after my younger dog after his owner threw a ball ( and they both ran to get the ball) to the point where the owner had to go pick him up so he would stop and my younger dog didn't do anything back so we said okay, no fetch around these dogs then and put the toys away and back to the regular growling. So last night they were over at my house again and their dog was growling at my younger dog again (she's just over a year now so not exactly a puppy anymore) but whatever, we're all used to it now. Until she brought one of her bones into the room and he went after her just like the time before and this time she responded: snarling, baring teeth, and looked like she was ready to fight him if he didn't back down but I knew he wouldn't back down so it was like this air fight between them but no actual contact (yet) so I pulled my dog away and we went into another room and closed  the door to calm down ( and meanwhile my friend put the bone into a different room so no one could get to it). And I thought... This is bad. This is getting worse and I can't have my dog injuring/killing a tiny dog since his entire head can fit in her mouth! And what if this causes my dog to suddenly think she needs to fight other dogs over her stuff? So I put a muzzle on her, which she's not used to and I did not train her in it properly (my older dog was trained on a muzzle so I could take him on the bus requirement in my area and so I could take him to my friend's farm that had chickens just in case. But my younger dog I never needed to and kinda forgot that it might be a thing we needed to do in the future so that's my bad) so my dog was pawing at the muzzle and visibly uncomfortable. But I thought... These people aren't going to watch/stop their dog unless I make a point. It worked: they told their dog to stop every time he growled and picked him up if he didn't stop growling then told me I could take the muzzle off of her and they would stop their dog. So our younger dogs got to play together without their other dog intervening. This entire time my older dog is in the other side of the room laying down with his ears back like \"I'm not getting involved in this BS\" lol, it must have made him feel pretty torn watching his 2 good friends fight. So now that we've gotten this far in the story lol... Wtf do I do now?? These people were my older dog's babysitter for years, and we babysit their dogs too, and if one of us is out late the other can drop into their house to tend to the dogs. It's a great set up we have going with them and they're only 5-10 minutes drive from us. We do have another friend who has a puppy that could mind our dogs too, but he lives in an apartment so not as much space as these friends plus he lives in a more city area with no private yard so he would have to walk 3 dogs to go potty/etc 😬. And it's further for us to drive to(45 minutes, longer if traffic). So I guess I'm asking for any advice dealing with my dog, dealing  with their dog, dealing with my friend... Or any similar situations you've been in so I don't feel alone. I feel bad because my dog is such a good dog and I let her get pushed too far but she clearly has a limit and I failed her by letting that happen... I don't want her to think she needs to fight other dogs or anything like that. I don't know what to do or what to think now. ",
    "Good morning! I have heard a lot about yak chews. I was wondering what everyone’s experience with them was. I hear they aren’t smelly but are they messy?  Do they leave a residue on the floor/carpet?  I have a 97 lb border collie GSD mix who LOVES to chew and absolutely destroys toys. Our local pet store stopped carrying his favorite large chew which was made my a local company - it was a “beef cheek rolll”. 🤢 Smelled gross but he loved it.  Anything else I can find is half the size & he will eat & try to swallow & choke on it in 10 minutes. I can’t find anything that lasts for him. Any suggestions would be great!",
    "My dogs both walk amazingly well alone - separate on walks (when I take one at a time) but whenever I try take both of them for a walk (I walk one my partner/ or friend walks the other) my younger boy goes crazy, he pulls, tries to run and he is a big boy so it’s hard to walk them together but I know I can help make it easier for us? On walks alone he is a dream to walk, he doesn’t pull, listens very well, sits at roads and everything (I did a lot of walk training since he was 8 weeks but not so often with both dogs together, he is now 12 months old and it’s never really gotten easier to walk both dogs together. Help? I think my younger boy just wants to ‘lead’ / be infront of our older dog ? 😅",
    "Ok help this isn’t much of a training question but I figured it’s related I have 2 gates and my 3 chihuahuas can walk right through these if I’m not watching them they get out…. Any ideas on fixing the problem It’s the gate the are squeezing past a new fence is out of the question as I have almost an acre My fence is not broken my dogs are literally 2lbs 🙃",
    "Looking for any advice My 11 month old male Neo has had 3 surgeries in 6 months and therefore has not gotten proper training/socializing during that time. I have 3 other dogs and trying to re-introduce him into the pack has been a nightmare. He has hurt 1 of my dogs by jumping on their back(playfully?) And caused a huge fight between him and 2 others when he tried bullying the alpha female. He also chews on anything wood and can't be left unsupervised for even 2 minutes. He will put down a raw meaty bone to chew wood baseboards 🙄 I live alone and work full time. Even if there were trainers in my area they either aren't affordable or aren't available for my schedule. I have resorted to keeping my neo separate from my other 3 dogs but this means he spends alot of time in a kennel because I can't devote as much time to JUST HIM. Shuffling dogs around for feedings and outings and all the baby gates and crate time is miserable and exhausting and time consuming and very impractical for long term. I need advice on ways to manage 4 dogs who don't get along and how to get a 135lb PUPPY to respect those smaller than him and eventually be able to be part of the pack without causing fights.",
    "Looking for suggestions for our Skip, in particular interacting with my husband. I have posted before, but we adopted a male chihuahua in March who was 14 mo. at the time. He was rescued from an animal hoarding situation and knew he had a huge fear of being caught. But we don’t know about particulars of trama he may have experienced, so is just a guess. He has a naturally super loving personality, now asks for pets and rubs(huge milestone when that happened🥰), has always been so fun and playful and energetic, is very food driven, is doing well on a leash, is very smart and extremely observant, just an all round fun dog to have! He has come SO far, and we are so incredibly proud of him! We have used a whole lot of positive reinforcement and let time work. I am the primary care taker of our dogs, I feed almost always and take out to play and walk. My husband is around a lot though and plays and interacts with them lovingly. Our two females are definitely “daddy’s girls”. I have heard that that can often be the case, females going to men, males to women. I know that Skip has definitely bonded with me but also noticed that he bonded with my oldest daughter very quickly(she is around a lot), but also noticed that he took to my younger daughter just after a couple visits a few weeks apart.  I feel is is absolutely safe to say that he takes to women and men are very intimidating to him and idk if it’s just his personality/preference or if he was mistreated by a man/men? The positive news is that of any man, Skip does interact willingly with my husband. The biggest thing that happened was when he pawed my husbands hand in bed and asked for rubs, but only at a full arm length away. He will run to see him when there is food around(not a great habit) and will take treats from him. He will also “bop” his hand with his nose and be happy jump and wag his tail. And a few times when I am not in the room, when the other two dogs have been laying with my husband in his chair, he has laid with him, but out of reach. Anyway, sorry to ramble, I guess I’m just trying to say that my husband would love and try’s daily to improve their relationship, you can tell Skip wants a closer relationship he will even bark with frustration seeing the girls get affection and he wants it, but is to scared to get close enough. His fears get to him and is harder for him to over come them with my husband, than with me, I feel it’s simply because he is a man. Question, do I just keep doing what we are doing, continue to make contact a very positive and rewarding experience and just let time tell, or is there anything else that can help him learn that men don’t have to be feared, especially his human daddy. Thank you❤️"
    "Hello, I have a 7 month old Golden Retriever. He has a stubborn streak. If he is outside and doesn’t want to move, he lays down. If he doesn’t want to come, he doesn’t. Months ago he obeyed recall commands. I know this is the age they get more independent-or the adolescent phase. I don’t want to mess this up though as this won’t be so cute when he is 85 pounds. What can I do to communicate with him that the stubbornness is not in his best interest?"

]

comments = [
    ['Dogs can have reflux but it’s typically indicative if something more. “Picky” dogs do not puke because they are picky. Your dog likely has a food aversion now and if not adressed will continue to get worse. Get another opinion or see an internal medicine specialist.',
     'Mine throws up if her tummy is really empty.', 'My girl has acid reflux. She takes pepcid every day.', 'Get a vet check at a teaching hospital if you can we live in ca in the Bay Area and take ours to Davis they run a much more thorough exam in my opinion',
     'Have them check her gallbladder.', 'So sorry hope she gets better', 'Try elevating all her food and water ...'],
    ['Chew toys by goughnuts.com They are a little more expensive but they\'re compressed rubber and some (the ones that we\'ve bought) have a lifetime warranty. We have a toy destroyer(destroys firehose toys in under 30 minutes) and it took her 18 months to even make a dent. They would have replaced it but we bought another one because it was well worth the money. She chews on it ALL DAY, EVERYDAY.',
     'I have two pits and they destroy almost everything in a day. This ball has lasted a MONTH and still squeaks https://app.chewy.com/n5403rs9ylb',
     'I have a cane corso. Standard Nylabone supervised chewing. Keeps tartar at bay also. Does a number on their gums when they get too into it but it’s fine. They chew and make super tiny pieces that either get swallowed or just sit on your floor. Passes out the other end with no issue- they are very small pieces.',
     'Jolly balls have been great. I have 4 different sizes and kinds. Some of the horse jolly balls are good too. Several Kong toys have lasted along time. elk antlers have been good natural chews.'
     ],
    ['That\'s a Lab', 'My dogs are trained to go to their “place” while I eat dinner. If place is broken once, I reset. Second time, up goes the ex pen.',
     'I’m working on “place” too.', 'We free feed our pup.', 'I almost always feed mine (with training) after I eat. They never ask'],
    ["Calmness calming collar and scatter feeding, low lights, soft music, lavender scent.",
        'Treats go a long way with training, building trust, and reinforcing positive behavior!', 'My dog, 3 years old, still barks at me when I sneeze.',
        'We also have a very fearful pup. One of the things we do which seems to help is we talk to her and explain things to her, neither minimizing nor feeding her fears. I\'m going to vacuum. I have a towel in my hand. See these pretty dishes? etc. The same works for out of sight noises, particularly when it\'s us. It\'s me, I\'m home from work, I hope you had a better day than me, etc. As for things she\'s afraid of we may fawn a little more over them. And sometimes pet it. I don\'t know if that would work with you friend with a beard or not😊. It appears to help familiarize her with our voices, our comings and goings, our routines, the quirks of our home, etc. She picks up our calm tone which helps her feel less threatened. And helps make her a bit more confident.',
        'She lacks experience. Experience builds reactions.. positive experience= positive reactions. Start exposing her to as many experiences as possible. 1 / foreign objects. Approach her calmly with objects. Observe her fear reactions. Invite her to investigate the object. Put it down and let her, see, sniff and experience it. Reward her with calm praise. Pats. Treats. She will soon come happily to invest new items. 2 / barking at sounds approaching. When she hears someone coming she will sound the alert. Part one: Teach her a command to cease barking. If she stops when she sees you, give the command(quiet, enough or stop). Then reward her obedience. Part 2: call out the command a second or two before she can see you. Reward her obedience. Part 3: call out the command from further away. Reward obedience. (I use the words, “ENOUGH, thank you!) Eventually you will be able to command her from the entry door to the roof, if necessary. 3 / strangers. Experiences must be positive. Introduce her to all kinds of people. Men, women, big, small, young, old. Loud, quiet, beards, glasses, hats, boots, clicking high heels. Helmets, flapping coats Etc keep her under your direct control at all times. Reward her for calm investigation(as in point 1 /) . Have people toss her tiny treats. Confidence will build with experience. She will become more interested in calm investigations, if these investigations result in bits of roast chicken, or other treats. I’m sure others will have some training ideas too. Good luck.'],
    ['I have a TP thief as well. I foudnd the best way to overcome it is management paired with ensuring needs are met (mental exercise, enrichment, mental exercisee).'],
    ['First the dogs need to be set up for success. they can’t just be left to keep practicing the behaviour - it makes to harder to fix and can escalate - as you have seen. if the dog is uncomfortable he needs space from your dog and management. do not punish growls - this is a crucial communication system this file has info on dealing with fights and how to reintroduce dogs',
     'Keep moving forward and always communicate as friends to solve issues 👌'],
    ['My pup lovea then and I don\'t find then messy. The end piece I take away so she doesn\'t swallow but then you can soak it in water and microwave it and turn it into a cheesy puff for the dog to eat. I will say she can get through a yak chew in a day. If you want something to last kongr try reindoor antlers.',
     'My dog loves them! They aren\'t smelly and I haven\'t noticed any film or stuff left from it. I have a shih tzu and it lasts her months!',
     'My pup loves them too. Her yak chew lasts a few days. I have carpet and haven’t seen any residue and there isn’t any yucky smell. When you get to a certain spot with the chew , you can microwave the rest and it becomes a different harder chew for them to enjoy.',
     'My 3 love them. They are all aggressive chewers', 'Have you tried a deer antler? I have a lab/ Pitt mix who chews up the yak chews like they’re nothing (they’re great for a slightly smaller dog) anyhow the antler has been great for him. He loves it and it’s last a good while',
     'Yak chews are great, they don’t smell, but do leave little crumb like things on the floor. If your pup is lactose intolerant at all, make sure it is pure yak milk cheese. Many mix cow’s mill in with the yak milk. Also I would buy a holder for it. A holder helps prevent it from breaking and stopping them from eating the last inch or do in one gulp . This is the holder I bought for my girl’s yak chews. I buy the large Raw Paws chews and put them in there',
     'Mighty Paw! You can order directly from them or on Amazon. I think they are way better quality than the Himalayan brand.', 
     'Someone suggested Trader Joe’s on here recently. They come in a two pack for $4.99. My dogs are enjoying them and they’re no-smell or mess. The holder up above will be helpful. One of our labs can swallow anything, it seems🙄',
     ],
    ["when you take them together start with short training sessions - start in the yard and around the front street. build up from there. just like when you trained them independantly"],
    ["I put lattice on mine on the deck and the gate door.", 
    "First I think of attaching some other light weight / small wire panel that is wider to the lower half of the gates and zip tying on. Also, someone said pool noodles. Idk if they make black pipe foam insulation that size, but it is split down the side and if had enough thickness could “hug” the posts and be cut to go around the hinge side. I think any size fence panel, baby gate or whatever could work but it depends how much you use each gate and how permanent you’d like it. Definitely worth the peace of mind to have a secure space for them though. We have chihuahuas and although I take them to run in the main yard with my full attention, they have a secure chain link run, but the gate gap is tight. Maybe see if they make a bit wider gate that would fit? Good luck! Let us know your solution:)",
     "Pool noodles", 'I know people that use chicken wire, stuff rocks or stack bricks, use wood pieces. Depends how much you use the gate too.',
     'Okay so extreme solution! Sell the Chihuahuas and buy a dog that can\'t fit through the gaps in the fence. Totally kidding, but I thought I\'d look at the problem from a different perspective. Filling the gaps in the fence was already covered.',
     "We zip tied plywood pieces to the gate.", "Jus replace gate with a larger wooden one, or find something to fill those spaces, like screen for doors.",
     "There used to be some sort of flexible fencing at Home Depot that you could attach to those areas.",
     "For a cheap fix we keep our chihuahuas in with chicken wire "
     ],
    ['I don’t have any advice but just wanted to say that I have the same problem with my 2 large, male dogs. They used to like each other when the youngest was a puppy but now they fight every chance they get and must be separated at all times. It really is difficult to say the least…I can imagine how it is for you with 4 of them! I hope that we both find solutions for this problem!!',
     'He been through a lot of pain give him time to forget', 
     "Part 1 of keeping a dog is making sure you have time for it. See, a dog is not like your typical cat or chicken or something. Dogs seek attention and a lack of it can be bad. What I am saying is, don't get so many dogs unless you have reached a stage in your knowledge of handling dogs where you can successfully modify their behavior or eliminate any bad tendencies all by yourself. It always leads to problems like this. I am not doubting your ability to raise a dog or dogs in this case but I think you should have gone for a dog rearing seminar waaaaay before the 1st one. Onto the post, I can only offer a little advice regarding the bullying aspect as well as starting fights. My dog was like this. I used a terrible but effective form of punishment. Water. And a couple of water sprays since he feared those so much. Everytime he started a fight with another dog I sprayed the hell out of him and he'd retreat. Eventually he would think of being sprayed with water Everytime he wanted to fight another dog. Then he would just retreat into a place somewhere in the yard.",
     "I’m by no means an expert but what I’d do in this case is reintroduce them entirely—I’d get someone you trust to help you with this. One dog at a time (after a few decompression days if they’ve recently gotten into a confrontation) I’d take the neo and another one (preferably a calmer one) for a walk, however walk on totally opposite sides of the street (even further apart if you have to) once each dog is calm you can walk side by side closer and closer together, and once they are calm allow them to greet briefly by guiding one (one of the pack) behind the other to sniff. If they become too focused on each other I’d break it and just keep walking, then repeat with the other one. It’s best to introduce one at a time so the whole pack doesn’t gang up on one dog—but also important that you introduce calmly. I’d repeat with each dog and make sure that the other dog isn’t the most interesting thing but rather YOU so you can easily refocus them if need be",
     "I have a Cane Corso and had limit his contact with other dogs while he went through the teenage phase. It was through playing a structured game of tug that he learned to control himself and follow commands while in the overexcited over-stimulated state."],
    ["I am not a trainer but I think you are doing everything right. Look how far this baby had come!",
     "I say keep doing what you’re doing showing love and patience he will eventually come around🥰❣️",
     "Keep doing what you're doing and lots of patience is required."],
    [" I have a tough time too, coming in and going home is wayyyyy more boring. I have found squeaky toys and a game of tug work well fir getting them moving towards home again.",
     "Make it his choice...offer high value treats...cut up hotdogs, bites of cooked liver....",
     "I don't suggest this, but just had to tell.. I had a stubborn Chow/Lab mix that didn't want to come when called. I would have to resort to, \"Goddamn it, Ty...\" Then he would let out a sigh, slowly turn around and come in. It's like when I finally got frustrated enough to swear, he figured, well anything to shut her up!🤣",
     "You got tobe more interesting than the outside. Up your anty and have a high value treat or toy they enjoy",
     "What can you do to make it *worth* coming? Sometimes we end up inadvertently punishing dogs for responding to \"come\" by making all the fun time end."
     "We are trying to train our 6 month old golden to come inside after going potty and usually the only way is to ask if he wants to eat (which he now knows “eat”) or yesterday when he was out in the snow which of course he loves, I had to put a few pieces of kibble in his metal food bowl and swirl it around it get him inside 🤣 so I don’t think these are good tips but I feel your pain 🤣",
     "Drill daily for 10 minutes. Always end on a happy note.",
     "My doodle does the same thing! I bring treats along to bribe him… kind of like a toddler 😂",
     "I’d use a long line when practicing so you can use pressure to guide him to you. Short multiple sessions a day will do it!",
     "Their personalities change a lot over the first 2 years and the second fear period is coming up at 8-9 months. It's pretty normal to think you have a behaviour down at one time/place then see it fall apart at another. You really have to proof things out over a longer time period and with higher levels of distraction. Your just hitting the teenager phase lol",
     "Mine know to do what I want when I say, NOW!",
     "My boxer was stubborn. I made a game out of getting him to chase me. I started indoors with a human play bow and treats. Once I got him into the game indoors, we trained outdoors. Now if he won't listen, I do my little hop (play bow) and he happily chases me wherever I go. My boy is a goof and responds to anything play related so this worked well."
     ],

]

def seed_posts():
    fake = Faker()
    posts = [
        Post(
            user_id=1,
            title='Is this normal?',
            post_body='My dog is always chasing his tail. Is this normal beahvior?',
            posted='11-11-2021',
            group_id=7
        ),
        Post(
            user_id=2,
            title='Dobermans are the best!',
            post_body='I just wanted to say that Dobermans are, by far, the BEST breed!!!',
            posted='11-05-2021',
            group_id=3

        ),
        Post(
            user_id=randrange(1, 12),
            title='Harness Recomendations',
            post_body='Recommendations for a no-pull harness? My Luna girl is approximately 60 lbs and pulls so hard she is wheezing when we go on walks.',
            posted=fake.date_between(start_date='-3y', end_date='today'),
            group_id=randrange(1, 8)

        ),

    ]

    db.session.add_all(posts)

    for i in range(100):
        num = randrange(0,11)
        user = randrange(1, 36)
        id = 4 + i
        post_to_add = Post(
            user_id=user,
            title=titles[num],
            post_body=seeded_posts[num],
            posted=fake.date_between(start_date='-3y', end_date='today'),
            group_id=randrange(1, 8)

        )
        db.session.add(post_to_add)
        print('\n\n\n', id, '\n\n\n')
        for comment in comments[num]:
            comment_to_add = Comment(
                user_id=randrange(1, 12),
                post_id=id,
                comment_body=comment,
                posted=fake.date_between(start_date='-3y', end_date='today')
            )
            db.session.add(comment_to_add)
    for i in range(100):
        num = randrange(0, 11)
        user = randrange(1, 36)
        post_to_add = Post(
            user_id=user,
            title=fake.sentence(),
            post_body=fake.paragraph(nb_sentences=25),
            posted=fake.date_between(start_date='-3y', end_date='today'),
            group_id=randrange(1, 8)

        )
        db.session.add(post_to_add)
        comment_to_add = Comment(
            user_id=randrange(1, 12),
            post_id=randint(1, 203),
            comment_body=fake.paragraph(nb_sentences=10),
            posted=fake.date_between(start_date='-3y', end_date='today')
        )
        db.session.add(comment_to_add)

   
    db.session.commit()


def undo_posts():
    db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
    db.session.commit()
