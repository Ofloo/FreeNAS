# $FreeBSD$

PORTNAME=	freenas-migrate113
PORTVERSION=	2020000000
PORTREVISION=	19
CATEGORIES=	freenas
VALID_CATEGORIES+=	freenas

MAINTAINER=	dev@ixsystems.com
COMMENT=	Tool to upgrade to 11.3 database

RUN_DEPENDS=	python>0:${PORTSDIR}/lang/python

USES=		python
USE_GITHUB=	yes
GH_ACCOUNT=	freenas
GH_TAGNAME=	72778332bc0f5bf83a9db6039e82244d25f54580

NO_BUILD=	yes

.include <bsd.port.pre.mk>

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/lib/migrate113
	cd ${WRKSRC} && ${COPYTREE_SHARE} django ${STAGEDIR}${PREFIX}/lib/migrate113/
	cd ${WRKSRC} && ${COPYTREE_SHARE} freenasUI ${STAGEDIR}${PREFIX}/lib/migrate113/
	cd ${WRKSRC} && ${COPYTREE_SHARE} src ${STAGEDIR}${PREFIX}/lib/migrate113/
	${INSTALL_SCRIPT} ${WRKSRC}/sbin/migrate113 ${STAGEDIR}${PREFIX}/sbin/
	find ${STAGEDIR}${PREFIX}/lib/migrate113 -name "*.py" -exec sed -i "" -e "/set_output_charset/d" -e "/codeset=/d" -e "s/from collections import Counter, Iterator, Mapping, OrderedDict/from collections import Counter, OrderedDict; from collections.abc import Iterator, Mapping/g" -e "s/collections.Iterator/collections.abc.Iterator/g" -e "s/collections.Mapping/collections.abc.Mapping/g" -e "s/collections.Sequence/collections.abc.Sequence/g" -e "s/collections.Callable/collections.abc.Callable/g" -e "s/collections.Iterable/collections.abc.Iterable/g" {} +
	${PYTHON_CMD} -m compileall -q ${STAGEDIR}${PREFIX}/lib/migrate113 || true
	(cd ${STAGEDIR}${PREFIX}/lib/migrate113; ${FIND} . -type f \
		| ${SED} -e 's,^\./,,g' \
		| ${AWK} '{print length, $$0}' | ${SORT} -rn \
		| ${AWK} '{print "lib/migrate113/"$$2 }' >> ${TMPPLIST})

.include <bsd.port.post.mk>
