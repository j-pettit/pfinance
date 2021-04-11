from setuptools import find_packages, setup

setup(
    name='pfinance',
    version='0.0.6',
    author='Julian Pettit',
    license='MIT',
    description='Financial mathematics library',
    packages=find_packages(include=['pfinance']),
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
