from distutils.core import setup
from setuptools import find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='nonebot-plugin-report-manager',  
      version='0.5.0',  
      description='群员通过Bot对话超管',
      author='HauKuen',
      author_email='haukuen@foxmail.com',
      url='https://github.com/HauKuen/nonebot_plugin_report_manager',
      license='MIT License',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',        
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
      ],
      python_requires='>=3.8',
      install_requires=[
        "nonebot2>=2.0.0rc1,<3.0.0",
        "nonebot-adapter-onebot>=2.1.5"
    ]
)