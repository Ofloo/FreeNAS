PORTNAME=	south
PORTVERSION=	1.0.2
PORTREVISION=	4
CATEGORIES=	databases python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DISTNAME=	South-${PORTVERSION}

MAINTAINER=	wen@FreeBSD.org
COMMENT=	Intelligent schema migrations for Django apps
WWW=		https://south.aeracode.org/

LICENSE=	APACHE20

USES=		python
USE_PYTHON=	distutils autoplist

post-extract:
	@${REINPLACE_CMD} -e "s/inspect.getargspec/inspect.getfullargspec/g" ${WRKSRC}/south/migration/migrators.py

post-install:
	@${REINPLACE_CMD} -e "s/inspect.getargspec/inspect.getfullargspec/g" ${STAGEDIR}${PYTHONPREFIX_SITELIBDIR}/south/migration/migrators.py

.include <bsd.port.mk>
