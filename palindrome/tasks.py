from invoke import task


@task
def test_robot(c):
    print("")
    c.run("robot --xunit robot-report.xml test/")

@task
def test_pytest(c):
    print("")
    c.run("pytest --junitxml=pytest-report.xml")

@task(pre=[test_pytest, test_robot])
def test_all(c):
    print("")
