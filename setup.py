from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setup(
   name='graph-generators',
   python_requires='>= 3.5',
   version='0.1.7',
   author='Chai Wah Wu',
   author_email='cwwuieee@gmail.com',
   packages=find_packages(),
   url='https://github.com/postvakje/graph-generators',
   license='LICENSE',
   description='Python functions to compute various classes of networkx graphs',
   long_description=long_description,
   long_description_content_type='text/markdown',
   install_requires=requirements,
   classifiers = ['Programming Language :: Python :: 3',
                'License :: OSI Approved :: Apache Software License',
                'Operating System :: OS Independent',  
                'Topic :: Scientific/Engineering :: Mathematics',
				'Topic :: Scientific/Engineering :: Information Analysis',
                'Development Status :: 4 - Beta',
				'Intended Audience :: Science/Research',
   ],
)