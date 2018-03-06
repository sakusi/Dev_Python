# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate

FROM_ADDR = "送信元メールアドレス"
# テスト用
TO_ADDR = ['宛先メールアドレス']

BCC_ADDR = ['BCC先メールアドレス']
ENCODING = "iso-2022-jp"


def main():

    mail_body = "メールだよ"

    message = MIMEText(
        mail_body.encode(ENCODING),
        "plain",
        ENCODING,
    )

    message["Subject"] = str(Header(u"テストメール",ENCODING))
    message["From"] = "%s <%s>" %(str(Header(u"From",ENCODING)),FROM_ADDR)
    #message["To"] = "%s <%s>" %(str(Header(u"To",ENCODING)),TO_ADDR)
    message["To"] = ",".join(TO_ADDR)
    message['Bcc'] = ",".join(BCC_ADDR)
    message["Date"] = formatdate()

    s = smtplib.SMTP("SMTPメールサーバー", 25)
    s.ehlo()
    s.login("送信元メールアカウント", "パスワード")

    try:
        s.sendmail(
            FROM_ADDR,
            TO_ADDR + BCC_ADDR,
            message.as_string(),
            )
        s.close()

        print("Successfully sent email")
    except Exception:
        print("Error: unable to send email")

if __name__ == '__main__':
    main()
