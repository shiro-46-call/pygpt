from setuptools import setup, find_packages

setup(
    name='pygpt',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'command=Example:main',
        ],
    },
    install_requires=[
        'openai',
        'python-dotenv',
        'colorama'
    ],
)
