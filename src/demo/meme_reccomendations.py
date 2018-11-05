from _api_dispatcher import register_intent
from dialogflow_spec import make_response
from dialogflow_spec.actions_objects import GACarouselTile, GACarousel


_MEME_TYPES_TO_CAROUSELS = {
    'sad': GACarousel(
        tiles=[
            GACarouselTile(
                title='Crying Cat',
                description='''Crying Cat, also known as Schmuserkadser, refers to a series of photoshopped images of cats with teary, glassy eyes to appear as though they are sad.''',
                image_url='https://i.kym-cdn.com/photos/images/newsfeed/001/384/545/7b9.jpg',
                open_url='https://knowyourmeme.com/memes/crying-cat'
            ),
            GACarouselTile(
                title='Pepe',
                description='''Pepe the Frog is an anthropomorphic frog character from the comic series Boy’s Club by Matt Furie. On 4chan, various illustrations of the frog creature have been used as reaction faces, including Feels Good Man, Sad Frog, Angry Pepe, Smug Frog and Well Meme'd.''',
                image_url='https://i.kym-cdn.com/entries/icons/mobile/000/017/618/pepefroggie.jpg',
                open_url='https://knowyourmeme.com/memes/pepe-the-frog'
            ),
            GACarouselTile(
                title='Sad Keanu',
                description='Sad Keanu is a photoshop meme based on a paparazzi photograph of the Canadian American actor Keanu Reeves sitting on a park bench and enjoying a sandwich by himself.',
                image_url='https://i.kym-cdn.com/entries/icons/mobile/000/002/862/SadKeanu.jpg',
                open_url='https://knowyourmeme.com/memes/sad-keanu'
            ),
        ]
    ),
    'animal': GACarousel(
        tiles=[
            GACarouselTile(
                title='Doge',
                description='''Doge is a slang term for "dog" that is primarily associated with pictures of Shiba Inus (nicknamed "Shibe") and internal monologue captions on Tumblr. These photos may be photoshopped to change the dog's face or captioned with interior monologues in Comic Sans font.''',
                image_url='https://i.kym-cdn.com/photos/images/masonry/000/581/296/c09.jpg',
                open_url='https://knowyourmeme.com/memes/doge'
            ),
            GACarouselTile(
                title='Confession Bear',
                description='''Confession Bear is an advice animal image macro series featuring a photo of a Malayan sun bear leaning against a log. The images are captioned with confessions about taboo behaviors and controversial opinions that are often kept secret for fear of being ostracized.''',
                image_url='https://i.kym-cdn.com/entries/icons/mobile/000/010/639/confessbear.jpg',
                open_url='https://knowyourmeme.com/memes/confession-bear'
            ),
        ]
    ),
}


@register_intent('meme-advisor')
def meme_recommendations_handler(request_data):
    params = request_data['queryResult']['parameters']

    meme_type_to_response = {
        'sad': 'There is a great choice of sad memes, have a look.',
        'animal': "I've got something here for you!",
    }
    message = meme_type_to_response.get(params['meme-type'])

    if message is not None:
        return make_response(message, _MEME_TYPES_TO_CAROUSELS[params['meme-type']])
    else:
        return make_response(f'''Sorry, but I don't know any memes of this type - {params["joke-type"]}.''')
