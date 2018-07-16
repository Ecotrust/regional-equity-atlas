import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='rea',
    version='0.0.1',
    packages=['rea'],
    include_package_data=True,
    license='MIT',
    description='Regional Equity Atlas Marineplanner Module',
    long_description=README,
    url='https://github.com/Ecotrust/regional-equity-atlas',
    author='Ecotrust',
    author_email='ksdev@ecotrust.org',
    classifiers=[
        'Environment :: Web Development',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
