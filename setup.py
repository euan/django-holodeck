from setuptools import setup, find_packages

setup(
    name='django-holodeck',
    version='0.1.1',
    description='Django based simple dashboard system.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Shaun Sephton',
    author_email='shaun@28lines.com',
    url='http://github.com/shaunsephton/holodeck',
    packages = find_packages(),
    install_requires = [
        'django==1.6',
        'south',
        'xlwt',
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
