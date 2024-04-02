from setuptools import setup, find_packages

setup(
    name='e-note-api',
    version='0.1.0',
    author='Nielo Wait',
    author_email='nielo@vrzchampions.world',
    description='A RESTful API for emoji sequence suggestions and management.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/a-nom-ali/e-note-api', # Replace with the real URL
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'sqlalchemy',
        'flask_sqlalchemy',
        'flask_migrate',
        'flask_marshmallow',
        'marshmallow-sqlalchemy',
        'flask_jwt_extended',
        # Add other dependencies as necessary
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8', # Replace with your Python version
        'Framework :: Flask',
    ],
    entry_points={
        'console_scripts': [
            'e-note-api=e-note-api.main:main', # Replace e-note-api.main with the correct import path
        ],
    },
)
