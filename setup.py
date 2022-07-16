import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

version = '0.1.4'

setuptools.setup(
    name='tictectoc',
    version=version,
    url='https://github.com/nemodleo/tictectoc',
    author='Hyun Park',
    author_email='nemod.leo@snu.ac.kr',
    license="MIT",
    description='Tic Tec Toc timing for Python',
    keywords="tic tec toc tictoc tictectoc time timing",
    long_description=long_description,
    long_description_content_type='text/markdown', 
    python_requires=">= 3.6",
    packages=['tictectoc'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    package_data={},
    classifiers=[
        'License :: OSI Approved :: MIT License'
    ] 
)