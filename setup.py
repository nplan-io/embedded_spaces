from setuptools import setup
from setuptools import find_packages

setup(name='embedded_spaces',
      version='0.0.5.2',
      description='word2vec and doc2vec based on Kearas and gensim',
      author='nPlan',
      author_email='hello@nplan.io',
      url='https://github.com/nplan-io/embedded_spaces',
      license='GNU Affero General Public License, version 3 - http://www.gnu.org/licenses/agpl-3.0.html',
      install_requires=['gensim', 'theano', 'pyyaml', 'six', 'keras<=0.3.1'],
      #install_requires=['gensim', 'theano', 'pyyaml', 'six', 'keras', 'sklearn'],
      # extras_require={
      #     'h5py': ['h5py'],
      # },
      packages=find_packages(),
      test_suite = 'test'
      )
