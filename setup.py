from setuptools import setup

with open('README.rst') as README:
    long_description = README.read()
    long_description = long_description[long_description.index('Description'):]

setup(name='timeme',
      version='0.1.1',
      description='Decorator that prints the running time of a function',
      long_description=long_description,
      url='http://github.com/enricobacis/timeme',
      author='Enrico Bacis',
      author_email='enrico.bacis@gmail.com',
      license='MIT',
      packages=['timeme'],
      keywords='time timing function decorator'
)
