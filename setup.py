from setuptools import find_packages, setup
setup(
    name="distributedpython",
    packages=find_packages(include=['distributedpython']),
    version="0.1.0",
    description="Run Python code on the Distributed Compute Protocol",
    author="George Shao",
    author_email="georgeshao123@gmail.com",
    license='gpl-3.0',
    install_requires=[],
)