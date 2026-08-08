"""WhiteNoise middleware subclass that also serves uploaded media files.

Render's free tier has no CDN, so we serve MEDIA_ROOT (admin uploads such as
the profile picture and resume) through WhiteNoise alongside static files.
"""
import os

from django.conf import settings
from whitenoise.middleware import WhiteNoiseMiddleware


class MediaWhiteNoiseMiddleware(WhiteNoiseMiddleware):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_files(
            os.path.abspath(str(settings.MEDIA_ROOT)),
            prefix=settings.MEDIA_URL,
        )
