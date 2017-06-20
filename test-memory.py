from ctypes import Structure, c_ulonglong, byref, POINTER, windll, sizeof
from ctypes.wintypes import DWORD, BOOL

DWORDLONG = c_ulonglong

class MEMORYSTATUSEX(Structure):
    _fields_ = [
        ("dwLength", DWORD),
        ("dwMemoryLoad", DWORD),
        ("ullTotalPhys", DWORDLONG),
        ("ullTotalPhys", DWORDLONG),
        ("ullTotalPageFile", DWORDLONG),
        ("ullAvailPageFile", DWORDLONG),
        ("ullTotalVirtual", DWORDLONG),
        ("ullAvailVirtual", DWORDLONG),
        ("ullAvailExtendedVirtual", DWORDLONG),
    ]

status = MEMORYSTATUSEX()
status.dwLength = sizeof(status)

GlobalMemoryStatusEx = windll.kernel32.GlobalMemoryStatusEx
GlobalMemoryStatusEx.argtypes = [POINTER(MEMORYSTATUSEX)]
GlobalMemoryStatusEx.restype = BOOL

assert GlobalMemoryStatusEx(byref(status)) != 0

virtual_memory_gb = status.ullTotalVirtual / 1024. ** 3

print "%f GB" % virtual_memory_gb

assert virtual_memory_gb > 3, "not enough virtual memory"
