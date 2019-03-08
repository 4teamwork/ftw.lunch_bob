import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = 'lunch_bob'
VERSION = '0.0.1'
AUTHOR = '4teamwork'
EMAIL = 'info@4teamwork.ch'
DESCRIPTION = 'Slack Bot App telling us what there is to eat today.'
URL = 'https://github.com/4teamwork/lunch_bob'
REQUIRED = [
    'python-dotenv==0.9.1',
    'slackclient==1.3.0'
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRED,
    entry_points={
        'console_scripts': ['bob_tell_lunch_options=lunch_bob.command_line:main'],
    },
)
