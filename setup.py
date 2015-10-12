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
            'IUGW_dojson.marc21': [
                  'bd01x09x = IUGW_dojson.fields.default.bd01x09x',
                  'bd2xx = IUGW_dojson.fields.default.bd2xx',
                  'bd5xx = IUGW_dojson.fields.default.bd5xx',
                  'bd69x = IUGW_dojson.fields.default.bd69x',
                  'bd7xx = IUGW_dojson.fields.default.bd7xx',
                  'bd8xx = IUGW_dojson.fields.default.bd8xx',
                  'bd9xx = IUGW_dojson.fields.default.bd9xx',
            ],
      },
      )
