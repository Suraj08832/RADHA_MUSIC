from RADHA_MUSIC.core.bot import RADHA
from RADHA_MUSIC.core.dir import dirr
from RADHA_MUSIC.core.git import git
from RADHA_MUSIC.core.userbot import Userbot
from RADHA_MUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = RADHA()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
