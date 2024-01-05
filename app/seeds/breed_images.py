from app.models import db, Breed_Image





def seed_breed_images():

    breeds = [
    Breed_Image(
        breed_id=1,
        img_url='https://images.pexels.com/photos/35638/labrador-breed-dogs-animal.jpg?auto=compress&cs=tinysrgb&h=750&w=1260'
    ),
    Breed_Image(
        breed_id=1,
        img_url='https://images.pexels.com/photos/162149/dog-black-labrador-black-dog-162149.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    ),
    Breed_Image(
        breed_id=1,
        img_url='https://images.pexels.com/photos/998251/pexels-photo-998251.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    ),
    Breed_Image(
        breed_id=1,
        img_url='https://images.pexels.com/photos/1790446/pexels-photo-1790446.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    ),
    Breed_Image(
        breed_id=1,
        img_url='https://images.pexels.com/photos/2832119/pexels-photo-2832119.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    ),
    Breed_Image(
        breed_id=1,
        img_url='https://images.pexels.com/photos/1696589/pexels-photo-1696589.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    ),
    Breed_Image(
        breed_id=1,
        img_url='https://images.pexels.com/photos/7210753/pexels-photo-7210753.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    ),
    Breed_Image(
        breed_id=2,
        img_url='https://images.pexels.com/photos/160846/french-bulldog-summer-smile-joy-160846.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    ),
    Breed_Image(
        breed_id=2,
        img_url='https://images.pexels.com/photos/3930940/pexels-photo-3930940.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    ),
    Breed_Image(
        breed_id=2,
        img_url='https://images.pexels.com/photos/4587998/pexels-photo-4587998.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    ),
    Breed_Image(
        breed_id=2,
        img_url='https://images.pexels.com/photos/20470/pexels-photo.jpg?auto=compress&cs=tinysrgb&h=750&w=1260'
    ),
    Breed_Image(
        breed_id=2,
        img_url='https://images.pexels.com/photos/7182594/pexels-photo-7182594.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    ),
    Breed_Image(
        breed_id=2,
        img_url='https://images.pexels.com/photos/3930941/pexels-photo-3930941.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    ),
    Breed_Image(
        breed_id=2,
        img_url='https://images.pexels.com/photos/6420248/pexels-photo-6420248.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    ),
    Breed_Image(
        breed_id=2,
        img_url='https://images.pexels.com/photos/4730048/pexels-photo-4730048.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    ),
    Breed_Image(
        breed_id=3,
        img_url='https://images.pexels.com/photos/333083/pexels-photo-333083.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    ),
    Breed_Image(
        breed_id=3,
        img_url='https://images.pexels.com/photos/1633522/pexels-photo-1633522.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    ),
    Breed_Image(
        breed_id=3,
        img_url='https://images.pexels.com/photos/1800314/pexels-photo-1800314.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    ),
    Breed_Image(
        breed_id=3,
        img_url='https://images.pexels.com/photos/2873382/pexels-photo-2873382.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    ),
    Breed_Image(
        breed_id=3,
        img_url='https://images.pexels.com/photos/2793158/pexels-photo-2793158.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    ),
    Breed_Image(
        breed_id=3,
        img_url='https://images.pexels.com/photos/8811378/pexels-photo-8811378.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    ),
    Breed_Image(
        breed_id=4,
        img_url='https://images.pexels.com/photos/2253275/pexels-photo-2253275.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    ),
    Breed_Image(
        breed_id=4,
        img_url='https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    ),
    Breed_Image(
        breed_id=4,
        img_url='https://images.pexels.com/photos/686094/pexels-photo-686094.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    ),
    Breed_Image(
        breed_id=4,
        img_url='https://images.pexels.com/photos/1959055/pexels-photo-1959055.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    ),
    Breed_Image(
        breed_id=4,
        img_url='https://images.pexels.com/photos/2318990/pexels-photo-2318990.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    ),
    Breed_Image(
        breed_id=4,
        img_url='https://images.pexels.com/photos/2791658/pexels-photo-2791658.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    ),
    Breed_Image(
        breed_id=5,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Bulldog-standing-in-the-grass.jpg'
    ),
    Breed_Image(
        breed_id=5,
        img_url='https://www.veterinarypracticenews.com/wp-content/uploads/2021/02/SA_Bulldogs.jpg'
    ),
    Breed_Image(
        breed_id=5,
        img_url='https://www.brproud.com/wp-content/uploads/sites/80/2021/02/GettyImages-93392638-e1613098268255.jpg?strip=1'
    ),
    Breed_Image(
        breed_id=5,
        img_url='https://cdn.pixabay.com/photo/2020/07/20/06/42/english-bulldog-5422018_1280.jpg'
    ),
    Breed_Image(
        breed_id=5,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/bulldog-on-skateboard-grinning.jpg'
    ),
    Breed_Image(
        breed_id=6,
        img_url='https://multifiles.pressherald.com/uploads/sites/10/2020/02/APTOPIX_Westminster_Dog_Show_63587.jpg'
    ),
    Breed_Image(
        breed_id=6,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Poodle-Standard-Gray-On-White-Standing.jpg'
    ),
    Breed_Image(
        breed_id=6,
        img_url='https://i.pinimg.com/736x/79/56/2a/79562af7c3e7f3363d14d0b157697278.jpg'
    ),
    Breed_Image(
        breed_id=6,
        img_url='https://www.purina.com.au/-/media/project/purina/main/breeds/dog/dog_poodle-standard_desktop.jpg?h=475&la=en&w=825&hash=6439CC36AD93D0366FA04E354F108825'
    ),
    Breed_Image(
        breed_id=6,
        img_url='https://www.floridapoodlerescue.org/wp-content/uploads/2020/07/fb-image2.jpg'
    ),
    Breed_Image(
        breed_id=6,
        img_url='https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/portrait-of-standard-poodle-dogs-panoramic-images.jpg'
    ),
    Breed_Image(
        breed_id=7,
        img_url='https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2016/06/24151048/Beagle-standing-in-a-frosty-field-on-a-cold-morning.jpg'
    ),
    Breed_Image(
        breed_id=7,
        img_url='https://www.cesarsway.com/wp-content/uploads/2019/09/AdobeStock_219003378-1024x683.jpeg'
    ),
    Breed_Image(
        breed_id=7,
        img_url='https://www.thesprucepets.com/thmb/WxVsARRPU_8Wx8iS3iqDxP3_iK4=/3881x2911/smart/filters:no_upscale()/beagle-RolfKopfle-Photolibrary-Getty-135631212-56a26b1d3df78cf772756667.jpg'
    ),
    Breed_Image(
        breed_id=7,
        img_url='https://assets.orvis.com/is/image/orvisprd/AdobeStock_25245434?wid=1023&src=is($object$:7-3)'
    ),
    Breed_Image(
        breed_id=8,
        img_url='https://upload.wikimedia.org/wikipedia/commons/2/26/Rottweiler_standing_facing_left.jpg'
    ),
    Breed_Image(
        breed_id=8,
        img_url='https://vetstreet.brightspotcdn.com/dims4/default/419926a/2147483647/crop/0x0%2B0%2B0/resize/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2Fbf%2F33d570a7fb11e0a0d50050568d634f%2Ffile%2FRottweiler-3-645mk062811.jpg'
    ),
    Breed_Image(
        breed_id=8,
        img_url='https://rottweilerhealth.org/wp-content/uploads/2021/01/Rottweiler-Health-Foundation-header-image-1-1500x630.jpg'
    ),
    Breed_Image(
        breed_id=8,
        img_url='https://assets.orvis.com/is/image/orvisprd/rottweiler?wid=1023&src=is($object$:7-3)'
    ),
    Breed_Image(
        breed_id=8,
        img_url='https://media-be.chewy.com/wp-content/uploads/2021/06/02111021/Rottweiler_Feature-Image.jpg'
    ),
    Breed_Image(
        breed_id=9,
        img_url='https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F08%2F16%2Fgerman-shorthaired-pointer-bird-in-mouth-613909636-2000.jpg'
    ),
    Breed_Image(
        breed_id=9,
        img_url='http://4.bp.blogspot.com/-HNNXBORFawQ/Tfgc9Q6ue5I/AAAAAAAAA3w/s1UIpnyimKg/s1600/GSPFinals-62.jpg'
    ),
    Breed_Image(
        breed_id=9,
        img_url='https://petpricelist.com/wp-content/uploads/2018/01/german-shorthaired-pointer.jpg'
    ),
    Breed_Image(
        breed_id=9,
        img_url='https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2019/01/09152204/345997288471648112_-_IMG_3984-1024x576.jpg'
    ),
    Breed_Image(
        breed_id=9,
        img_url='https://1.bp.blogspot.com/-MfqdbDwM8Tc/XPYpxWeI6fI/AAAAAAAAB-o/V9WWqveX6-Q-KqgxFDmws2TUAMj1yVYBwCLcBGAs/s1600/GermanShorthaired.jpg'
    ),
    Breed_Image(
        breed_id=9,
        img_url='https://www.thesprucepets.com/thmb/nxHrhvEXVRDhTnD9kzQaua93h9o=/1412x1412/smart/filters:no_upscale()/GermanShorthairedPointerProfile-9c0431e942dc44f1b26aa839d9032eee.jpg'
    ),
    Breed_Image(
        breed_id=10,
        img_url='https://formydachshund.com/wp-content/uploads/2019/12/Depositphotos_320885450_ots_photo_web-800x600.jpg'
    ),
    Breed_Image(
        breed_id=10,
        img_url='https://i.redd.it/0ke87zxgyux31.jpg'
    ),
    Breed_Image(
        breed_id=10,
        img_url='https://thehappypuppysite.com/wp-content/uploads/2018/09/dachshund-puppies2.jpg'
    ),
    Breed_Image(
        breed_id=10,
        img_url='https://www.petfirst.com/wp-content/uploads/2018/03/Breed-Hero-Dachshund-1200x1200.jpg'
    ),
    Breed_Image(
        breed_id=10,
        img_url='https://ilovedachshunds.b-cdn.net/wp-content/uploads/2019/03/dachshund-health-problems.jpg'
    ),
    Breed_Image(
        breed_id=10,
        img_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/curious-dachshund-outdoors-royalty-free-image-1631002404.jpg?crop=1.00xw:0.668xh;0,0.200xh&resize=640:*'
    ),
    Breed_Image(
        breed_id=10,
        img_url='https://cdn.shopify.com/s/files/1/0108/6819/5428/files/How_social_are_Dachshunds_5.jpg?v=1580859512'
    ),
    Breed_Image(
        breed_id=11,
        img_url='https://www.akc.org/wp-content/uploads/2015/11/Cane-Corso-standing-in-the-park.jpg'
    ),
    Breed_Image(
        breed_id=11,
        img_url='https://moderndogmagazine.com/sites/default/files/styles/slidehsow-banner/public/images/breeds/top_images/CaneCorso-Header.jpg?itok=R1dRXozR'
    ),
    Breed_Image(
            breed_id=11,
        img_url='https://www.petage.com/wp-content/uploads/2017/06/Cane-Corso-1-670x447.jpg'
        ),
    Breed_Image(
        breed_id=11,
        img_url='https://www.trendingbreeds.com/wp-content/uploads/2020/02/Alert-Cane-Corso.jpg'
    ),
    Breed_Image(
            breed_id=11,
        img_url='https://petkeen.com/wp-content/uploads/2021/06/Cane-Corso-laying-in-the-park_Stivog_Shutterstock.jpg'
        ),

    Breed_Image(
        breed_id=12,
        img_url='https://www.dogmal.com/wp-content/uploads/2018/07/American-Staffordshire-Terriers.jpg'
    ),

    Breed_Image(
        breed_id=12,
        img_url='https://i.pinimg.com/originals/22/a3/39/22a339226c83494298a28aef79378bdd.jpg'
    ),
    Breed_Image(
        breed_id=12,
        img_url='https://www.kopekler.com/assets/media/b1618-11.jpg'
    ),
    Breed_Image(
        breed_id=12,
        img_url='https://i.pinimg.com/236x/65/fb/82/65fb82e8e4edd4c3273544de3ee565e8--dog-breeds-american-staffordshire-terriers.jpg'
    ),
    Breed_Image(
        breed_id=12,
        img_url='https://i.pinimg.com/736x/a3/7a/87/a37a8754ab05079eb4b9feebb31b0016.jpg'
    ),
    Breed_Image(
        breed_id=12,
        img_url='https://i.pinimg.com/originals/9a/58/69/9a586990564a2e17cad4e1c0deb243bd.jpg'
    ),
    Breed_Image(
        breed_id=12,
        img_url='https://jelenadogshows.com/eng/wp-content/uploads/2019/11/286-674x500.jpg'
    ),
    Breed_Image(
        breed_id=13,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Boxer.1.jpg'
    ),
    Breed_Image(
        breed_id=13,
        img_url='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Male_fawn_Boxer_undocked.jpg/1200px-Male_fawn_Boxer_undocked.jpg'
    ),
    Breed_Image(
        breed_id=13,
        img_url='https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/09/06202234/Boxer-laying-on-the-floor-indoors.jpg'
    ),
    Breed_Image(
        breed_id=13,
        img_url='https://www.huntercreekboxers.com/s/cc_images/teaserbox_4104747998.jpg?t=1570900365'
    ),
    Breed_Image(
        breed_id=13,
        img_url='https://i.pinimg.com/236x/e2/8d/f2/e28df2dcb25e60dd3b1f9d777aa096bd.jpg'
    ),
    Breed_Image(
        breed_id=13,
        img_url='https://www.zooplus.co.uk/magazine/wp-content/uploads/2018/07/deutscher-boxer-tabby-2-768x523.jpg'
    ),
    Breed_Image(
        breed_id=13,
        img_url='https://cdn.pixabay.com/photo/2016/04/11/01/17/good-aiderbichl-1321216_960_720.jpg'
    ),
    Breed_Image(
        breed_id=14,
        img_url='http://cdn.akc.org/content/article-body-image/SimonLouieVinnie.jpg'
    ),
    Breed_Image(
        breed_id=14,
        img_url='http://cdn.akc.org/PugPuppies.jpg'
    ),
    Breed_Image(
        breed_id=14,
        img_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7-RTwNHxoTKPZ1tgbUVp8yQC2KW8Jd6OhqA&usqp=CAU'
    ),
    Breed_Image(
        breed_id=14,
        img_url='http://cdn.akc.org/PugSleeping.jpg'
    ),
    Breed_Image(
        breed_id=14,
        img_url='https://a-z-animals.com/media/Pug-Canis-familiaris-face.jpg'
    ),
    Breed_Image(
        breed_id=14,
        img_url='https://images.newscientist.com/wp-content/uploads/2020/10/13230802/pug-ex5kgg_web.jpg'
    ),
    Breed_Image(
        breed_id=14,
        img_url='https://www.purina.com.au/-/media/project/purina/main/breeds/dog/mobile/dog_pugs_mobile.jpg?h=300&la=en&w=375&hash=5BF9CFC4E6FC7347E6FDA383E42D8A52'
    ),
    Breed_Image(
        breed_id=15,
        img_url='https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/06154034/Akita-standing-outdoors-in-the-summer.jpg'
    ),
        Breed_Image(
        breed_id=15,
        img_url='https://cdn.pixabay.com/photo/2021/01/30/15/14/akita-5964180__480.jpg'
    ),
        Breed_Image(
        breed_id=15,
        img_url='https://i.pinimg.com/originals/03/df/ae/03dfae2c5037d44ce8a34b3f81d62f62.jpg'
    ),
        Breed_Image(
        breed_id=15,
        img_url='https://i.pinimg.com/originals/f7/a3/54/f7a354d1b505ffec228c9c34319b252d.jpg'
    ),
        Breed_Image(
        breed_id=15,
        img_url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8b706595-f0cd-42f2-9778-da1b590a294b/deotrui-a92c3bd7-e2a3-439d-bda2-f7acb9e4f0e3.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzhiNzA2NTk1LWYwY2QtNDJmMi05Nzc4LWRhMWI1OTBhMjk0YlwvZGVvdHJ1aS1hOTJjM2JkNy1lMmEzLTQzOWQtYmRhMi1mN2FjYjllNGYwZTMuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.6EXqjqwgApUR9ivLkVGOevPeaHccwbfK0lTSg5P-JN8'
    ),
        Breed_Image(
        breed_id=15,
        img_url='https://image.jimcdn.com/app/cms/image/transf/none/path/s53b36d06bb1bc5e5/image/iea74cdb9a08eab13/version/1620740965/image.jpg'
    ),
        Breed_Image(
        breed_id=15,
        img_url='https://www.dog-breeds-expert.com/images/AmericanAkita10.jpg'
    ),
        Breed_Image(
        breed_id=16,
        img_url='https://d17fnq9dkz9hgj.cloudfront.net/breed-uploads/2018/08/siberian-husky-card-small.jpg?bust=1535567860'
    ),
        Breed_Image(
        breed_id=16,
        img_url='https://patterjack.com/wp-content/uploads/2021/11/Siberian-Husky-head-portrait-outdoors.jpg'
    ),
        Breed_Image(
        breed_id=16,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Siberian-Husky-standing-outdoors-in-the-winter.jpg'
    ),
        Breed_Image(
        breed_id=16,
        img_url='https://i.pinimg.com/originals/e5/8d/43/e58d43e8bbfe3713b5e039a084ec9663.jpg'
    ),
        Breed_Image(
        breed_id=16,
        img_url='http://i.imgur.com/0FxPrzv.jpg'
    ),
        Breed_Image(
        breed_id=17,
        img_url='https://media.kidadl.com/607a5d6ba78690a68373593b_american_bully_facts_are_ideal_for_bulldog_lovers_2e2c894ab3.jpg'
    ),
        Breed_Image(
        breed_id=17,
        img_url='https://i.pinimg.com/736x/71/79/34/71793492aa5340305ba917a4aee1ae1b.jpg'
    ),
        Breed_Image(
        breed_id=17,
        img_url='https://www.bubblypet.com/wp-content/uploads/2020/11/Big-American-Bully-XL.jpg'
    ),
        Breed_Image(
        breed_id=17,
        img_url='https://i.pinimg.com/originals/c7/57/1e/c7571e5e2d08db5f781fc27cd0afe1e6.jpg'
    ),
        Breed_Image(
        breed_id=18,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Pembroke-Welsh-Corgi-standing-outdoors-in-the-fall.jpg'
    ),
        Breed_Image(
        breed_id=18,
        img_url='https://www.purina.com.au/-/media/project/purina/main/breeds/puppies/puppy-chihuahua/puppy-corgi.jpg'
    ),
        Breed_Image(
        breed_id=18,
        img_url='https://dogtime.com/assets/uploads/gallery/pembroke-welsh-corgi-dog-breed-pictures/prance-8.jpg'
    ),
        Breed_Image(
        breed_id=18,
        img_url='https://hellobark.com/wp-content/uploads/corgi-1200.jpg'
    ),
        Breed_Image(
        breed_id=18,
        img_url='https://tevrapet.com/wp-content/uploads/2020/12/AdobeStock_219316170-scaled.jpeg'
    ),
        Breed_Image(
        breed_id=18,
        img_url='https://www.thesprucepets.com/thmb/48TXFBlasHhZqSM-3Yq3h-ZCn_Q=/1333x1000/smart/filters:no_upscale()/breed-profile-pembroke-welsh-corgi-1117986-hero-a9d0f486d2c64c5fa09ed8e4044eb0a9.jpeg'
    ),
        Breed_Image(
        breed_id=19,
        img_url='https://www.thesprucepets.com/thmb/KH5GXBgckmJrNs2QsjNiXD9UC8U=/3084x3084/smart/filters:no_upscale()/GettyImages-1193899346-55c8ffea082e49f1b1f5bc7c58415785.jpg'
    ),
        Breed_Image(
        breed_id=19,
        img_url='http://justfunfacts.com/wp-content/uploads/2021/02/cocker-spaniel.jpg'
    ),
        Breed_Image(
        breed_id=19,
        img_url='https://i.pinimg.com/originals/29/67/98/2967982abd2f2ce2a487e99e8846cbf1.jpg'
    ),
    Breed_Image(
        breed_id=19,
        img_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeCxL4mtfGDSpVM7UN31W4SLrglGYabUuzSbwMji-dG5Lr4ELc2rNPLHRnVN5a8ME4tcs&usqp=CAU'
    ),
        Breed_Image(
        breed_id=19,
        img_url='https://perfectcockerspaniel.files.wordpress.com/2019/08/fred-chocolate-tan-cocker-spaniel-perfect-cocker-spaniel-blog-book-copy.jpg?w=1200'
    ),
        Breed_Image(
        breed_id=20,
        img_url='https://media-be.chewy.com/wp-content/uploads/2021/06/02113056/Bullmastiff-FeaturedImage.jpg'
    ),
        Breed_Image(
        breed_id=20,
        img_url='https://media.istockphoto.com/photos/bullmastiff-posing-picture-id619520136?k=20&m=619520136&s=612x612&w=0&h=3Qzmbjl-RSQAdoIq5iF_Fil6R1fO0_Q015WVrKtsOmg='
    ),
        Breed_Image(
        breed_id=20,
        img_url='https://images-ra.adoptapet.com/seo/1/ff/30_ff.jpg'
    ),
    Breed_Image(
        breed_id=20,
        img_url='https://fuzzy-rescue.com/wp-content/uploads/2020/11/Bullmastiff-1a.jpg'
    ),
        Breed_Image(
        breed_id=20,
        img_url='https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F02%2F23%2Fbullmastiff-running-tongue-249331584-2000.jpeg'
    ),

        Breed_Image(
        breed_id=21,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Australian-Shepherd.1.jpg'
    ),

        Breed_Image(
        breed_id=21,
        img_url='https://besthqwallpapers.com/Uploads/12-4-2018/48079/thumb2-aussie-meadow-blur-australian-shepherd-pets.jpg'
    ),

        Breed_Image(
        breed_id=21,
        img_url='https://images4.alphacoders.com/101/1012745.jpg'
    ),

        Breed_Image(
        breed_id=21,
        img_url='https://wallup.net/wp-content/uploads/2018/09/25/571172-Australian_Shepherd-forest-Papillon-dog-748x468.jpg'
    ),

        Breed_Image(
        breed_id=21,
        img_url='https://c4.wallpaperflare.com/wallpaper/94/43/766/autumn-leaves-pose-background-paw-hd-wallpaper-preview.jpg'
    ),

        Breed_Image(
        breed_id=21,
        img_url='https://besthqwallpapers.com/Uploads/4-10-2018/67832/thumb2-australian-shepherd-little-puppy-autumn-forest-pets.jpg'
    ),

    Breed_Image(
        breed_id=21,
        img_url='https://motaen.com/upload/wallpapers/2020/06/08/14/52/67329/nature-running-dog-wildflowers-preview.jpg'
    ),

        Breed_Image(
        breed_id=22,
        img_url='https://highlandcanine.com/wp-content/uploads/2021/05/yorkshire-terrier-sitting-on-decking.jpg'
    ),

        Breed_Image(
        breed_id=22,
        img_url='https://www.thesprucepets.com/thmb/wUATuqZfVXedDqKnYorz3vwadQ8=/1414x1414/smart/filters:no_upscale()/GettyImages-652401198-53c4d9adf78c4d5a9cb1eec9d8ecb1a5.jpg'
    ),

        Breed_Image(
        breed_id=22,
        img_url='https://media-be.chewy.com/wp-content/uploads/2021/07/16074327/YorkshireTerrier-FeaturedImage.jpg'
    ),

        Breed_Image(
        breed_id=22,
        img_url='https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F08%2F10%2Fyorkshire-terrier-red-bow-walking-1291798649-2000.jpg'
    ),

    Breed_Image(
        breed_id=22,
        img_url='https://assets.orvis.com/is/image/orvisprd/AdobeStock_180022533?wid=1023&src=is($object$:7-3)'
    ),

        Breed_Image(
        breed_id=22,
        img_url='https://cdn1.playbarkrun.com/wp-content/uploads/2018/05/28100010/yorkshire-terrier-coat-grooming-brushing.jpg'
    ),

        Breed_Image(
        breed_id=23,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Great-Dane-looking-back-over-his-shoulder-outdoors-at-the-park.jpg'
    ),

        Breed_Image(
        breed_id=23,
        img_url='https://cdn.mos.cms.futurecdn.net/2vdJPwVUSsqtZJLdxJ4i36.jpg'
    ),

    Breed_Image(
        breed_id=23,
        img_url='https://www.purinaproclub.com/sites/g/files/auxxlc346/files/styles/large/public/GrtDane_list.jpg?itok=OTuKazwD'
    ),

    Breed_Image(
        breed_id=23,
        img_url='https://vetstreet.brightspotcdn.com/dims4/default/531e3f0/2147483647/crop/0x0%2B0%2B0/resize/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F46%2F2d1f90a0d711e0a2380050568d634f%2Ffile%2FGreat-Danes-3-645mk062111.jpg'
    ),

        Breed_Image(
        breed_id=23,
        img_url='https://i.pinimg.com/originals/be/7e/4f/be7e4fd51e34ffb15157d8ac859a0990.jpg'
    ),
        Breed_Image(
        breed_id=23,
        img_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/great-dane-dog-portrait-royalty-free-image-1594629594.jpg?crop=1.00xw:0.752xh;0,0.151xh&resize=1200:*'
    ),

        Breed_Image(
        breed_id=23,
        img_url='https://animals.net/wp-content/uploads/2018/08/Great-Dane-3.jpg'
    ),

        Breed_Image(
        breed_id=24,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Cavalier-King-Charles-Spaniel-standing-in-the-grass.jpg'
    ),

        Breed_Image(
        breed_id=24,
        img_url='https://media-be.chewy.com/wp-content/uploads/2021/06/02112758/Cavalier-King-Charles-Spaniel-FeaturedImage.jpg'
    ),

        Breed_Image(
        breed_id=24,
        img_url='https://vetstreet.brightspotcdn.com/dims4/default/31d2721/2147483647/thumbnail/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F6a%2F38%2F713599734f789b790f6cb060ac74%2FCavalier-King-Charles-Spaniel-AP-KHUGZ3-645sm11514.jpg'
    ),

        Breed_Image(
        breed_id=24,
        img_url='https://www.k9web.com/wp-content/uploads/2019/02/cavalier-king-charles-spaniel-relaxing-outdoor-in-autumn-season.jpg'
    ),
        Breed_Image(
        breed_id=24,
        img_url='https://d17fnq9dkz9hgj.cloudfront.net/breed-uploads/2018/08/cavalier-king-charles-spaniel-detail.jpg?bust=1535565465&width=355'
    ),

        Breed_Image(
        breed_id=24,
        img_url='https://biologydictionary.net/wp-content/uploads/2020/09/shutterstock_1697345674-1.jpg'
    ),

        Breed_Image(
        breed_id=25,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Doberman-Pinscher-standing-outdoors.jpg'
    ),

    Breed_Image(
        breed_id=25,
        img_url='https://c4.wallpaperflare.com/wallpaper/330/679/681/doberman-dog-face-tongue-wallpaper-preview.jpg'
    ),

    Breed_Image(
        breed_id=25,
        img_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSR9m_ah6RPKoeUIR6L9GVeZYY-bkEsaIcG3zV3Pew0LF_NjvGT2wsMYrhbkmtBj-zrVWc&usqp=CAU'
    ),

        Breed_Image(
        breed_id=25,
        img_url='https://www.petfirst.com/wp-content/uploads/2018/03/Breed-Hero-Doberman.jpg'
    ),
        Breed_Image(
        breed_id=25,
        img_url='https://d.newsweek.com/en/full/1844491/doberman-sat-grass.jpg?w=1600&h=1600&q=88&f=a3db3191c42298f89836cf05466b2de6'
    ),

        Breed_Image(
        breed_id=25,
        img_url='https://cdn-bcjdl.nitrocdn.com/gnkKBTQljcQxQnaeTeakBaOogLcXVjMx/assets/static/optimized/wp-content/uploads/2015/10/doberman-768x432.jpg'
    ),

        Breed_Image(
        breed_id=25,
        img_url='https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F03%2F25%2Fdoberman-pinscher-running-grass-1082940764-2000.jpg'
    ),

    Breed_Image(
        breed_id=26,
        img_url='https://d17fnq9dkz9hgj.cloudfront.net/breed-uploads/2018/08/miniature-schnauzer-detail.jpg?bust=1535566660&width=355'
    ),

    Breed_Image(
        breed_id=26,
        img_url='https://images.ctfassets.net/440y9b545yd9/2T9MD2d7gNk5aqBD1alzc8/4810719048d0e773ddc2bdb66e837128/Miniature_Schnauzer_5_Things_850.jpg'
    ),

        Breed_Image(
        breed_id=26,
        img_url='https://cf.ltkcdn.net/dogs/images/orig/259106-1600x1030-standard-schnauzer-temperament.jpg'
    ),
        Breed_Image(
        breed_id=26,
        img_url='https://upload.wikimedia.org/wikipedia/commons/3/36/%D0%9F%D0%B8%D1%82%D0%BE%D0%BC%D0%BD%D0%B8%D0%BA_%22%D0%90%D1%81%D1%81%D0%BE%D0%BD_%D0%90%D1%80%D0%B8%22_%D0%A6%D0%B2%D0%B5%D1%80%D0%B3%D1%88%D0%BD%D0%B0%D1%83%D1%86%D0%B5%D1%80%D1%8B_%D0%B1%D0%B5%D0%BB%D1%8B%D0%B5_%D0%B8_%D1%87%D0%B5%D1%80%D0%BD%D1%8B%D0%B5_%D1%81_%D1%81%D0%B5%D1%80%D0%B5%D0%B1%D1%80%D0%BE%D0%BC_12.jpg'
    ),

        Breed_Image(
        breed_id=26,
        img_url='https://m9b5y6z6.rocketcdn.me/wp-content/uploads/2019/07/Miniature_Schnauzer_standing-scaled.jpeg'
    ),

        Breed_Image(
        breed_id=27,
        img_url='https://www.petmd.com/sites/default/files/2020-11/picture-of-shih-tzu-dog.jpg'
    ),

    Breed_Image(
        breed_id=27,
        img_url='https://s36700.pcdn.co/wp-content/uploads/2017/04/iStock-shihtzu_thumb-600x400.jpg.optimal.jpg'
    ),

    Breed_Image(
        breed_id=27,
        img_url='https://www.scotsman.com/webimg/b25lY21zOmU5ZDY3Mjc5LWRkMTItNDA1Zi04MzljLTM2MTE5ZTU2N2ZkNzo5OTM1OGZlZC1jYmQ3LTQ2N2ItOWJlMi03ZjY3NDBmNmVhMWE=.jpg?width=2048&enable=upscale'
    ),

        Breed_Image(
        breed_id=28,
        img_url='https://vetstreet.brightspotcdn.com/dims4/default/871fdd9/2147483647/crop/0x0%2B0%2B0/resize/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F30%2Fee8ec09e8e11e0a2380050568d634f%2Ffile%2Fboston-terrier-1-062411.jpg'
    ),
        Breed_Image(
        breed_id=28,
        img_url='https://thehappypuppysite.com/wp-content/uploads/2019/01/Boston-Terrier-Temperament-long.jpg'
    ),

        Breed_Image(
        breed_id=28,
        img_url='https://thehappypuppysite.com/wp-content/uploads/2018/08/boston-terrier-long.jpg'
    ),

        Breed_Image(
        breed_id=28,
        img_url='https://img.particlenews.com/img/id/2Q7G40_0cfD0NBP00?type=thumbnail_1600x1200'
    ),

    Breed_Image(
        breed_id=28,
        img_url='https://media-be.chewy.com/wp-content/uploads/2021/07/06093435/Boston-Terrier_FeaturedImage.jpg'
    ),

    Breed_Image(
        breed_id=28,
        img_url='https://maggielovesorbit.com/wp-content/uploads/2020/02/Canada-Pooch-2.jpg'
    ),

        Breed_Image(
        breed_id=29,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Bernese-Mountain-Dog-On-White-01.jpg'
    ),
        Breed_Image(
        breed_id=29,
        img_url='https://s36700.pcdn.co/wp-content/uploads/2018/04/Bernese-Mountain-Dog-running-600x400.jpg.optimal.jpg'
    ),

        Breed_Image(
        breed_id=29,
        img_url='https://www.akc.org/wp-content/uploads/2020/11/Bernese-Mountain-Dog-head-portrait-outdoors.jpg'
    ),

        Breed_Image(
        breed_id=29,
        img_url='https://www.wideopenpets.com/wp-content/uploads/2021/10/living-with-Bernese-mountain-dogs.png'
    ),

    Breed_Image(
        breed_id=29,
        img_url='https://www.wideopenpets.com/wp-content/uploads/2019/11/Bernese-Mountain-Dog.png'
    ),

    Breed_Image(
        breed_id=29,
        img_url='https://cf.ltkcdn.net/dogs/images/orig/268758-1600x1030-bernese-mountain-dog-complete-breed-care-guide.jpg'
    ),

        Breed_Image(
        breed_id=29,
        img_url='https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F05%2F27%2Fbernese-mountain-dog-closeup-puppy-429989103-2000.jpg'
    ),
        Breed_Image(
        breed_id=30,
        img_url='https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F03%2F12%2Fpomeranian-beach-1190837479-2000.jpg'
    ),
        Breed_Image(
        breed_id=30,
        img_url='https://i1.wp.com/alaskadogworks.com/wp-content/uploads/2020/02/pomeranian461cb6a24c9f653bbdf5ff0000035de2.jpg?fit=460%2C246&ssl=1'
    ),
        Breed_Image(
        breed_id=30,
        img_url='https://media-be.chewy.com/wp-content/uploads/2021/06/02102132/Pomeranian_Featured-Image.jpg'
    ),
        Breed_Image(
        breed_id=30,
        img_url='https://highlandcanine.com/wp-content/uploads/2021/03/pomeranian-running-and-happy.jpg'
    ),
        Breed_Image(
        breed_id=30,
        img_url='https://i.dailymail.co.uk/i/pix/2013/12/07/video-undefined-19EFC1D600000578-516_636x358.jpg'
    ),
        Breed_Image(
        breed_id=31,
        img_url='https://upload.wikimedia.org/wikipedia/commons/e/ed/A_Havanese_judging.jpg'
    ),
        Breed_Image(
        breed_id=31,
        img_url='https://media-be.chewy.com/wp-content/uploads/2021/06/02143631/Havanese-FeaturedImage.jpg'
    ),
        Breed_Image(
        breed_id=31,
        img_url='https://i.pinimg.com/originals/76/74/87/7674870f6d207bf7f3e1030c8112c237.jpg'
    ),
        Breed_Image(
        breed_id=31,
        img_url='https://www.thesprucepets.com/thmb/6qDIditb6Uw9Im4A_90Opvdxzr0=/2592x2592/smart/filters:no_upscale()/havanese-HansSurfer-Moment-GettyImages-462845543-58a4777a3df78c47586a596f.jpg'
    ),
        Breed_Image(
        breed_id=31,
        img_url='https://images.ctfassets.net/440y9b545yd9/6XCxx2l7veIe9DL6CfgEoU/0f9451b3c92c543c64b83c8ff1f41313/Havanese850.jpg'
    ),
        Breed_Image(
        breed_id=32,
        img_url='https://dogtime.com/assets/uploads/gallery/english-spaniel-dog-breed-pictures/3-water.jpg'
    ),
        Breed_Image(
        breed_id=32,
        img_url='https://keyassets.timeincuk.net/inspirewp/live/wp-content/uploads/sites/6/2020/06/Springer-spaniels_393004211_696634241.jpg'
    ),
        Breed_Image(
        breed_id=32,
        img_url='https://i.pinimg.com/originals/c9/b5/73/c9b5731030007d0dad9978ac998c9bb0.jpg'
    ),
        Breed_Image(
        breed_id=32,
        img_url='https://vetstreet.brightspotcdn.com/dims4/default/89f653e/2147483647/crop/0x0%2B0%2B0/resize/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F78%2F20e770a0d711e0a2380050568d634f%2Ffile%2FEnglish-Springer-Spaniel-2-645mk062311-.jpg'
    ),
        Breed_Image(
        breed_id=32,
        img_url='https://www.purina.com.au/-/media/project/purina/main/breeds/dog/mobile/dog_english-springer-spaniel_mobile.jpg?h=300&la=en&w=375&hash=F5617F7E548E64866E8E2D8D4D3BF3C8'
    ),
        Breed_Image(
        breed_id=33,
        img_url='https://s36700.pcdn.co/wp-content/uploads/2019/11/Sheltie_8463-170411-CharlotteReeves-e1600083550271-600x665.png'
    ),
        Breed_Image(
        breed_id=33,
        img_url='https://vetstreet-brightspot.s3.amazonaws.com/76/76fd40a80411e0a0d50050568d634f/file/Shetland-Sheepdog-3-645mk062811.jpg'
    ),
        Breed_Image(
        breed_id=33,
        img_url='https://vetstreet.brightspotcdn.com/dims4/default/4e20015/2147483647/thumbnail/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F04%2F37%2F505c751547a39f7164930317b2a4%2Fshetland-sheepdog-ap-uzbjbg-645-x-380.jpg'
    ),
        Breed_Image(
        breed_id=33,
        img_url='https://i.pinimg.com/originals/16/18/f3/1618f378c4ebecd6ef65e3b2ed52a575.jpg'
    ),
        Breed_Image(
        breed_id=33,
        img_url='https://vetstreet.brightspotcdn.com/dims4/default/39177d1/2147483647/crop/0x0%2B0%2B0/resize/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F94%2F3965c0a80411e0a0d50050568d634f%2Ffile%2FShetland-Sheepdog-5-645mk062811.jpg'
    ),
        Breed_Image(
        breed_id=33,
        img_url='https://cdn.shopify.com/s/files/1/0994/0236/articles/shetland-sheepdog_1200x.jpg?v=1502396148'
    ),
        Breed_Image(
        breed_id=34,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Brittany-1.jpg'
    ),
        Breed_Image(
        breed_id=34,
        img_url='https://m8r6w9i6.rocketcdn.me/wp-content/uploads/2020/09/Brittany-Dog-Breed.jpeg'
    ),
        Breed_Image(
        breed_id=34,
        img_url='https://d17fnq9dkz9hgj.cloudfront.net/breed-uploads/2018/08/brittany-spaniel-card-small.jpg?bust=1535567402'
    ),
        Breed_Image(
        breed_id=34,
        img_url='https://s3.amazonaws.com/images.gearjunkie.com/uploads/2021/03/bs-2400x1600.jpg'
    ),
        Breed_Image(
        breed_id=34,
        img_url='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/American_Brittany_standing.jpg/1024px-American_Brittany_standing.jpg'
    ),
        Breed_Image(
        breed_id=34,
        img_url='https://www.pheasantsforever.org/getattachment/8d46f083-bc5f-456f-8ca5-266256238803/American-Brittany-On-Point.jpg.aspx'
    ),
        Breed_Image(
        breed_id=35,
        img_url='https://kennelclubofbeverlyhills.org/wp-content/uploads/2019/12/Miniature-American-Shepherd4.jpg'
    ),
        Breed_Image(
        breed_id=35,
        img_url='https://i.pinimg.com/originals/ab/2c/e2/ab2ce22068e711163df581c4d0aadf52.jpg'
    ),
        Breed_Image(
        breed_id=35,
        img_url='https://upload.wikimedia.org/wikipedia/commons/d/d3/Miniature_American_Shepherd_red_merle.jpg'
    ),
        Breed_Image(
        breed_id=35,
        img_url='https://m8r6w9i6.rocketcdn.me/wp-content/uploads/2020/08/Miniature-American-Shepherd-Dog-Breed.jpeg'
    ),
        Breed_Image(
        breed_id=35,
        img_url='https://dogisworld.com/wp-content/uploads/2019/09/Miniature-American-Shepherd.jpg'
    ),
        Breed_Image(
        breed_id=35,
        img_url='https://doglime.com/wp-content/uploads/2019/03/Miniature-American-Shepherd.jpg'
    ),
        Breed_Image(
        breed_id=35,
        img_url='https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F06%2F14%2Fminiature-american-shepherd-vertical-jumping-208478711.jpg'
    ),
        Breed_Image(
        breed_id=36,
        img_url='https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F03%2F02%2Fborder-collie-green-field-268313239-2000.jpeg'
    ),
        Breed_Image(
        breed_id=36,
        img_url='https://www.pupvine.com/wp-content/uploads/2021/05/Male-Vs.-Female-Border-Collie-Can-You-Handle-Them-720x405.jpg'
    ),
        Breed_Image(
        breed_id=36,
        img_url='https://media-be.chewy.com/wp-content/uploads/2021/04/15160416/Border-Collie_Featured-Image.jpg'
    ),
        Breed_Image(
        breed_id=36,
        img_url='https://i.pinimg.com/474x/8a/f1/c9/8af1c93320d9b5a2ee930f6deeecd459--border-collie-mix-best-dogs.jpg'
    ),
        Breed_Image(
        breed_id=36,
        img_url='https://dogfoodsmart.com/wp-content/uploads/2021/05/Border_Collie_Life_Expectancy.jpg'
    ),
        Breed_Image(
        breed_id=36,
        img_url='http://iheartdogs.com/wp-content/uploads/2015/08/shutterstock_140916883.jpg'
    ),
        Breed_Image(
        breed_id=36,
        img_url='https://vetstreet.brightspotcdn.com/dims4/default/5d9d95a/2147483647/crop/0x0%2B0%2B0/resize/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2Fc3%2F54ed80c75711e0a5640050568d6ceb%2Ffile%2FBorder-Collie-3-645mk062411.jpg'
    ),
        Breed_Image(
        breed_id=37,
        img_url='https://blog.myollie.com/content/images/2020/03/chihuahua-puppy-on-grey-background--1-.jpg'
    ),
        Breed_Image(
        breed_id=37,
        img_url='https://www.petguide.com/wp-content/uploads/2013/02/chihuahua1.jpg'
    ),
        Breed_Image(
        breed_id=37,
        img_url='https://2.bp.blogspot.com/-G4vji4gGPi0/Vza9sHNTYDI/AAAAAAAAE58/H1QQKB2taCkBIJtEVITiI9kYvFkZfnS2gCLcB/s1600/Chihuahua-lying-down.jpg'
    ),
        Breed_Image(
        breed_id=37,
        img_url='https://i.pinimg.com/originals/65/0a/de/650ade94faae09ed46d230c7c20a98f5.jpg'
    ),
        Breed_Image(
        breed_id=37,
        img_url='https://puccicafe.com/wp-content/uploads/2020/09/Chihuahua-Traits-PUCCI-Cafe.jpg'
    ),
        Breed_Image(
        breed_id=37,
        img_url='https://www.zooplus.co.uk/magazine/wp-content/uploads/2019/12/chihuahua-UK.jpg'
    ),
        Breed_Image(
        breed_id=38,
        img_url='https://www.thesprucepets.com/thmb/hWG-gNdY8wVZ0G5-V2BloRy3UMs=/2837x2128/smart/filters:no_upscale()/HillaryKladkeGettyImages-964594770-505a264849384317a11e77259e8e5feb.jpg'
    ),
        Breed_Image(
        breed_id=38,
        img_url='https://vetstreet.brightspotcdn.com/dims4/default/ffc131a/2147483647/crop/0x0%2B0%2B0/resize/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2Fff%2F325bd0a80811e0a0d50050568d634f%2Ffile%2FVizsla-2-645mk062911.jpg'
    ),
        Breed_Image(
        breed_id=38,
        img_url='https://cdn.fotofits.com/petzlover/gallery/img/l/hungarian-wirehaired-vizsla-dogs-824850.jpg'
    ),
        Breed_Image(
        breed_id=38,
        img_url='https://blog.myollie.com/content/images/2021/09/Vizslapuppyoutdoors.jpg'
    ),
        Breed_Image(
        breed_id=38,
        img_url='https://cf.ltkcdn.net/dogs/images/orig/252973-1600x1030-vizsla-dog-breed-traits.jpg'
    ),
        Breed_Image(
        breed_id=38,
        img_url='https://i2.wp.com/puppytoob.com/wp-content/uploads/2017/07/Hungarian-Vizsla.jpeg?resize=750%2C421&ssl=1'
    ),
        Breed_Image(
            breed_id=39,
            img_url='https://images.pexels.com/photos/786773/pexels-photo-786773.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
        ),
        Breed_Image(
            breed_id=39,
            img_url='https://images.pexels.com/photos/1582835/pexels-photo-1582835.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
        ),
        Breed_Image(
            breed_id=39,
            img_url='https://images.pexels.com/photos/760618/pexels-photo-760618.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
        ),
        Breed_Image(
            breed_id=39,
            img_url='https://images.pexels.com/photos/4006590/pexels-photo-4006590.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
        ),
        Breed_Image(
        breed_id=40,
        img_url='https://dogsbestlife.com/wp-content/uploads/2019/11/Belgian-malinois-scaled.jpeg'
    ),
        Breed_Image(
        breed_id=40,
        img_url='https://vetstreet.brightspotcdn.com/dims4/default/871f72c/2147483647/thumbnail/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F2b%2F03%2F045cdbe54bd98ab051ece28a144f%2FBelgian-Malinois-AP-1PTFPZ-645sm101513.jpg'
    ),
        Breed_Image(
        breed_id=40,
        img_url='https://thehappypuppysite.com/wp-content/uploads/2019/02/Belgian-Malinois-Temperament-long.jpg'
    ),
        Breed_Image(
        breed_id=40,
        img_url='https://cf.ltkcdn.net/dogs/images/orig/258720-1600x1030-belgian-malinois-temperament.jpg'
    ),
        Breed_Image(
        breed_id=40,
        img_url='https://i.pinimg.com/originals/6c/46/f5/6c46f587a4701ff700f54a9c92f20ac3.jpg'
    ),
        Breed_Image(
        breed_id=41,
        img_url='https://dogtime.com/assets/uploads/gallery/maltese-dog-breed-picture/9-fullbody.jpg'
    ),
        Breed_Image(
        breed_id=41,
        img_url='https://thepetproject.in/wp-content/uploads/2020/09/Maltese-Lifespan-long.jpg'
    ),
        Breed_Image(
        breed_id=41,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Maltese-laying-down-in-a-chair.jpg'
    ),
        Breed_Image(
        breed_id=41,
        img_url='https://i.pinimg.com/originals/ee/a4/1c/eea41c427fb61cc3f8aa2a0bc6b236ad.jpg'
    ),
        Breed_Image(
        breed_id=41,
        img_url='https://spoiledmaltese.com/attachments/img_8779-jpg.257694/'
    ),
        Breed_Image(
        breed_id=41,
        img_url='https://img.dog-learn.com/dog-breeds/maltese/maltese-sz5.jpg'
    ),
        Breed_Image(
        breed_id=42,
        img_url='https://www.thesprucepets.com/thmb/ARk1MUmxIxix5Ci5LWR1PzhjlUc=/2121x1414/filters:fill(auto,1)/AdultWeimaranerinPark-465fadcefa954d09aca201d68c2826cb.jpg'
    ),
        Breed_Image(
        breed_id=42,
        img_url='https://www.dogzone.com/images/breeds/weimaraner.jpg'
    ),
        Breed_Image(
        breed_id=42,
        img_url='https://res.cloudinary.com/fleetnation/image/private/c_fit,w_1120/g_south,l_text:style_gothic2:%C2%A9%20Christian%20M%C3%BCller,o_20,y_10/g_center,l_watermark4,o_25,y_50/v1493724994/nwqlsm1uq4ynxe8vdykw.jpg'
    ),
        Breed_Image(
        breed_id=42,
        img_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSW3P-GCTpejlYXeCY540rO6nEjWT4NXZcYKU0maWvcT35hmiNAiEJiZ-mtCiNzikPNxPE&usqp=CAU'
    ),
        Breed_Image(
        breed_id=42,
        img_url='https://c.stocksy.com/a/0xn400/z9/1145326.jpg'
    ),
       Breed_Image(
        breed_id=42,
        img_url='https://vetstreet.brightspotcdn.com/dims4/default/477f20f/2147483647/thumbnail/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2Fe4%2Fe0%2Fab2376c743628f81cc23f6bac97b%2Fweimaraner-AP-18ULPF-645sm12913.jpg'
    ),
       Breed_Image(
        breed_id=43,
        img_url='https://upload.wikimedia.org/wikipedia/commons/6/6c/1Dog-rough-collie-portrait.jpg'
    ),
       Breed_Image(
        breed_id=43,
        img_url='https://st.depositphotos.com/1908759/2169/i/600/depositphotos_21697401-stock-photo-colli.jpg'
    ),
       Breed_Image(
        breed_id=43,
        img_url='https://elsrem.files.wordpress.com/2013/07/collie.jpg'
    ),
       Breed_Image(
        breed_id=43,
        img_url='https://i.pinimg.com/originals/ae/6c/09/ae6c09a89e029b003fef9221302a1bf2.jpg'
    ),
        Breed_Image(
        breed_id=43,
        img_url='https://assets.puzzlefactory.pl/puzzle/253/616/original.jpg'
    ),
        Breed_Image(
        breed_id=43,
        img_url='https://cdn.pixabay.com/photo/2020/05/28/12/11/sheep-dog-5230971_960_720.jpg'
    ),
        Breed_Image(
        breed_id=44,
        img_url='https://upload.wikimedia.org/wikipedia/commons/a/a5/Newfoundland_dog_Smoky.jpg'
    ),
        Breed_Image(
        breed_id=44,
        img_url='https://d17fnq9dkz9hgj.cloudfront.net/breed-uploads/2018/08/newfoundland-dog-card-medium.jpg?bust=1535567515&width=560'
    ),
        Breed_Image(
        breed_id=44,
        img_url='https://www.hospitalveterinariglories.com/wp-content/uploads/2020/03/terranova-676x451.jpg'
    ),
        Breed_Image(
        breed_id=44,
        img_url='https://i.pinimg.com/originals/0f/8d/de/0f8ddeb972ebd607e01c7b84614ccad4.jpg'
    ),
        Breed_Image(
        breed_id=44,
        img_url='https://dinoanimals.com/wp-content/uploads/2021/02/Newfoundland-dog-1.jpg'
    ),
        Breed_Image(
        breed_id=44,
        img_url='https://itsdogornothing.com/wp-content/uploads/2015/11/Newfoundland.jpg'
    ),
        Breed_Image(
        breed_id=45,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Rhodesian-Ridgeback-standing-in-profile-outdoors.jpg'
    ),
        Breed_Image(
        breed_id=45,
        img_url='https://wyattslist.com/wp-content/uploads/2017/09/rhodesianridgeback_adult.jpg'
    ),
        Breed_Image(
        breed_id=45,
        img_url='https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/13135405/ANC2016-Conformation-Hound-Group-David-0E9A5697.20191213183002111-500x486.jpg'
    ),
        Breed_Image(
        breed_id=45,
        img_url='https://www.loveyourdog.com/wp-content/uploads/2021/09/Rhodesian-Ridgeback-Dog.jpg'
    ),
        Breed_Image(
        breed_id=45,
        img_url='https://media.istockphoto.com/photos/beautiful-rhodesian-ridgeback-picture-id1212343227?k=20&m=1212343227&s=170667a&w=0&h=x94SwEhOuRUcL3Jenv22jSY1XS4IvflXW8Rv7V6BvSE='
    ),
        Breed_Image(
        breed_id=45,
        img_url='https://i.pinimg.com/474x/59/1e/84/591e84a297a6f94574f1dd00b83b7a16.jpg'
    ),
        Breed_Image(
        breed_id=46,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Shiba-Inu-standing-in-profile-outdoors.jpg'
    ),
        Breed_Image(
        breed_id=46,
        img_url='https://m.foolcdn.com/media/affiliates/images/shiba_inu_puppy_in_a_field_3wWwMo1.width-1200.jpg'
    ),
        Breed_Image(
        breed_id=46,
        img_url='https://parade.com/wp-content/uploads/2018/01/Shiba-Inu-FTR.jpg'
    ),
        Breed_Image(
        breed_id=46,
        img_url='https://gettotext.com/wp-content/uploads/2021/10/Shiba-Inu-SHIB-not-to-be-stopped-whats-behind.jpg'
    ),
        Breed_Image(
        breed_id=46,
        img_url='https://www.zooroyal.at/magazin/wp-content/uploads/2019/01/Shiba-Inu-.jpg'
    ),
        Breed_Image(
        breed_id=46,
        img_url='https://upload.wikimedia.org/wikipedia/commons/a/a3/Taro_%28black_and_tan%2C_reu%29_-_Chiko_%28rood%2C_reu%29_-_Ichigo_%28rood%2C_teef%29.jpg'
    ),
        Breed_Image(
        breed_id=47,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/West-Highland-White-Terrier-laying-down-in-the-grass.jpg'
    ),
        Breed_Image(
        breed_id=47,
        img_url='http://cdn.akc.org/westie_header_1.jpg'
    ),
        Breed_Image(
        breed_id=47,
        img_url='https://i.pinimg.com/originals/a0/8b/af/a08bafb2bcbf289baa1ae8beafd6c9d2.jpg'
    ),
        Breed_Image(
        breed_id=47,
        img_url='https://terriblyterrier.com/wp-content/uploads/2019/05/west-highland-white-terrier-feature.jpg'
    ),
        Breed_Image(
        breed_id=47,
        img_url='https://vetstreet.brightspotcdn.com/dims4/default/09a78ea/2147483647/thumbnail/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2Fcd%2F88fde0a81d11e0a0d50050568d634f%2Ffile%2Fwest-highland-white-terrier-5-645mk070111.jpg'
    ),
        Breed_Image(
        breed_id=47,
        img_url='https://i.pinimg.com/originals/14/a8/76/14a876465378131bc0c215d71664709e.jpg'
    ),
        Breed_Image(
        breed_id=48,
        img_url='https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F08%2F03%2Fbichon-frise-175833398-2000.jpg'
    ),
        Breed_Image(
        breed_id=48,
        img_url='https://www.thekennelclub.org.uk/media/1605/bichon-frise-standing.jpg?mode=pad&width=1000&rnd=132143802470000000'
    ),
        Breed_Image(
        breed_id=48,
        img_url='https://www.thegoodypet.com/wp-content/uploads/2020/06/what-is-the-temperaments-of-a-bichon-frise-1200x900.jpg'
    ),
        Breed_Image(
        breed_id=48,
        img_url='https://s.abcnews.com/images/Lifestyle/bichon-frise-westminster-winner5-ap-mem-180214_4x5_992.jpg'
    ),
        Breed_Image(
        breed_id=49,
        img_url='https://dogtime.com/assets/uploads/gallery/bloodhound-dog-breed-pictures/7-faceforward.jpg'
    ),
        Breed_Image(
        breed_id=49,
        img_url='http://web5.lifelearn.com/wp-content/uploads/2011/02/BloodHound1of1.jpg'
    ),
        Breed_Image(
        breed_id=49,
        img_url='https://s36700.pcdn.co/wp-content/uploads/2018/01/Bloodhound-600x400.jpg.optimal.jpg'
    ),
        Breed_Image(
        breed_id=49,
        img_url='https://www.thetimes.co.uk/imageserver/image/%2Fmethode%2Ftimes%2Fprod%2Fweb%2Fbin%2Fa0955992-d7c5-11e9-a836-b8a7068a08fb.jpg?crop=3369%2C4211%2C839%2C1628'
    ),
        Breed_Image(
        breed_id=49,
        img_url='https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F09%2F02%2Fbloodhound-four-puppies-873691218-2000.jpg'
    ),
        Breed_Image(
        breed_id=49,
        img_url='https://i.pinimg.com/originals/83/3d/58/833d5830517d7274f537d12a7352325f.jpg'
    ),
        Breed_Image(
        breed_id=50,
        img_url='https://vetstreet.brightspotcdn.com/dims4/default/563369a/2147483647/crop/0x0%2B0%2B0/resize/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2Ff9%2F5c7930a7f811e0a0d50050568d634f%2Ffile%2FPortugese-Water-Dog-2-645mk062811.jpg'
    ),
        Breed_Image(
        breed_id=50,
        img_url='https://www.k9rl.com/wp-content/uploads/2016/07/Portuguese-Water-Dog-Image.jpg'
    ),
        Breed_Image(
        breed_id=50,
        img_url='https://i1.wp.com/wagave.com/wp-content/uploads/2020/06/Portuguese_Water_Dog.jpg?fit=1200%2C867&ssl=1'
    ),
        Breed_Image(
        breed_id=50,
        img_url='https://images.squarespace-cdn.com/content/v1/5e45de34031fc90ac86298fa/1589040887032-24F79TORY1R48KAC5BMY/portuguese-water-dog-jaxi-kimball-art-museum-7931.jpg'
    ),
        Breed_Image(
        breed_id=50,
        img_url='https://images.squarespace-cdn.com/content/v1/5e45de34031fc90ac86298fa/1588963811014-FPNBU0ON1VY50QPB4U4Z/yare-portuguese-water-dogs-padfoot-portrait-7501.jpg'
    ),
        Breed_Image(
        breed_id=50,
        img_url='https://portraitofaportuguesewaterdog.files.wordpress.com/2017/01/apier3-shareable.jpg?w=1000'
    ),
        Breed_Image(
        breed_id=51,
        img_url='https://s3.amazonaws.com/images.gearjunkie.com/uploads/2021/04/ch.jpg'
    ),
        Breed_Image(
        breed_id=51,
        img_url='https://cdn.shopify.com/s/files/1/0053/9649/6456/articles/Chesapeake-Bay-Retriever-Breed-Profile-Hero-min-564269_1800x.png?v=1625947130'
    ),
        Breed_Image(
        breed_id=51,
        img_url='https://vetstreet.brightspotcdn.com/dims4/default/2ed2583/2147483647/crop/0x0%2B0%2B0/resize/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F71%2Fe869409e9411e0a2380050568d634f%2Ffile%2FChesapeake-Bay-Retriever-2-645mk062111.jpg'
    ),
        Breed_Image(
        breed_id=51,
        img_url='https://s3.amazonaws.com/ocn-media/e07b677f-0d47-467d-8da1-4d96c1ff46c1.png'
    ),
        Breed_Image(
        breed_id=51,
        img_url='https://www.k9rl.com/wp-content/uploads/2016/04/Chesapeake-Bay-Retriever-dog-breed.jpg'
    ),
        Breed_Image(
        breed_id=51,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Chesapeake-Bay-Retriever-hunting.jpg'
    ),
        Breed_Image(
        breed_id=53,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Saint-Bernard-On-White-01.jpg'
    ),
        Breed_Image(
        breed_id=53,
        img_url='https://media-be.chewy.com/wp-content/uploads/2021/06/02135531/Saint-Bernard-FeaturedImage.jpg'
    ),
        Breed_Image(
        breed_id=53,
        img_url='https://www.thesprucepets.com/thmb/lG6YBdOwDZ6UmIkJ2e4ChDl1Yoc=/2121x1193/smart/filters:no_upscale()/SaintBernard-GettyImages-973528124-0bdea12e02ea4d71a21a7fc7c0acb469.jpg'
    ),
        Breed_Image(
        breed_id=53,
        img_url='https://i.pinimg.com/originals/10/db/7d/10db7d31b07272343588e1eb32d6b904.jpg'
    ),
    Breed_Image(
        breed_id=53,
        img_url='https://bloximages.newyork1.vip.townnews.com/goldendalesentinel.com/content/tncms/assets/v3/editorial/e/e8/ee825168-8cc9-11eb-abe5-a72d623c8e98/605b7ce04cc00.image.jpg?resize=400%2C376'
    ),
        Breed_Image(
        breed_id=53,
        img_url='https://better-bred-cdn.azureedge.net/wp-content/uploads/2019/11/AdobeStock_58781044.jpeg'
    ),
        Breed_Image(
        breed_id=53,
        img_url='https://www.puppyviewer.com/breed-photos/st-bernard.jpg'
    ),
        Breed_Image(
        breed_id=52,
        img_url='https://www.dogtime.com/assets/uploads/2011/01/file_23146_dalmatian-460x290.jpg'
    ),
        Breed_Image(
        breed_id=52,
        img_url='https://spiritdogtraining.com/wp-content/uploads/2021/07/Dalmatian-1.png'
    ),
        Breed_Image(
        breed_id=52,
        img_url='https://www.rd.com/wp-content/uploads/2019/07/shutterstock_1161034495-scaled.jpg?fit=700,1024'
    ),
        Breed_Image(
        breed_id=52,
        img_url='https://dogsbreedusa.online/wp-content/uploads/2018/10/Spotted-Coach-Dog.jpg'
    ),
        Breed_Image(
        breed_id=52,
        img_url='https://www.orlandosentinel.com/resizer/2WW8dP_Zvim0a16C_WIAJXfr51I=/800x800/top/cloudfront-us-east-1.images.arcpublishing.com/tronc/J4YZLTJMUZAQ5BUIKJCTPGFVNI.JPG'
    ),
    Breed_Image(
        breed_id=54,
        img_url='https://www.akc.org/wp-content/uploads/2017/11/Papillon-On-White-01.jpg'
    ),
        Breed_Image(
        breed_id=54,
        img_url='https://dogfriendlyscene.co.uk/wp-content/uploads/2021/07/Papillon-Dog-Breed.png'
    ),
        Breed_Image(
        breed_id=54,
        img_url='https://www.thesprucepets.com/thmb/1fxUJ4sMNzmSn4QKWrp7FzO_enU=/1453x1453/smart/filters:no_upscale()/Papillon-GettyImages-713839323-6985913363dd4791852de6f246e6c15d.jpg'
    ),
        Breed_Image(
        breed_id=54,
        img_url='https://images2.minutemediacdn.com/image/upload/c_fit,f_auto,fl_lossy,q_auto,w_728/v1555996784/shape/mentalfloss/istock_000055044242_small.jpg'
    ),
        Breed_Image(
        breed_id=54,
        img_url='https://pbs.twimg.com/media/DzMEcbKX0AE_vYW.jpg'
    ),
        Breed_Image(
        breed_id=54,
        img_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXqjmTYiPag629B7UwwpdGVzfgtkDVL4xPFuOvye3zcyGHK0XuYMAGAI07A3Ki-liiuRo&usqp=CAU'
    ),

    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    # Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    # Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    #     Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
    ]
    
   


   
    db.session.add_all(breeds)



    db.session.commit()

def undo_breed_images():
    db.session.execute('TRUNCATE breed_images RESTART IDENTITY CASCADE;')
    db.session.commit()



    # Breed_Image(
    #     breed_id=,
    #     img_url=''
    # ),
 