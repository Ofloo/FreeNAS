<p align="center">
 <a href="https://discord.gg/Q3St5fPETd"><img alt="Join Discord" src="https://badgen.net/discord/members/Q3St5fPETd/?icon=discord&label=Join%20the%20TrueNAS%20Community" /></a>
 <a href="https://www.truenas.com/community/"><img alt="Join Forums" src="https://badgen.net/badge/Forums/Post%20Now//purple" /></a> 
 <a href="https://jira.ixsystems.com"><img alt="File Issue" src="https://badgen.net/badge/Jira/File%20Issue//red?icon=jira" /></a>
</p>

# Building TrueNAS 13 CORE/Enterprise from Scratch

Note: All these commands must be run as `root`.


## Requirements:

* Hardware

  * CPU: amd64-compatible 64-bit Intel or AMD CPU.
  * 16GB memory, or the equivalent in memory plus swap space
  * at least 80GB of free disk space

* Operating System

  * The build environment must be FreeBSD 13.x (or 13-STABLE)


## Make Targets

* ```checkout``` creates a local working copy of the git repositories with
  ```git clone```

* ```update``` does a ```git pull``` to update the local working copy with
  any changes made to the git repositories since the last update

* ```release``` actually builds the FreeNAS release

* ```clean``` removes previously built files


## Procedure

* Install git
    ```
    pkg install -y git
    rehash
    ```

* Clone the build repository (```/usr/build``` is used for this example):

    ```
    git clone https://github.com/truenas/build /usr/build
    ```

* Install Dependencies

    ```
    cd /usr/build
    make bootstrap-pkgs
    python3 -m ensurepip
    pip3 install six
    ```


* First-time checkout of source:

    ```
    make checkout
    ```


A FreeNAS release is built by first updating the source, then building:

```
make update
make release
```

To build the SDK version:

```
make update
make release BUILD_SDK=yes
```


Clean builds take a while, not just due to operating system builds, but
because poudriere has to build all of the ports. Later builds are faster,
only rebuilding files that need it.

Use ```make clean``` to remove all built files.


## Results

Built files are in the ```freenas/_BE``` subdirectory,
```/usr/build/freenas/_BE``` in this example.

ISO files: ```freenas/_BE/release/TrueNAS-13-MASTER-{date}/x64/```.

Update files: ```freenas/_BE/release/```.

Log files: ```freenas/_BE/objs/logs/```.

## FreeBSD 15.1 Porting Notes

The Poudriere package environment is configured in `build/profiles/freenas/config.pyd` through `make_conf_pkg`. Keep the Python toolchain pinned with:

```
DEFAULT_VERSIONS=python=3.11 python3=3.11 ssl=base
```

This configuration is written to the Poudriere jail's `/etc/make.conf`; changing the build host's `/etc/make.conf` is not sufficient for the package jail.

`py-middlewared` requires SQLAlchemy 1.4. The `databases/py-alembic` entry in `build/profiles/freenas/ports-freenas.pyd` therefore explicitly enables `SQLALCHEMY14` and disables `SQLALCHEMY20`. These are Poudriere port options and must be defined in the profile so `build/tools/build-ports.py` recreates them on every release build.
The FreeBSD 15 port requires `limits.h` in `freenas/src/winacl/winacl.c` for `PATH_MAX`; this compatibility include is part of the source tree used by the `freenas-files` port.
The FreeBSD 15 ports tree moved `fusefs-ntfs` to `filesystems/ntfs`, `fusefs-s3fs` to `filesystems/s3fs`, and `netatalk3` to `netatalk4`; `build/profiles/freenas/ports-system.pyd` uses the current origins.
Fixed `net/netatalk4` PAM stage install by moving the sample PAM configuration installation from `post-patch` to `post-install-PAM-on` with directory creation.
Added Python 3.11 compatibility substitutions for legacy migration Django imports and the middleware client (`collections.abc` for Iterator, Mapping, Callable).
Bumped migration and middleware port revisions so Python 3.11 compatibility patches are rebuilt instead of reused from the package cache.
Updated `freenas-migrate93` and `freenas-migrate113` Makefiles with Python one-liners during staging to reliably patch `collections.abc` compatibility without BSD sed multiline syntax errors.
Restored the expired py-ws4py dependency and patched remaining Python 3.11 legacy Django compatibility issues.
Added `freenas/py-ws4py` to the system profile and patched legacy Django translation and paginator compatibility for Python 3.11.
Fixed `freenas/py-ws4py` categories to start with `freenas` and added `VALID_CATEGORIES+=freenas`.
Cleaned up quoting in `freenas-migrate93` and `freenas-migrate113` Makefiles for `trans_real.py` and `paginator.py` staging adjustments.
