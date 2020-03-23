from whitenoise import WhiteNoise
from app import a

application = WhiteNoise(a)
application.add_files('static/', prefix='static/')
