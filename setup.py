from setuptools import setup

setup (
    name='ujs-jsonvalidate',
    version='0.1.0',
    description='JSON validation utility',
    long_description=open('README.rst').read(),
    url='http://github.com/usingjsonschema/ujs-jsonvalidate-python',
    author='Joe McIntyre',
    author_email='j_h_mcintyre@yahoo.com',
    keywords='bookujs json json-schema',
    license='MIT',
    packages=['jsonvalidate'],
    install_requires=['jsonschema', 'ujs-safefile'],
    entry_points={
        'console_scripts':[
            'validate=jsonvalidate.main:main',
            'validatep=jsonvalidate.main:main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development'
    ])
