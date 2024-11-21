from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, e.g., 'requests>=2.25.1'
    ],
    entry_points={
        # 'console_scripts': [
        #     'command_name=module:function',
        # ],
    },
    author='eagle',
    author_email='eagle@42.fr',
    description='A sample test package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/eagle/ft_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT',
)

