import setuptools

setuptools.setup(
    version='201106.1',
    name='atrafainfo',
    author='David S',
    install_requires=[
        'anvil-parser',
        'flask',
        'jinja2'
    ],
    include_package_data=True
)