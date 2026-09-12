# Created by: William Grzybowski <wg@FreeBSD.org>
# $FreeBSD: head/net/py-netif/Makefile 412348 2016-04-01 14:16:16Z mat $

PORTNAME=	netif
PORTVERSION=	1.0
PORTREVISION=	7
CATEGORIES=	net python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	wg@FreeBSD.org
COMMENT=	Python network configuration library for FreeBSD

LICENSE=	BSD2CLAUSE

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}cython>0:lang/cython@${PY_FLAVOR}

USE_GITHUB=	yes
GH_ACCOUNT=	truenas
GH_PROJECT=	py-netif
GH_TAGNAME=	9298aa968e24c423caa35d2ea4f960d487f1bf10

USES=		python
USE_PYTHON=	autoplist distutils

post-extract:
	@${REINPLACE_CMD} -e "s/ifbc.ifbic_len \/ cython.sizeof(defs.ifbreq)/ifbc.ifbic_len \/\/ cython.sizeof(defs.ifbreq)/" ${WRKSRC}/netif.pyx
	@${CP} ${FILESDIR}/config.pxi ${WRKSRC}/config.pxi
	@${CP} ${FILESDIR}/config.h ${WRKSRC}/config.h

.include <bsd.port.mk>
