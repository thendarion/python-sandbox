from invoke import task


@task
def test_robot(c):
    c.run("robot tests/robot/")

@task
def test_pytest(c):
    c.run("pytest")

@task(pre=[test_pytest, test_robot])
def test_all(c):
    pass
