from flask import Flask, render_template,request
import new



app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
    if request.method == "POST":
        movie_name = request.form["movie_name"]
        movie_recommend =new.recommender(movie_name)
        m = movie_recommend


    return render_template('index.html', my_movie = m)




# @app.route("/sub", methods=['POST'])
# def submit():
#     if request.method == "POST":
#         name= request.form["username"]

#     return render_template("sub.html", n = name)

if __name__ == "__main__":
    app.run()