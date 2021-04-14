import base64

import click

from basicauth.server import SimpleHTTPAuthHandler, serve


@click.command()
@click.argument("port", type=int)
@click.argument("key", type=str)
@click.option("-d", "--directory", help="Path to directory to serve")
def start_and_wait(port, key, directory):
    """ Start a simple http server with basic auth.

        \b
        PORT to start the server
        KEY to check for in format 'username:password'
    """
    SimpleHTTPAuthHandler.KEY = base64.b64encode(key.encode("utf-8")).decode("utf-8")
    serve(port, start_dir=directory, handler_class=SimpleHTTPAuthHandler)


if __name__ == '__main__':
    start_and_wait()
