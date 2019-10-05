from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    varsion='0.1.0',
    author='Abhishek Dwivedi',
    author_email='abhishekdwivedi131@gmail.com',
    description='A utility for backing up PostgreSQL databases.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/abdwivedi7/pgbackup',
    packages=find_packages('src')
)
