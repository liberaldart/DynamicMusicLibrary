from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Music Collector'
settings.subtitle = 'powered by web2py'
settings.author = 'Amit Singh'
settings.author_email = 'aksinghdce@gmail.com'
settings.keywords = 'Download Youtube audio'
settings.description = 'We will be using pafy library'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '622fe752-912c-4f57-9795-d20ce8938d23'
settings.email_server = 'localhost'
settings.email_sender = 'aksinghdce@gmail.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
