import smtplib
import os
from dotenv import load_dotenv

load_dotenv()




class EmailManager:
    def __init__(self):
        self.myemail=os.getenv("MYEMAIL")
        self.password=os.getenv("APPPAS")
        self.toemail=os.getenv("TOEMAIL")
        
    def send_email(self,person_name,person_email,person_phone,person_message):
        try:
            with smtplib.SMTP("smtp.gmail.com",587) as connection:
                connection.starttls()
                connection.login(user=self.myemail, password=self.password)
                message=(
                    f"Subject: Someone is trying to contact you\n\n"
                    f"from: {person_name}\n\n"
                    f"email: {person_email}\n\n"
                    f"phone: {person_phone}\n\n"
                    f"message:{person_message}"
                )
                connection.sendmail(to_addrs=self.toemail, from_addr=self.myemail,msg=message)
                final_message="Message sent succesfully"
                return final_message
        except Exception as e:
            final_message=f"Sorry, message couldn't be send {e}"
            return final_message
        