from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name='py_compiler',
    version='0.0.1',
    author='Kim Yongbeom',
    author_email='yongbeom.kim@u.nus.edu',
    license='<the license you chose>',
    description='Wrapper around the python compileall utility.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='<github url where the tool code will remain>',
    py_modules=['py_compiler', 'app'],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        py_compile=py_compiler:cli
    '''
)