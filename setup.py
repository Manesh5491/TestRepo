from setuptools import setup, find_packages
setup(
    name = "testRepo",
    version = "0.1",
    packages = find_packages(),
    author = '',
    author_email = '',
    description = 'Automation Library',
    long_description='Api for automation',
    url = 'https://github.com/Manesh5491/TestRepo', # The URL to the github repo
    download_url = 'https://github.com/Manesh5491/TestRepo.git',
    license='MIT',# Choose your license
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. 
        'Programming Language :: Python :: 2.7'
        ],
    install_requires=[
        "pytest==3.0.1",
        "Appium-Python-Client==0.22"
        ],
    )
