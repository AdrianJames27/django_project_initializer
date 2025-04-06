from setuptools import setup, find_packages

setup(
    name='django_project_initializer',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here, e.g., 'gitpython'
    ],
    entry_points={
        'console_scripts': [
            'django-init=django_project_initializer.project_initializer:main',
        ],
    },
)
