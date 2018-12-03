import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = ''
insta_password = ''

# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username="navi.clicks",
                  password="D0aba41",
                  headless_browser=False,
                  multi_logs=True)

try:
    session.login()

    # settings
    session.set_relationship_bounds(enabled=True,
				 potency_ratio=-0.9,
				  delimit_by_numbers=True,
				   max_followers=4590,
				    max_following=5555,
				     min_followers=45,
				      min_following=77)
    # session.set_do_comment(True, percentage=95)
    # session.set_comments(['aMEIzing!', 'cool shot', 'Nicey!'])
    # session.set_dont_include(['friend1', 'friend2', 'friend3'])
    # session.set_dont_like(['pizza', 'girl'])
    # session.set_comments(['Amazing post @{}'],media='Photo')
    session.set_user_interact(amount=5, randomize=True, percentage=95, media='Photo')
    
    # actions
    session.like_by_tags(['welivetoexplore', 'travel', 'roadtrip'], amount=100)

except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()
