from aiosmtpd.controller import Controller

class DebuggingHandler:
    async def handle_DATA(self, server, session, envelope):
        print('Message from:', envelope.mail_from)
        print('Message to:', envelope.rcpt_tos)
        print('Message data:\n', envelope.content.decode('utf8', errors='replace'))
        print('End of message\n')
        return '250 Message accepted for delivery'

controller = Controller(DebuggingHandler(), hostname='localhost', port=1025)
controller.start()

input('SMTP server running. Press Enter to stop.\n')
controller.stop()
