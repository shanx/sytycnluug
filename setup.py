from setuptools import setup, find_packages

version = '1.0dev'

setup(
    name='sytycnluug',
    version=version,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'lxml',
        'Django',
        'south',
        ])
