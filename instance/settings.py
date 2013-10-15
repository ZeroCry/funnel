# -*- coding: utf-8 -*-

#: The title of this site
SITE_TITLE='OSDConf 2014 Funnel'
#: Support contact email
SITE_SUPPORT_EMAIL = 'test@example.com'
#: TypeKit code for fonts
TYPEKIT_CODE=''
#: Google Analytics code UA-XXXXXX-X
GA_CODE=''
#: Database backend
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
#: Secret key
SECRET_KEY = 'this is random enough in the meantime'
#: Timezone
TIMEZONE = 'Asia/Calcutta'
#: LastUser server
LASTUSER_SERVER = 'https://auth.hasgeek.com/'
#: LastUser client id
LASTUSER_CLIENT_ID = ''
#: LastUser client secret
LASTUSER_CLIENT_SECRET = ''
#: Used for attribution when shared a proposal on twitter
TWITTER_ID = "jiitosdc"
#: Mail settings
#: MAIL_FAIL_SILENTLY : default True
#: MAIL_SERVER : default 'localhost'
#: MAIL_PORT : default 25
#: MAIL_USE_TLS : default False
#: MAIL_USE_SSL : default False
#: MAIL_USERNAME : default None
#: MAIL_PASSWORD : default None
#: DEFAULT_MAIL_SENDER : default None
MAIL_FAIL_SILENTLY = False
MAIL_SERVER = 'localhost'
DEFAULT_MAIL_SENDER = ('JIIT OSDC', 'jiit.osdc@gmail.com')

# Required for Flask-Mail to work.
MAIL_DEFAULT_SENDER = DEFAULT_MAIL_SENDER
#: Logging: recipients of error emails
ADMINS=[]
#: Log file
LOGFILE='error.log'

#: Messages (text or HTML)
WELCOME_MESSAGE = "The funnel is a space for proposals and voting on events. Pick an event to get started."

NETWORKBAR_LINKS = [
	{
		'children': None,
		'name': 'home',
		'url': '/',
		'title': 'OSDConf Home',
		'sep': False
	}]
