from setuptools import setup
import os

VERSION = '0.1.0'
PROJECT = 'quantum-sg'
AUTHOR = u'Alexander Shelepenok'
AUTHOR_EMAIL = u'alxshelepenok@gmail.com'
URL = 'https://github.com/alxshelepenok/quantum-sg'
DESCRIPTION = "A command line tool that generates a cryptographically secure quantum-level secrets using ANU QRNG."


def read_file(file_name):
    file_path = os.path.join(
        os.path.dirname(__file__),
        file_name
    )
    return open(file_path).read()


setup(
    url=URL,
    name=PROJECT,
    author=AUTHOR,
    version=VERSION,
    description=DESCRIPTION,
    author_email=AUTHOR_EMAIL,
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    zip_safe=True,
    include_package_data=True,
    packages=['quantum_sg'],
    keywords='quantum random secrets',
    install_requires=['quantumrandom'],
    entry_points="""
        [console_scripts]
        quantum-sg = quantum_sg.quantum_sg:main
      """,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
