import smtplib
import ssl


smtp_port=587
smtp_server="smtp.gmail.com"

email_from="fajrjauharkk@gmail.com"
email_to="celestialfaju@gmail.com"


pswd='irpoqsecsnsodsut'


message="Hello This is the first email automation test"


simple_email_context=ssl.create_default_context()


try:
    print("Connecting to server")
    TIE_server=smtplib.SMTP(smtp_server,smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from,pswd)
    print("connected to server")


    print()
    print(f"sending email to -{email_to}")
    TIE_server.sendmail(email_from,email_to,message)
    print(f"email successfully sen to -{email_to}")


except Exception as e:
    print(e)
finally:
    TIE_server.quit()
