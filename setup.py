from setuptools import setup, find_packages

setup(
    name="basicauth-http-server",
    version="0.0.1",
    description='Simple HTTP and HTTPS Auth Server',
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "click==7.1.2"
    ],
    entry_points={
        'console_scripts': [
            'basicauth-http-server=basicauth.scripts.server_cli:start_and_wait',
        ],
    },
)
