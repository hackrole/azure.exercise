from invoke import task


@task
def ab(ctx, url="http://localhost:8000/"):
    "run ab test, force 200 requsts 10 concurrency"
    print("you need to have apache ab installed in your host.")
    cmd = f"ab -t 60 -c 10 {url}"
    ctx.run(cmd)


@task
def build(ctx):
    """build docker images, the image name and tags unable to set now."""
    cmd = "docker build -t web ."
    ctx.run(cmd)


@task
def run(ctx):
    """run using docker image in frontend for debug log."""
    cmd = "docker run -p 8000:8000 --name web --rm web"
    ctx.run(cmd)
