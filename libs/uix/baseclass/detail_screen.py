from kivymd.uix.boxlayout import MDBoxLayout

from kivy.lang.builder import Builder
from kivy.properties import StringProperty

Builder.load_file("libs//uix//kv//detail_screen.kv")

class DetailScreen(MDBoxLayout):
    movie_id = StringProperty()
    title = StringProperty()
    description = StringProperty()
    year = StringProperty()
    image = StringProperty()
    date_upload = StringProperty()
    runtime = StringProperty()
    def __init__(self, movie_id, title, description, year, runtime,  image, date_upload, **kwargs):
        super().__init__(**kwargs)
        self.movie_id = movie_id
        self.title = title
        self.description = description
        self.year = year
        self.runtime = runtime
        self.image = image
        self.date_upload = date_upload