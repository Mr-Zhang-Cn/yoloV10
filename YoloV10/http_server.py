from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import json
import subprocess
import logging
import socket
import signal
import sys
import argparse
import daemon
from daemon import pidfile

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 检查请求路径是否为 /api_ai_model
        if self.path != '/api_ai_model':
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {'status': 'error', 'message': 'Not Found'}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            return

        # 获取Content-Length，读取POST请求的数据
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # 解析JSON数据
        try:
            data = json.loads(post_data)
            url = data.get('url')

            # 检查url是否为图片地址
            if url and (url.endswith('.jpg') or url.endswith('.jpeg') or url.endswith('.png')):
                # 执行 ai_model.py 脚本并获取输出
                logging.info(f"Processing URL: {url}")
                res = subprocess.run(['python', 'ai_model.py', url,'--url'], capture_output=True, text=True, encoding='utf-8')

                # 从 res.stdout 中提取 JSON 部分
                try:
                    # 提取最后一行 JSON 数据
                    output_lines = res.stdout.strip().split('\n')
                    json_output = output_lines[-1]
                    result = json.loads(json_output)

                    if result.get('success'):
                        response = {'url':url,'status': 'havePerson', 'message': '图像处理完成，检测到人物。'}
                        self.send_response(200)
                    else:
                        response = {'url':url,'status': 'notHavePerson', 'message': '图像处理完成，但未检测到人物。'}
                        self.send_response(200)

                except (json.JSONDecodeError, IndexError):
                    response = {'url':url,'status': 'error', 'message': 'JSON数据解析失败.'}
                    self.send_response(200)

            else:
                response = {'url':url,'status': 'error', 'message': '无效的图像URL.'}
                self.send_response(200)

        except json.JSONDecodeError:
            response = {'url':url,'status': 'error', 'message': 'JSON数据无效.'}
            self.send_response(200)

        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def run(server_class=ThreadingHTTPServer, handler_class=MyHandler, port=8000):
    try:
        # 获取主机名
        hostname = socket.gethostname()
        # 获取本机IP地址
        ip_address = socket.gethostbyname(hostname)
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        logging.info(f'Starting httpd server on')
        logging.info(f'http://{ip_address}:{port}/api_ai_model')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('You pressed Ctrl+C!')
        sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description='HTTP Server')
    parser.add_argument('-d', '--daemon', action='store_true', help='Run as a daemon')
    args = parser.parse_args()

    if args.daemon:
        with daemon.DaemonContext(
            working_directory='.',
            umask=0o002,
            pidfile=pidfile.TimeoutPIDLockFile('./tmp/http_server.pid'),
            stdout=open('./tmp/http_server.log', 'w+'),
            stderr=open('./tmp/http_server.err', 'w+'),
            signal_map={
                signal.SIGTERM: signal_handler,
                signal.SIGTSTP: signal_handler
            }
        ):
            run()
    else:
        run()

if __name__ == '__main__':
    main()
