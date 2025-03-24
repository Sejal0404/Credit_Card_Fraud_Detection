from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='your_package_name',  # Replace with your package name
    version='0.1.0',           # Replace with your package version
    author='Your Name',        # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    description='A brief description of your package',
    packages=find_packages(),
    install_requires=requirements,
)
