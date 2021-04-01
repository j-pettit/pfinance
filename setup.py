from setuptools import find_packages, setup

setup(
    name='pfinance',
    packages=find_packages(include=['pfinance']),
    version='0.0.4',
    description='Financial mathematics library',
    author='Julian Pettit',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)