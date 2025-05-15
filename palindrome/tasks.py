from invoke import task


@task
def test_robot(c):
    c.run("robot --xunit robot-report.xml tests/robot/")

@task
def test_pytest(c):
    c.run("pytest --junitxml=pytest-report.xml")

@task(pre=[test_pytest, test_robot])
def test_all(c):
    pass
