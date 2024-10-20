from setuptools import setup, find_packages

setup(
    name='con2cao',
    version='0.1',
    packages=find_packages(),
    description='A utility for converting PostgreSQL types to MySQL types',
    #long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Robert Su',
    author_email='bertsu@fuxipc.com',
    #url='https://github.com/gw3746/python_packages/con2cao',
    url='git@github.com:gw3746/python_packages.git',
    install_requires=[
        'pyodbc',
        
        'mysql.connector-python',
        'datetime',
        
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)