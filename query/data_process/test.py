
import hashlib
import tornado.web
import tornado.httpserver
from tornado.options import options,define

define('port', default=8000, help='run on the given port', type=int)
token = 'test'

class WxSignatureHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce = self.get_argument('nonce')
        echostr = self.get_argument('echostr')
        result = self.check_signature(signature, timestamp, nonce)
        if result:
            self.write(echostr)
        else:
            self.write("error")
    def check_signature(self, signature, timestamp, nonce):
        token = 'test'
        L = [timestamp, nonce, token]
        L.sort()
        s = L[0] + L[1] + L[2]
        sha1 = hashlib.sha1(s.encode('utf-8')).hexdigest()
        return sha1 == signature

    def post(self):
        # 获取微信公众平台发送的验证参数
        signature = self.get_argument('signature', '')
        timestamp = self.get_argument('timestamp', '')
        nonce = self.get_argument('nonce', '')
        echostr = self.get_argument('echostr', '')
        # 获取所有值并解析
        msg = parse_message(self.request.body)
        if msg.type == 'text':
            content = msg.content.strip()

            reply = create_reply(content, msg)
            self.write(reply.render())
        else:
            help_str = "目前仅支持文字输入\n"
            reply = create_reply(help_str, msg)
            self.write(reply.render())

def main():
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [
            (r"/wenwu_kgqa",WxSignatureHandler)
        ],debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()