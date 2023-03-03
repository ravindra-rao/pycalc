import setuptools

#Adding code for packaging
setuptools.setup(
    include_package_data=True, 
    name='pycalc', 
    version='0.0.1', 
    description='pycalc python module',
    url='https://github.com/ravindra-rao/setuptoolsdemo.git',
    author='yobro',
    author_email='contact@yobro.com',
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'pytest'
    ], 
    long_description='pycalc python module',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
)