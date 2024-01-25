from setuptools import setup, find_packages

setup(
    name='blivedm',
    version='0.1.1',
    description='blivedm fork仓库',
    long_description=open('README.md', encoding='UTF-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xfgryujk/blivedm',
    packages=find_packages(),  # 自动发现并包含所有包和子包
    license='MIT',
    install_requires=[
        'aiohttp',
        'brotli',
    ]
)
