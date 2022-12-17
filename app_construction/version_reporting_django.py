VERSION = (1, 4, 0, 'alpha', 0)

def get_version():
    version = f'{VERSION[0]}.{VERSION[1]}'
    if VERSION[2]:
        version = f'{version}.{VERSION[2]}'
    if VERSION[3:] == ('alpha', 0):
        version = f'{version} pre-alpha'
    elif VERSION[3] != 'final':
        version = f'{version} {VERSION[3]} {VERSION[4]}'
    from django.utils.version import get_svn_revision
    svn_rev = get_svn_revision()
    if svn_rev != u'SVN-unknown':
        version = f"{version} {svn_rev}"
    return version
