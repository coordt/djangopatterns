# ... other stuff above

setup(
    name = "$$$$APP_NAME$$$$",
    version = __import__('$$$$PKG_NAME$$$$').get_version().replace(' ', '-'),
    url = '$$$$URL$$$$',
    author = '$$$$AUTHOR$$$$',
    author_email = '$$$$AUTHOR_EMAIL$$$$',
    description = DESC,
    long_description = get_readme(),
    packages = find_packages(),
    include_package_data = True,
    install_requires = read_file('requirements.txt'),
    classifiers = [
        'License :: OSI Approved :: Apache Software License',
        'Framework :: Django',
    ],
)
