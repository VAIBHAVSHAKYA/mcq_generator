from distutils.core import setup

setup(name='mcq_gen',
      version='1.0.0',
      description='mcq generator from any text',
      author='mcq_gen',
      author_email='cdac.vaishakya09@gmail.com',
      packages=['main', 'encoding', 'mcq'],
      url="https://github.com/VAIBHAVSHAKYA/mcq_generator",
      install_requires=[
         
           'torch==1.10.0',
           'transformers==3.0.2',
           'sense2vec==2.0.0',
           'strsim==0.0.3',
           'six==1.15.0',
           'networkx==2.6.3',
           'numpy==1.21.5',
           'scipy==1.4.1',
           'scikit-learn==1.0.2',
           'unidecode==1.3.4',
           'future==0.16.0',
           'joblib==1.1.0',
           'pytz==2018.9',
           'python-dateutil==2.8.2',
           'flashtext==2.7',
           'pandas==1.3.5'
      ],
      package_data={['mcq.py', 'main.py', 'encoding.py']}
      )
