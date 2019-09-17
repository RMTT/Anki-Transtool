from setuptools import setup, find_packages

print(find_packages())
setup(
    name="transtool",
    version="0.0.1",
    author="",
    author_email="",
    description=(""),
    license="GPLv3",
    keywords="",
    url="",
    packages=find_packages(),

    # 需要安装的依赖
    install_requires=[
        'requests',
        'googletrans',
        'jinja2'
    ],
    package_data={'': ["back.md","front.md"]},
    include_package_data=True,
    entry_points={'console_scripts': [
        'anki-transtool = transtool.main:run',
    ]},
)
