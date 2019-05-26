from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='hfexcel',
      version='0.0.2',
      description='human friendly excel creation in python',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Text Processing :: Linguistic',
         'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='xlsxwriter xlsx excel json writing python wrapper',
      url='https://github.com/ebsaral/hfexcel',
      author='Emin Bugra Saral',
      author_email='eminbugrasaral@me.com',
      license='BSD',
      packages=['hfexcel'],
      install_requires=[
          'xlsxwriter',
      ],
      include_package_data=True,
      zip_safe=False,
      project_urls={
        'Documentation': 'https://github.com/ebsaral/hfexcel',
        'Funding': 'https://github.com/ebsaral/hfexcel',
        'Source': 'https://github.com/ebsaral/hfexcel',
      }
)