from setuptools import setup, find_packages

setup(
    name='hello-world',
    version='0.1',
    description='Hello World Example',
    author='Andrej',
    author_email='akubek@gmail.com',
    license='Public Domain',
    url='https://gist.github.com/63fb02bf7fca9c9d68ee3b4ad942d43e.git',
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        ],
    zip_safe=False,
)