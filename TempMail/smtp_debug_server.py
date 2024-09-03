from aiosmtpd.controller import Controller
import os

EMAIL_LOG_FILE = 'emails.log'

class DebuggingHandler:
    async def handle_DATA(self, server, session, envelope):
        email_content = (
            f"From: {envelope.mail_from}\n"
            f"To: {', '.join(envelope.rcpt_tos)}\n"
            f"Message data:\n{envelope.content.decode('utf8', errors='replace')}\n"
            "End of message\n\n"
        )

        # Save email content to file
        with open(EMAIL_LOG_FILE, 'a') as f:
            f.write(email_content)

        print(email_content)
        return '250 Message accepted for delivery'

controller = Controller(DebuggingHandler(), hostname='localhost', port=1025)
controller.start()

input('SMTP server running. Press Enter to stop.\n')
controller.stop()
