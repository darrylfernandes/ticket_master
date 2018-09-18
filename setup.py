# from distutils.core import setup, find_packages
from setuptools  import setup, find_packages

setup(
    name='book_movie_tickets',
    description="Loads Movies and calculates the cheapest price available",
    version='0.1.0',
    packages=find_packages(exclude=['*/__pycache__']),
    author="Darryl Fernandes",
    author_email="darrylfernandes@gmail.com",
    # Include additional files into the package
    include_package_data=True,
    long_description=open('README.md').read(),
    install_requires=['click==6.7',
                      'Flask==1.0.2',
                      'itsdangerous==0.24',
                      'Jinja2==2.10',
                      'MarkupSafe==1.0',
                      'Werkzeug==0.14.1'],
)
