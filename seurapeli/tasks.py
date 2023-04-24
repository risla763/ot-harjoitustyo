from invoke import task


@task
def start(ctx):
<<<<<<< HEAD
    ctx.run("python3 main_game_loop.py", pty=True)
=======
    ctx.run("python3 src/main_game_loop.py", pty=True)
>>>>>>> 093557e4de1e334ef8962ed261454bd8c753cfcc


@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest src", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
<<<<<<< HEAD


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
=======
    
@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)
>>>>>>> 093557e4de1e334ef8962ed261454bd8c753cfcc
