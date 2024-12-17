import reflex as rx
from .screens.autentication_screen import autentication
from .screens.download_screen import download
from .screens.favorite_screen import favorite
from .screens.home_screen import home
from .screens.login_screen import login
from .screens.register_screen import register
from .screens.splash_screen import splash
from .screens.umboarding1 import umboarding1
from .screens.umboarding2 import umboarding2
from .screens.umboarding3 import umboarding3
from rxconfig import config

def index() -> rx.Component:
    return rx.mobile_and_tablet(
        splash()
    )
app = rx.App()
app.add_page(index)
