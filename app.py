from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app)  


EMAIL_ADDRESS = "kumarsaivaibhav4@gmail.com" 
EMAIL_PASSWORD = "vbyy zfdl ckyj bsut"  

@app.route("/") 
def index():
    return render_template("index.html")  

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.json
    first_name = data.get("firstName")
    last_name = data.get("lastName")
    user_email = data.get("email")
    user_message = data.get("message")

    try:
      
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = user_email
        msg["Subject"] = "We’re Excited to Help You With Your Service Requirements!"

      
        body = f"""
       Dear {first_name} {last_name},

        Thank you for reaching out to us! We have received your message below:

        ---------------------------------
        {user_message}
        ---------------------------------

        Thank you for reaching out to us. We are thrilled to assist you with your upcoming project! To ensure that we understand your specific needs and can offer the most tailored services for you, we kindly ask you to fill out our service requirements form.

Please provide the details about your project by clicking on the link below:

Fill Out the Service Requirements Form CLICK ON LINK : https://forms.gle/rW1M9mCrKzPWRtQ59

The form covers the following services:

Digital Marketing
Web Development
Cloud Hosting
And more
Your responses will help us better understand your vision, timeline, and budget, allowing us to propose the perfect solution for your business.

If you have any questions or need assistance, feel free to reach out to us directly. We look forward to collaborating with you and bringing your project to life!

Best regards,
        Your Kumar sai vaibhav
        """

        msg.attach(MIMEText(body, "plain"))

        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, user_email, msg.as_string())
        server.quit()

        return jsonify({"message": "Email sent successfully!"}), 200

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
