import sys

# This just mirrors the changes done by editbin.exe, I don't know
# how robust that is, but we check if it worked later anyway.
with open(sys.argv[1], "rb+") as h:
    h.seek(150)
    h.write(b"\x2f")
    h.seek(216)
    h.write(b"\x41")
