# $FreeBSD$

PORTNAME=	freenas-migrate93
PORTVERSION=	20191105
PORTREVISION=	9
CATEGORIES=	freenas
VALID_CATEGORIES+=	freenas

MAINTAINER=	dev@ixsystems.com
COMMENT=	Tool to upgrade from 9.X databases

RUN_DEPENDS=	python>0:${PORTSDIR}/lang/python \
		${PYTHON_PKGNAMEPREFIX}south>0:databases/py-south \
		${PYTHON_PKGNAMEPREFIX}bsd>0:freenas/py-bsd \
		${PYTHON_PKGNAMEPREFIX}lxml>0:devel/py-lxml

USES=		python
USE_GITHUB=	yes
GH_TUPLE+=	freenas:freenas-migrate93:cb7ffe6 \
		freenas:django:168674c:django

NO_BUILD=	yes

.include <bsd.port.pre.mk>

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/lib/migrate93
	cd ${WRKSRC} && ${COPYTREE_SHARE} src ${STAGEDIR}${PREFIX}/lib/migrate93/
	cd ${WRKSRC} && ${COPYTREE_SHARE} freenasUI ${STAGEDIR}${PREFIX}/lib/migrate93/
	cd ${WRKSRC_django} && ${COPYTREE_SHARE} django ${STAGEDIR}${PREFIX}/lib/migrate93/
	${INSTALL_SCRIPT} ${WRKSRC}/sbin/migrate93 ${STAGEDIR}${PREFIX}/sbin/
	${PYTHON_CMD} -c "import pathlib; r=pathlib.Path('${STAGEDIR}${PREFIX}/lib/migrate93'); [p.write_text(p.read_text().replace('collections.Iterator','collections.abc.Iterator').replace('collections.Sequence','collections.abc.Sequence').replace('collections.Mapping','collections.abc.Mapping').replace('collections.Callable','collections.abc.Callable')) for p in r.rglob('*.py') if p.is_file()]; p=r/'django/utils/translation/trans_real.py'; p.write_text(p.read_text().replace('self.set_output_charset','# self.set_output_charset'))"
	${PYTHON_CMD} -m compileall -q ${STAGEDIR}${PREFIX}/lib/migrate93 || true
	(cd ${STAGEDIR}${PREFIX}/lib/migrate93; ${FIND} . -type f \
		| ${SED} -e 's,^\./,,g' \
		| ${AWK} '{print length, $$0}' | ${SORT} -rn \
		| ${AWK} '{print "lib/migrate93/"$$2 }' >> ${TMPPLIST})

.include <bsd.port.post.mk>
