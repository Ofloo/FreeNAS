# Created by: Vladimir Vinogradenko <vladimirv@ixsystems.com
# $FreeBSD$

PORTNAME=	onedrivesdk
PORTVERSION=	1.1.8
PORTREVISION=	1
CATEGORIES=	devel python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Official Python OneDrive SDK for interfacing with OneDrive APIs

USES=		python zip
USE_PYTHON=	distutils autoplist

post-install:
	@${PYTHON_CMD} -c "import pathlib; p=pathlib.Path('${STAGEDIR}${PYTHON_SITELIBDIR}/onedrivesdk/__init__.py'); s=p.read_text(); s='import types\nif not hasattr(__import__(\"asyncio\"), \"coroutine\"):\n    import asyncio\n    asyncio.coroutine = types.coroutine\n' + s; p.write_text(s)"

.include <bsd.port.mk>
