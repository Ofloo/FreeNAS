#!/usr/bin/env python3
import os, sys
build_lib = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'lib')
sys.path.insert(0, build_lib)

# Set environment if not set
if not os.environ.get('BUILD_CONFIG'):
    os.environ['BUILD_CONFIG'] = '/home/opencode/truenas-dev/core-build/build/profiles/freenas'
if not os.environ.get('PROFILE'):
    os.environ['PROFILE'] = 'freenas'
if not os.environ.get('PROFILE_ROOT'):
    os.environ['PROFILE_ROOT'] = '/home/opencode/truenas-dev/core-build/build/profiles/freenas'
if not os.environ.get('BE_ROOT'):
    os.environ['BE_ROOT'] = '/home/opencode/truenas-dev/core-build/freenas/_BE'
if not os.environ.get('BUILD_ROOT'):
    os.environ['BUILD_ROOT'] = '/home/opencode/truenas-dev/core-build'

from dsl import load_profile_config
from utils import info, debug, error, e

config = load_profile_config()


def check_sandbox():
    if not os.path.exists(e('${BE_ROOT}/.pulled')):
        error('Sandbox is not fully checked out')

    checkout_only = e('${CHECKOUT_ONLY}')
    if checkout_only:
            checkout_only = checkout_only.split(',')
    for i in config['repos']:
        if checkout_only and i['name'] not in checkout_only:
            continue
        if not os.path.isdir(os.path.join(e('${BE_ROOT}'), i['path'], '.git')):
            error('Sandbox is not fully checked out, {0} is missing', i['name'])

    info('Sandbox is fully checked out')


if __name__ == '__main__':
    debug('Checking sandbox')
    check_sandbox()
