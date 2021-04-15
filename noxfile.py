import nox


@nox.session
def lint(session):
    targets = ['pfinance', 'tests', 'noxfile.py']
    session.install('flake8')
    session.run('flake8', *targets)


@nox.session
def tests(session):
    session.install('pytest')
    session.run('pytest', '-v')
