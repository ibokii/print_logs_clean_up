from setuptools import setup, find_packages


def load_requirements(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()


setup(
    name='log_cleaner_project',
    version='1.0.0',
    packages=find_packages(),
    install_requires=load_requirements('requirements.txt'),
    python_requires='>=3.9',
)
