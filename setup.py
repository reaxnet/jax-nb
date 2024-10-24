from setuptools import setup, find_packages

setup(name='jax-nb',
      version="0.0.1",
      install_requires=[
   'jax-md>=0.2.8',
   'jax>=0.4.20'
],
      author='Rongzhi Gao',
      packages=find_packages(),
      package_data={
        '':['dftd3_params.npz'],
           },
)
