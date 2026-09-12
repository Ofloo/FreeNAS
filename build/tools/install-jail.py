#!/usr/bin/env python3
import os, sys
build_lib = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'lib')
sys.path.insert(0, build_lib)
#+
# Copyright 2015 iXsystems, Inc.
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
#####################################################################

import os
import sys
from utils import sh, e, objdir, info, import_function


installworldlog = objdir('logs/jail-installworld')
distributionlog = objdir('logs/jail-distribution')
installkernellog = objdir('logs/jail-installkernel')
installworld = import_function('build-os', 'installworld')
installkernel = import_function('build-os', 'installkernel')


if __name__ == '__main__':
    if e('${SKIP_INSTALL_JAIL}'):
        info('Skipping jail installation, as instructed by setting SKIP_INSTALL_JAIL')
        sys.exit(0)

    if os.path.isdir(e('${JAIL_DESTDIR}')) and os.path.exists(e('${JAIL_DESTDIR}/bin/sh')):
        info('Jail already exists, skipping rebuild')
        sys.exit(0)

    if os.path.isdir(e('${JAIL_DESTDIR}')):
        sh('jail -r ja-p', nofail=True)
        sh('jail -r ja-p-n', nofail=True)
        sh('jail -r ja-p-job-01', nofail=True)
        sh('jail -r ja-p-job-01-n', nofail=True)
        sh('jail -r ja-p-job-02', nofail=True)
        sh('jail -r ja-p-job-02-n', nofail=True)
        sh('jail -r ja-p-job-03', nofail=True)
        sh('jail -r ja-p-job-03-n', nofail=True)
        sh('jail -r ja-p-job-04', nofail=True)
        sh('jail -r ja-p-job-04-n', nofail=True)
        sh('jail -r ja-p-job-05', nofail=True)
        sh('jail -r ja-p-job-05-n', nofail=True)
        sh('umount -f ${JAIL_DESTDIR}/usr/src', nofail=True)
        sh('chflags -fR 0 ${JAIL_DESTDIR}/*', nofail=True)
        sh('rm -rf ${JAIL_DESTDIR}/*')

    if e('${USE_ZFS}'):
        if not os.path.ismount(e('${JAIL_DESTDIR}')):
            sh('zfs create -o mountpoint=${JAIL_DESTDIR} ${ZPOOL}${ZROOTFS}/jail')

    sh('mkdir -p ${JAIL_DESTDIR}')
    installworld(e('${JAIL_DESTDIR}'), installworldlog, distributionlog, conf="jail")
