from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.toast import toast
from kivymd.utils import asynckivy

from kivy.lang.builder import Builder
from kivy.clock import Clock

from libs.uix.components.moviecard import MovieCard
from libs.uix.baseclass.detail_screen import DetailScreen

from libs.utils.ListMovie import *

import json, time

Builder.load_file("libs//uix//kv//main_screen.kv")

Builder.load_string("""
<LoadingSpinner>:
    size_hint_y: None
    height: self.children[0].height * 2
    MDSpinner:
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .7}
        determinate: False
""")

class LoadingSpinner(MDRelativeLayout):
    pass

class MainScreen(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.page = 1
        self.dialog = None
        self.refresh_dialog = MDDialog(
            type="custom",
            content_cls=LoadingSpinner(),
        )

        self.on_start()

    def on_start(self):
        self.page = 1
        try:
            self.default_action_movies()
            data = home_page()
        except Exception as err:
            self.dialog = MDDialog(
                title="Error!",
                text="Please try again!",
                buttons=[
                    MDRaisedButton(
                        text="Try Again!",
                        on_release=lambda x: self.on_start()
                    )
                ]
            )
            self.dialog.open()
        else:
            movies = data['data']
            self.ids.content.clear_widgets()
            for movie in movies:
                self.ids.content.add_widget(MovieCard(
                    movie_id=str(movie['id']),
                    title=movie['title'],
                    year=str(movie['year']),
                    image=str(movie['large_cover_image']),
                    background_image=f"{movie['background_image_original']}",
                    duration=str(movie['runtime']),
                    description=f"{movie['description_full']}",
                    date_upload=f"{movie['date_uploaded']}",
                    on_release=lambda x=movie: self.movie_detail(x)
                ))
            self.goto_main()

    def set_list(self):
        async def set_list():
            names_icons_list = list(md_icons.keys())[self.x:self.y]
            for name_icon in names_icons_list:
                await asynckivy.sleep(0)
                self.screen.ids.box.add_widget(
                    ItemForList(icon=name_icon, text=name_icon))
        asynckivy.start(set_list())

    def add_movie(self):
        async def add_movie():
            try:
                data = next_page(cur_page=self.page)
            except Exception as err:
                self.dialog = MDDialog(
                    title="Error!",
                    text="Please try again!",
                    buttons=[
                        MDRaisedButton(
                            text="Try Again!",
                            on_release=lambda x: self.on_start()
                        )
                    ]
                )
                self.dialog.open()
            else:
                movies = data['data']
                for movie in movies:
                    # await asynckivy.sleep(0)
                    self.ids.content.add_widget(MovieCard(
                        movie_id=str(movie['id']),
                        title=movie['title'],
                        year=str(movie['year']),
                        image=str(movie['large_cover_image']),
                        background_image=f"{movie['background_image_original']}",
                        duration=str(movie['runtime']),
                        description=f"{movie['description_full']}",
                        date_upload=f"{movie['date_uploaded']}",
                        on_release=lambda x=movie: self.movie_detail(x)
                    ))
                    await asynckivy.sleep(0)
                self.page += 1
                # await asynckivy.sleep(5)
        asynckivy.start(add_movie())

    def default_action_movies(self):
        try:
            data = default_action()
        except Exception as err:
            self.dialog = MDDialog(
                title="Error!",
                text="Please try again!",
                buttons=[
                    MDRaisedButton(
                        text="Try Again!",
                        on_release=lambda x: self.on_start()
                    )
                ]
            )
            self.dialog.open()
        else:
            movies = data['data']
            self.ids.content_action.clear_widgets()
            for movie in movies:
                self.ids.content_action.add_widget(MovieCard(
                    movie_id=str(movie['id']),
                    title=movie['title'],
                    year=str(movie['year']),
                    image=str(movie['large_cover_image']),
                    background_image=f"{movie['background_image_original']}",
                    duration=str(movie['runtime']),
                    description=f"{movie['description_full']}",
                    date_upload=f"{movie['date_uploaded']}",
                    on_release=lambda x=movie: self.movie_detail(x)
                ))

    def on_search(self, title):
        def return_main_screen():
            self.close_dialog()
            self.on_start()
        if title != "":
            query = "+".join(title.split(" "))
            try:
                data = search_result(query)
            except Exception as err:
                self.dialog = MDDialog(
                    title="Error!",
                    text=f"{err}",
                    buttons=[
                        MDRaisedButton(
                            text="Close",
                            on_release=lambda x: return_main_screen()
                        )
                    ]
                )
                self.dialog.open()
            else:
                if data['status'] is True:
                    self.ids.search_content.clear_widgets()
                    movies = data['data']
                    for movie in movies:
                        self.ids.search_content.add_widget(MovieCard(
                            movie_id=str(movie['id']),
                            title=movie['title'],
                            year=str(movie['year']),
                            image=str(movie['large_cover_image']),
                            background_image=f"{movie['background_image_original']}",
                            duration=str(movie['runtime']),
                            description=f"{movie['description_full']}",
                            date_upload=f"{movie['date_uploaded']}",
                            on_release=lambda x=movie: self.movie_detail(x)
                        ))
                    self.goto_search()
                else:
                    self.dialog = MDDialog(
                        title="Error!",
                        text=f"{data['message']}",
                        buttons=[
                            MDRaisedButton(
                                text="Close",
                                on_release=lambda x: return_main_screen()
                            )
                        ]
                    )
                    self.dialog.open()
        else:
            self.on_start()

    def focus_search(self):
        self.ids.search_fld.focus = True

    def goto_main(self):
        self.ids.scrn_mngr.transition.direction = 'right'
        self.ids.scrn_mngr.current = "main_scrn"
        self.ids.search_fld.text = ""

        self.ids.toolbar.left_action_items = [
            ['home', lambda x: self.on_start()]
        ]

        self.ids.toolbar.right_action_items = [
            ['magnify', lambda x: self.focus_search()]
        ]

    def goto_detail(self):
        self.ids.scrn_mngr.transition.direction = 'left'
        self.ids.scrn_mngr.current = "detail_scrn"

    def goto_search(self):
        self.ids.scrn_mngr.transition.direction = "left"
        self.ids.scrn_mngr.current = "search_scrn"

        self.ids.toolbar.left_action_items = [
            ['arrow-left-bold', lambda x: self.goto_main()]
        ]

        self.ids.toolbar.right_action_items = []

    def movie_detail(self, movie):
        self.ids.detail_scrn.clear_widgets()
        self.ids.toolbar.left_action_items = []
        self.ids.toolbar.right_action_items = []
        detail_screen = DetailScreen(
            movie_id=f"{movie.movie_id}",
            title=movie.title,
            description=movie.description,
            year=f"{movie.year}",
            runtime=f"{movie.duration}",
            image=f"{movie.image}",
            date_upload=f"{movie.date_upload}"
        )

        self.ids.detail_scrn.add_widget(detail_screen)
        self.ids.toolbar.left_action_items = [
            ['arrow-left-bold', lambda x: self.goto_main()]
        ]
        self.goto_detail()

    def refresh_callback(self, scroll_value, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback(interval):
            self.add_movie()
            self.refresh_dialog.dismiss()
        if scroll_value < 0:
            self.refresh_dialog.open()
            Clock.schedule_once(refresh_callback, 3)
        else:
            pass
    def close_dialog(self, *args):
        self.dialog.dismiss(force=True)