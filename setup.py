#!/usr/bin/env python

from setuptools import setup, find_packages

name = "indiccallendar"

setup(
    name=name,
    version="0.1",
    license="LGPL-3.0",
    author="Santhosh Thottingal",
    description="callendar conversion library supporting indic callendar systems",
    long_description=""" a callendar conversion library supporting indic
    callendar systems """,
    author_email="santhosh.thottingal@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['setuptools-git'],
    install_requires=['setuptools'],
    zip_safe=False,
)
