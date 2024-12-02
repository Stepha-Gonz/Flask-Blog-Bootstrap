from tkinter import NO
from flask import Flask, render_template, request
import datetime
import requests
from posts import Post
from email_manager import EmailManager


today=datetime.datetime.now()
year=today.year
blog_url="https://api.npoint.io/673ccc80824705651391"
blog_response=requests.get(blog_url)
blog_data=blog_response.json()
blog_info=[]

for item in blog_data:
    post=Post(item["id"],item["title"],item["subtitle"],item["body"])
    blog_info.append(post)
    



app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",year=year, posts=blog_info)

@app.route("/post/<int:id>")
def show_route(id):
    requested_post=None
    for post in blog_info:
        if post.id==id:
            requested_post=post
    return render_template("post.html", post=requested_post, year=year)

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method=="POST":
        email=EmailManager()
        data = request.form
        final_message=email.send_email(data["name"],data["email"],data["phone"],data["message"])
        return render_template("contact.html",year=year,msg=True,final_message=final_message)
    
    return render_template("contact.html",year=year,msg=False)

    

@app.route("/about")
def about():
    return render_template("about.html", year=year)







if __name__=="__main__":
    app.run(debug=True)

