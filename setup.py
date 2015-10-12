from setuptools import setup

setup(name='IUGW_dojson',
      version='0.1',
      description='dojson version for IUGW',
      url='http://github.com/switowsk/IUGW_dojson',
      author='Sebastian Witowski',
      author_email='s.w@cern.ch',
      license='BSD',
      packages=['IUGW_dojson'],
      install_requires=[
            'dojson'
      ],
      zip_safe=False,
      entry_points={
            'dojson.contrib.marc21': [
                  'IUGW_bd9xx = IUGW_dojson.fields.default.bd9xx',
            ],
      },
      )
