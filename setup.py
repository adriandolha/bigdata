from setuptools import setup

setup(name='big_data',
      version='0.1',
      description='Kafka module',
      url='http://github.com/big-data/kafka',
      author='Adrian Dolha',
      author_email='adrianddolha@yahoo.com',
      license='MIT',
      packages=['big_data_kafka', 'compute_jobs'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['pykafka', 'pyspark', 'faker', 'faker_web'])
