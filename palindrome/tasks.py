from invoke import task


@task
def test_robot(c):
    c.run("robot --xunit junit-robot.xml tests/robot/")

@task
def test_pytest(c):
    c.run("pytest --junitxml=junit-pytest.xml")

@task(pre=[test_pytest, test_robot])
def test_all(c):
    pass
