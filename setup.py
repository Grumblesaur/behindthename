import setuptools

with open('README.md', 'r') as f:
  long_description = f.read()

with open('requirements.txt', 'r') as f:
  requirements = f.read().splitlines()

setuptools.setup(
  name='behindthename',
  version='0.1.2',
  author='James Murphy',
  author_email='james.frank.murphy@protonmail.com',
  description='A simple API wrapper for behindthename.com',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/Grumblesaur/behindthename',
  install_requires=requirements,
  packages=setuptools.find_packages(),
  classifiers=[],
  python_requires='>=3.6',
)
