from flask import Flask, render_template

app = Flask(__name__)

# Sample resume data
resume_data = {
    "personal_info": {
        "name": "Kushal K",
        "email": "kushalkantharaju536@gmail.com",
        "phone": "9741692290",
        "address": " #11 Kodikaleshwara nilaya, 1st main 1st cross, Shantinagar, Acharya College Road, Bangalore 560090",
    },
    "skills": [
        {"name": "Python", "cert_image": "images/python_cert.jpg"},
        {"name": "C and C++", "cert_image": "images/flask_cert.jpg"},
        {"name": "Web Development", "cert_image": "certificate.jpg"},
        {"name": "Machine Learning", "cert_image": "images/css_cert.jpg"},
        {"name": "Data Analysis", "cert_image": "images/data_analysis_cert.jpg"},
        {"name": "JavaScript", "cert_image": "images/javascript_cert.jpg"},
    ],
    "positions_responsibilities": [  # Changed key for simplicity
        {"position": "Coordinator & Founding Member", "description": "DACS (Data and Code Society)"},
        {"position": "captain ", "description": "Badminton"},
        {"position":"cordinator","description":"IEEE"},
    ],
    "extracurricular": [
        "Represented VTU University at National-Level Inter-University Competition",
        "Founding member of DACS (Data and Code Society)",
        "Organized hackathons and coding bootcamps in DACS",
        "Participated in debate competitions and secured prizes",
        "Volunteered at a local NGO teaching programming to kids",
        "Participated in inter-college hackathons",
        "Participated in IEEE conferences",
    ],
}

@app.route("/")
def home():
    # Render the template and pass resume data
    return render_template("index.html", resume=resume_data)

if __name__ == "__main__":
    app.run(debug=True)
