sys.path.append(os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'example.settings'

import categories

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = categories.get_version(short=True)
# The full version, including alpha/beta/rc tags.
release = categories.get_version()