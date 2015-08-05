from setuptools import find_packages, setup


setup(name='dialogKit',
    version='1.0',
    description='A dialog toolkit that works across a couple of font editing applications.',
    author='Tal Leming',
    author_email='tal@typesupply.com',
    license="MIT",
    package_dir = {'': 'Lib'},
    packages=find_packages('Lib'),
)
