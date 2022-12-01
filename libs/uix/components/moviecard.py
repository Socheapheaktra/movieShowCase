from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard

from kivy.lang.builder import Builder
from kivy.properties import StringProperty

card_view = """
#: import AsyncImage kivy.uix.image
<MovieCard>:
    orientation: "vertical"
    spacing: 20
    size_hint_y: None
    height: self.minimum_height
    radius: [25, 25, 25, 25]
    
    FitImage:
        radius: [25, 25, 0, 0]
        adaptive_size: True
        size_hint_y: None
        height: self.minimum_height
        size: dp(100), dp(200)
        source: root.image
        
    MDBoxLayout:
        orientation: "vertical"
        spacing: 10
        padding: 10, 20
        size_hint_y: None
        height: self.minimum_height
        
        MDLabel:
            text: root.title
            adaptive_height: True
        MDLabel:
            text: root.year
            adaptive_height: True
    
"""

Builder.load_string(card_view)

class MovieCard(MDCard):
    movie_id = StringProperty()
    title = StringProperty()
    year = StringProperty()
    image = StringProperty()
    background_image = StringProperty()
    duration = StringProperty()
    description = StringProperty()
    date_upload = StringProperty()
    def __init__(self, movie_id, title, year, image, background_image, duration, description, date_upload, **kwargs):
        super().__init__(**kwargs)
        self.movie_id = movie_id
        self.title = title
        self.year = year
        self.image = image
        self.background_image = background_image
        self.duration = duration
        self.description = description
        self.date_upload = date_upload