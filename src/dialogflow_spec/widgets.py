# https://developers.google.com/actions/assistant/responses


class GACarouselTile(dict):
    """
      {
        "title": "Title of item 1",
        "description": "Description of item 1",
        "footer": "Item 1 footer",
        "image": {
          "url": "https://www.gstatic.com/mobilesdk/170329_assistant/assistant_color_96dp.png",
          "accessibilityText": "Google Assistant Bubbles"
        },
        "openUrlAction": {
          "url": "https://github.com"
        }
      }
    """
    def __init__(self, *, title, description,
                 footer=None, image_url=None, image_hint='nothing',
                 open_url=None):
        super().__init__()
        self.update({
            "title": title,
            "description": description
        })
        if footer is not None:
            self['footer'] = footer

        if image_url is not None:
            self['image'] = {
                "url": image_url,
                "accessibilityText": image_hint
            }

        if open_url is not None:
            self['openUrlAction'] = {
                "url": open_url
            }


class GAButton(dict):
    """
       {
            "title": "Read more",
            "openUrlAction": {
                "url": "https://knowyourmeme.com/memes/crying-cat"
            }
        }

    """

    def __init__(self, *, title, url):
        super().__init__()
        self.update({
            "title": title,
            "openUrlAction": {
                "url": url
            }
        })


class ValidResponsePiece(dict):
    pass


class GACard(ValidResponsePiece):
    """
    {
        "basicCard": {
            "title": "Crying cat meme",
            "formattedText": "Dank memes are dank.",
            "image": {
                "url": "https://i.kym-cdn.com/entries/icons/mobile/000/026/489/crying.jpg",
                "accessibilityText": "This is a cat."
                },
            "buttons": [
                {
                    "title": "Read more",
                    "openUrlAction": {
                        "url": "https://knowyourmeme.com/memes/crying-cat"
                    }
                }
            ],
            "imageDisplayOptions": "CROPPED"
        }
    }
    """

    def __init__(self, *, title, formatted_text, buttons, image_url, image_hint='',
                 image_display='CROPPED'):
        super().__init__()
        self.update({
            "basicCard": {
                "title": title,
                "formattedText": formatted_text,
                "image": {
                    "url": image_url,
                    "accessibilityText": image_hint
                },
                "buttons": [
                    *buttons
                ],
                "imageDisplayOptions": image_display
            }
        })


class GACarousel(ValidResponsePiece):
    def __init__(self, *, tiles):
        super().__init__()
        tiles = list(tiles)
        # all tiles must have the same elements

        tile_keys = set(tiles[0].keys())
        assert all(tile_keys == set(tile.keys()) for tile in tiles)

        self.update({
            "carouselBrowse": {
                "items": [*tiles]
            }
        })
