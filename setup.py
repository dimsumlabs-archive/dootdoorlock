from setuptools import setup, find_packages


setup(
    name='dsldoor',
    version='2.0',
    description='DSL door control',
    author='DSL',
    url='https://github.com/dimsumlabs/dootdoorlock',
    setup_requires=['pyserial>=2.5'],
    packages=find_packages(),
    scripts = [
        'bin/doorctl',
        'bin/doord',
        'bin/door.sh',
        'bin/octopusd'
    ]
)
