from setuptools import setup

with open("README.rst") as f:
    long_description = f.read()

setup(
    name='Dragon Masher',
    version='0.1dev',
    author='Thomas Roten',
    author_email='thomas@roten.us',
    url='https://github.com/tsroten/dragonmasher',
    description='',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    keywords=[],
    py_modules=[],
    packages=['dragonmasher'],
    test_suite='dragonmasher.tests',
)