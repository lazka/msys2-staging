_realname=pypy
pkgbase=mingw-w64-${_realname}
pkgname=("${MINGW_PACKAGE_PREFIX}-${_realname}")
pkgver=5.7.1
pkgrel=1
pkgdesc="A Python implementation written in Python, JIT enabled (mingw-w64)"
arch=('i686')
url="http://pypy.org"
options=(!buildflags)
license=('custom:MIT')
source=("${_realname}-${pkgver}.tar.bz2::https://bitbucket.org/pypy/pypy/downloads/pypy2-v${pkgver}-src.tar.bz2"
        "fix-build.patch"
        "4g_patch.py"
        "test-memory.py")
sha256sums=('SKIP' 'SKIP' 'SKIP' 'SKIP')

prepare() {
  cd $srcdir/${_realname}2-v${pkgver}-src

  patch -p2 -i "${srcdir}/fix-build.patch"

  # Make a copy of python2.exe and patch it to support 4GB virtual memory
  cp $(which python2.exe) "${srcdir}"
  python2 "${srcdir}/4g_patch.py" "${srcdir}/python2.exe"
  # This checks if we really got 4GB now
  PYTHONHOME=$(cygpath -am ${MINGW_PREFIX}) "${srcdir}/python2.exe" "${srcdir}/test-memory.py"
}

build() {
  cd "$srcdir"/${_realname}2-v${pkgver}-src/pypy/goal

  PYTHONHOME=$(cygpath -am ${MINGW_PREFIX}) \
    PYPY_LOCALBASE=$(cygpath -am ${MINGW_PREFIX}) \
    CC=gcc \
    "${srcdir}/python2.exe" -u ../../rpython/bin/rpython -O2 --shared targetpypystandalone --no-allworkingmodules
}

check() {
  cd "${srcdir}"/build-${CARCH}
  make check
}

package() {
  cd "${srcdir}"/build-${CARCH}
  make install DESTDIR="${pkgdir}"
}
