import setuptools  # type: ignore

with open('README.md', 'rt') as f:
    long_description = f.read()

setuptools.setup(
    name='showdialog',
    version='1.0.0',
    author='Chechkenev Andrey (@DarkCat09)',
    author_email='aacd0709@mail.ru',
    description='Simple module for showing GTK dialog',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 6 - Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'PyGObject>=3.42.2'
    ],
    packages=['showdialog'],
    python_requires=">=3.6",
)
