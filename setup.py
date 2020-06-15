from setuptools import setup

setup(
    name='snapshotalyzer99',
    version='1.0',
    author='Ravi Goel',
    description='snapshotalyzer99 is a tool to manage AWS EC2 instances',
    license='GPLv3+',
    packages=['shotty'],
    url="https://github.com/rvgoel/snapshotalyzer-99",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
