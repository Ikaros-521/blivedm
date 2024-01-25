from setuptools import setup

setup(
    name='blivedm',
    version='0.0.1',
    description='blivedm fork仓库',
    long_description=open('README.md', encoding='UTF-8').read(),
    long_description_content_type='text/markdown',
    #author='-',
    #author_email='-',
    url='https://github.com/xfgryujk/blivedm',
    packages=['blivedm'],
    license='MIT',
    install_requires=[
        'aiohttp',
        'brotli',
    ] 
)