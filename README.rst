Various WIP MSYS2 packages.

mingw-w64-pypy:
    With the included patches it makes it through translations but 
    fails at compilation right now. I've given up on this for now...

mingw-w64-glib-openssl:
    Builds fine, when installed TLS fails with
    g-tls-error-quark: Unacceptable TLS certificate (2)
