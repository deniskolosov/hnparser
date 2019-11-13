from celery import task


@task(name='Fetch HN frontpage')
def fetch_page():
    pass
