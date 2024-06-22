from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from test_model import Person  # test_model.py内でPersonモデルが定義されていると仮定

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# ファイルのダウンロードと配置後に以下の関数を追加する
@app.route("/person_search")
def person_search():
    return render_template("person_search.html")


@app.route("/person_result")
def person_result():
    search_size = request.args.get("search_size")
    persons = db.session.query(Person).filter(Person.size > search_size)
    return render_template(
        "./person_result.html", persons=persons, search_size=search_size
    )


# SQLAlchemyのモデルを定義（humanテーブルの定義と同じものを想定）
class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)

    def __repr__(self):
        return f"<Human {self.id}: {self.name}, {self.height}cm, {self.weight}kg>"
