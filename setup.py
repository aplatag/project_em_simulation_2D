from setuptools import setup, find_packages


setup (
    name='project_em_simulation_2D',
    version='0.0.1',
    license='MIT',
    description='2D Electromagnetic Simulator for GPR Scenarios',
    long_description=open('README.md',encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Aplatag',
    packages=find_packages(),
    install_requires = ['math','numpy','time'],

    url='https://github.com/aplatag/project_em_simulation_2D.git'
)