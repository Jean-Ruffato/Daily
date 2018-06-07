from distutils.core import setup

setup(
    name='Daily',
    version='1.0',
    packages=['Base', 'Base.migrations', 'Daily', 'Coordenador', 'Coordenador.migrations', 'Funcionarios',
              'Funcionarios.migrations'],
    url='http://tecjc.com',
    license='GNU',
    author='Jean Ruffato',
    author_email='jean.ruffato@gmail.com',
    description='', requires=['django']
)
