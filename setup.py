from setuptools import setup

from chubby.version import VERSION


with open('requirements.txt') as req:
    dependencies = req.read().splitlines()

with open('README.rst') as readme:
    long_description = readme.read()


if __name__ == "__main__":
    setup(
        name='chubby',
        version=VERSION,
        description="Misc. GitHub actions in your terminal",
        long_description=long_description,
        author="Meet Mangukiya",
        author_email="meetmangukiya98@gmail.com",
        maintainer="Meet Mangukiya",
        maintainer_email=("meetmangukiya98@gmail.com", ),
        url="http://meetmangukiya.github.io",
        install_requires=dependencies,
        license='MIT',
        packages=['chubby'],
        entry_points={
            'console_scripts': [
                'chubby=chubby.chubby:main'
            ]
        }
    )
