#!/usr/bin/env python3
import os, sys

# Set environment
os.environ["BUILD_CONFIG"] = "/home/opencode/truenas-dev/core-build/build/config"
os.environ['PROFILE'] = 'freenas'
os.environ['PROFILE_ROOT'] = '/home/opencode/truenas-dev/core-build/build/profiles/freenas'
os.environ['BE_ROOT'] = '/home/opencode/truenas-dev/core-build/freenas/_BE'
os.environ['BUILD_ROOT'] = '/home/opencode/truenas-dev/core-build'
os.environ['FREENAS_ROOT'] = '/home/opencode/truenas-dev/core-build/freenas/_BE/freenas'
os.environ["OBJDIR"] = "/home/opencode/truenas-dev/core-build/freenas/_BE/objs"
os.environ["JAIL_DESTDIR"] = "/home/opencode/truenas-dev/core-build/freenas/_BE/objs/jail"
os.environ["WORLD_DESTDIR"] = "/home/opencode/truenas-dev/core-build/freenas/_BE/objs/world"
os.environ["PACKAGES_DESTDIR"] = "/home/opencode/truenas-dev/core-build/freenas/_BE/objs/packages"
os.environ["INSTUFS_DESTDIR"] = "/home/opencode/truenas-dev/core-build/freenas/_BE/objs/instufs"
os.environ["ISO_DESTDIR"] = "/home/opencode/truenas-dev/core-build/freenas/_BE/objs/iso"
os.environ["PORTS_OVERLAY"] = "/home/opencode/truenas-dev/core-build/freenas/_BE/objs/ports-overlay"
os.environ["POUDRIERE_ROOT"] = "/home/opencode/truenas-dev/core-build/freenas/_BE/objs/poudriere"
os.environ["DISTFILES_CACHE"] = "/home/opencode/truenas-dev/core-build/freenas/_BE/objs/ports/distfiles"
os.environ["PORTS_ROOT"] = "/home/opencode/truenas-dev/core-build/freenas/_BE/ports"
os.environ["BUILD_ARCH"] = "amd64"
os.environ["BUILD_ARCH_SHORT"] = "x64"
os.environ["FREEBSD_RELEASE_VERSION"] = "15.1-RELEASE"
os.environ['KERNCONF'] = 'TRUENAS'
os.environ['OS_ROOT'] = '/home/opencode/truenas-dev/core-build/freenas/_BE/os'
os.environ['PYTHONPATH'] = '/home/opencode/truenas-dev/core-build/build/lib'

build_lib = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'lib')
sys.path.insert(0, build_lib)

from utils import e, info, error, setup_env

def main():
    setup_env()
    os.execlp(sys.argv[1], *sys.argv[1:])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        error('Usage: buildenv.py <prog> <args...>')
    main()
