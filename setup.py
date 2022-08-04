from setuptools import setup

setup(
    name='src',
    version='0.0.1',
    author='Subhradipta Paul & Arnab Mitra',
    description='Face Monitering System',
    packages=['src'],
    install_requires=['flask','flask-cors','sklearn','pandas','numpy','mysql-connector-python']
)