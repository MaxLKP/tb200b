from setuptools import setup, find_packages

setup(
    name = "tb200b",
    version = "0.1",
    author = 'Max K.',
    description = "Python serial interface for TB200B based gas sensors",
    url = 'https://github.com/MaxLKP/tb200b',
    license = 'MIT',
    packages = find_packages(),
    include_package_data = True,
    package_data = {},
    install_requires = ['pyserial'],
)