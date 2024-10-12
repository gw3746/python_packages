from setuptools import setup, find_packages

setup(
    name='con2mailserver',
    version='0.1',
    packages=find_packages(),
    description='A utility for con2hinet or con2gmail',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Robert Su',
    author_email='bertsu@fuxipc.com',
    #url='https://github.com/gw3746/python_packages/con2mailserver',
    url='git@github.com:gw3746/python_packages.git',
    install_requires=[
        'imapclient',        
              
        
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)