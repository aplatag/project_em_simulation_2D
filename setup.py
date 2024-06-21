from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup (
    name='em_simulation',
    version='0.6',
    license='MIT',
    description='2D Electromagnetic Simulator for GPR Scenarios',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Aplatag',
    packages=find_packages(),
    install_requires = ['numpy'],

    url='https://github.com/aplatag/project_em_simulation_2D.git'
)