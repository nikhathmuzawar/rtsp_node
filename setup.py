from setuptools import find_packages, setup

package_name = 'rtsp_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bob',
    maintainer_email='nikhath.fatimam@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rtsp_url_publisher = rtsp_node.rtsp_url_publisher:main',
            'rtsp_dummy_publisher = rtsp_node.rtsp_dummy_publisher:main',
        ],
    },
)
