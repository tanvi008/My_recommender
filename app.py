from flask import Flask, render_template,request
import new as n

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
    if request.method == "POST":
        movie_name = request.form["movie_name"]
        movie_recommend =n.recommender(movie_name)
        mr = movie_recommend
        dff = mr.to_html()
        text_file = open("sunny.html", "w")
        text_file.write(dff)
        text_file.close()
        return render_template('sunny.html', my_movie = dff)
    return render_template("index.html")


if __name__ == "__main__":
    app.run()