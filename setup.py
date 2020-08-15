from setuptools import find_packages, setup
setup(
    name="distributedpython",
    packages=find_packages(include=['distributedpython']),
    version="1.0.0",
    description="Python library to run Python code on the Distributed Compute Protocol",
    author="George Shao",
    author_email="georgeshao123@gmail.com",
    license='gpl-3.0',
    install_requires=[],
)