from setuptools import setup
from glob import glob
import os

package_name = 'unkothink'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name),glob('launch/*.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Aso Hidetoshi',
    maintainer_email='asouhide2002@gmail.com',
    description='unkothink for ros2',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'sayhello = unkothink.sayhello:main',
          'listen_unko = unkothink.listen_unko:main'
        ],
    },
)
