# coding: utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='django_datetime',
    version='0.0.1',
    description='datetime extension using Django',
    long_description='',
    url='',
    author='Hirokazu Miyaji',
    maintainer_email='hirokazu.miyaji@gmail.com',
    keywords=['Django', 'datetime'],
    license='MIT',
    packages=['django_datetime'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)
