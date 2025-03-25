from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Credit_Card_Fraud_Detection',  # Replace with your package name
    version='0.0.1',           # Replace with your package version
    author='Sejal',        # Replace with your name
    author_email='sejalofficial1507@gmail.com',  # Replace with your email
    description='A project for detecting whether there will be fraud or not',
    packages=find_packages(),
    install_requires=requirements,
)
