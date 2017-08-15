#!/usr/bin/env python
import os, sys, subprocess
import click
import requests
import json
import logging
import contextlib
try:
    from http.client import HTTPConnection # py3
except ImportError:
    from httplib import HTTPConnection # py2

from time import sleep

@click.command()
@click.option('--rancher-url', envvar='RANCHER_URL', required=True,
              help='The URL for your Rancher server, eg: http://rancher:8000')
@click.option('--rancher-key', envvar='RANCHER_ACCESS_KEY', required=True,
              help="The environment or account API key")
@click.option('--rancher-secret', envvar='RANCHER_SECRET_KEY', required=True,
              help="The secret for the access API key")
@click.option('--action', required=True,
              help="Action to do with Rancher Catalogs.")
@click.option('--debug/--no-debug', default=False,
              help="Enable HTTP Debugging")

def main(rancher_url, rancher_key, rancher_secret, action, debug):
    """Performs an in service upgrade of the service specified on the command line"""

    if debug:
        debug_requests_on()

    # split url to protocol and host
    if "://" not in rancher_url:
        bail("The Rancher URL doesn't look right")

    proto, host = rancher_url.split("://")
    api = "%s://%s:%s@%s/v1-catalog" % (proto, rancher_key, rancher_secret, host)
  
    # 1 -> Trigger template refresh
    if action=='refresh':
        try:
            r = requests.get("%s/templates?action=refresh" % api)
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            bail("Unable to connect to Rancher at %s - is the URL and API key right?" % host)
        else:
            response = r.json()['data']
            msg("Upgrade %s finished" % response)
    sys.exit(0)

def msg(msg):
    click.echo(click.style(msg, fg='green'))

def warn(msg):
    click.echo(click.style(msg, fg='yellow'))

def bail(msg):
    click.echo(click.style('Error: ' + msg, fg='red'))
    sys.exit(1)

def debug_requests_on():
    '''Switches on logging of the requests module.'''
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
