# # # from flask import Flask, render_template, redirect, url_for, request, flash
# # # from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# # # from werkzeug.security import generate_password_hash, check_password_hash
# # #
# # # app = Flask(__name__)
# # # app.secret_key = "supersecretkey"
# # #
# # # # Cấu hình Flask-Login
# # # login_manager = LoginManager()
# # # login_manager.init_app(app)
# # # login_manager.login_view = "login"
# # #
# # # # Danh sách người dùng giả lập (có thể lưu vào CSDL sau này)
# # # users = {
# # #     "admin": {"password": generate_password_hash("123456")}
# # # }
# # #
# # # # Định nghĩa User Model
# # # class User(UserMixin):
# # #     def __init__(self, username):
# # #         self.id = username
# # #
# # # @login_manager.user_loader
# # # def load_user(user_id):
# # #     if user_id in users:
# # #         return User(user_id)
# # #     return None
# # #
# # # # Route trang đăng nhập
# # # @app.route("/login", methods=["GET", "POST"])
# # # def login():
# # #     if request.method == "POST":
# # #         username = request.form["username"]
# # #         password = request.form["password"]
# # #
# # #         if username in users and check_password_hash(users[username]["password"], password):
# # #             user = User(username)
# # #             login_user(user)
# # #             flash("Đăng nhập thành công!", "success")
# # #             return redirect(url_for("dashboard"))
# # #         else:
# # #             flash("Sai tài khoản hoặc mật khẩu", "danger")
# # #
# # #     return render_template("login.html")
# # #
# # # # Route trang sau khi đăng nhập
# # # @app.route("/dashboard")
# # # @login_required
# # # def dashboard():
# # #     return render_template("dashboard.html", username=current_user.id)
# # #
# # # # Route đăng xuất
# # # @app.route("/logout")
# # # @login_required
# # # def logout():
# # #     logout_user()
# # #     flash("Bạn đã đăng xuất!", "info")
# # #     return redirect(url_for("login"))
# # #
# # # # Trang chủ
# # # @app.route("/")
# # # def index():
# # #     return render_template("index.html")
# # #
# # # if __name__ == "__main__":
# # #     app.run(debug=True)
# #
# #
# # from flask import Flask, render_template, redirect, url_for, request, flash
# # from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# # from werkzeug.security import generate_password_hash, check_password_hash
# #
# # app = Flask(__name__)
# # app.secret_key = "supersecretkey"
# #
# # # Cấu hình Flask-Login
# # login_manager = LoginManager()
# # login_manager.init_app(app)
# # login_manager.login_view = "login"
# #
# # # Danh sách người dùng giả lập
# # users = {
# #     "admin": {"password": generate_password_hash("123456")}
# # }
# #
# # # Định nghĩa User Model
# # class User(UserMixin):
# #     def __init__(self, username):
# #         self.id = username
# #
# # @login_manager.user_loader
# # def load_user(user_id):
# #     if user_id in users:
# #         return User(user_id)
# #     return None
# #
# # # Route đăng nhập
# # @app.route("/login", methods=["GET", "POST"])
# # def login():
# #     if request.method == "POST":
# #         username = request.form["username"]
# #         password = request.form["password"]
# #
# #         if username in users and check_password_hash(users[username]["password"], password):
# #             user = User(username)
# #             login_user(user)
# #             flash("Đăng nhập thành công!", "success")
# #             return redirect(url_for("index"))  # Chuyển đến index.html
# #         else:
# #             flash("Sai tài khoản hoặc mật khẩu", "danger")
# #
# #     return render_template("login.html")
# #
# # # Route đăng xuất
# # @app.route("/logout")
# # @login_required
# # def logout():
# #     logout_user()
# #     flash("Bạn đã đăng xuất!", "info")
# #     return redirect(url_for("login"))
# #
# # # Trang chủ
# # @app.route("/")
# # # @login_required
# # def index():
# #     return render_template("index.html", user=current_user if current_user.is_authenticated else None)
# #
# # if __name__ == "__main__":
# #     app.run(debug=True)
# from flask import Flask, request, render_template, redirect, url_for, session
# import os
# import cv2
# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.image import load_img
#
# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'  # Thay đổi chuỗi này trong thực tế để bảo mật
#
# # Load model
# model = load_model("brain_tumor_model.h5")
# categories = ["glioma", "meningioma", "notumor", "pituitary"]
#
# UPLOAD_FOLDER = "static/uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#
# # Tài khoản mặc định
# USERNAME = "admin"
# PASSWORD = "123456"
#
#
# def predict_image(img_path):
#     img = cv2.imread(img_path)
#     img = cv2.resize(img, (224, 224))
#     img = img / 255.0
#     img = np.expand_dims(img, axis=0)
#
#     pred = model.predict(img)
#     class_idx = np.argmax(pred)
#     return categories[class_idx]
#
#
# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         username = request.form.get("username")
# #         password = request.form.get("password")
# #         if username == USERNAME and password == PASSWORD:
# #             session['logged_in'] = True
# #             return redirect(url_for('index'))
# #         else:
# #             return render_template('login.html', error="Invalid credentials")
# #     return render_template('login.html')
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get("username")
#         password = request.form.get("password")
#
#         if username != USERNAME:
#             return render_template('login.html', error="Tên người dùng không đúng")
#         elif password != PASSWORD:
#             return render_template('login.html', error="Mật khẩu không đúng")
#         else:
#             session['logged_in'] = True
#             return redirect(url_for('index'))
#
#     return render_template('login.html')
#
#
# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     return redirect(url_for('login'))
#
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if not session.get('logged_in'):
#         return redirect(url_for('login'))
#
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return render_template('index1.html', error='No file uploaded')
#
#         file = request.files['file']
#         if file.filename == '':
#             return render_template('index1.html', error='No file selected')
#
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(file_path)
#         label = predict_image(file_path)
#
#         return render_template('index1.html', file_path=file_path, label=label)
#
#     return render_template('index1.html')
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, render_template, redirect, url_for, session
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Thay đổi chuỗi này trong thực tế để bảo mật

# Load model
model = load_model("brain_tumor_model.h5")
categories = ["glioma", "meningioma", "notumor", "pituitary"]

tumor_info = {
    "glioma": {
        "description": "U glioma là loại u não phát sinh từ tế bào thần kinh đệm, có thể phát triển nhanh và xâm lấn mô xung quanh.",
        "success_rate": "50-70% tùy thuộc vào giai đoạn và phác đồ điều trị.",
        "treatment": "Phẫu thuật, xạ trị và hóa trị kết hợp."
    },
    "meningioma": {
        "description": "U màng não là khối u phát triển từ màng bao quanh não và tủy sống, phần lớn là lành tính.",
        "success_rate": "90% nếu được phát hiện sớm và điều trị kịp thời.",
        "treatment": "Phẫu thuật loại bỏ u, có thể theo dõi nếu kích thước nhỏ và không có triệu chứng."
    },
    "notumor": {
        "description": "Không phát hiện khối u trong ảnh chụp.",
        "success_rate": "Không áp dụng.",
        "treatment": "Không cần điều trị, nên khám định kỳ để theo dõi."
    },
    "pituitary": {
        "description": "U tuyến yên là khối u hình thành ở tuyến yên, có thể ảnh hưởng đến nội tiết tố.",
        "success_rate": "80-90% với điều trị phù hợp.",
        "treatment": "Phẫu thuật (thường qua đường mũi), điều trị nội tiết hoặc xạ trị."
    }
}


UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Tài khoản mặc định
USERNAME = "admin"
PASSWORD = "123456"


def predict_image(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)
    class_idx = np.argmax(pred)
    return categories[class_idx]


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        if username != USERNAME:
            return render_template('login.html', error="Tên người dùng không đúng")
        elif password != PASSWORD:
            return render_template('login.html', error="Mật khẩu không đúng")
        else:
            session['logged_in'] = True
            return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index1.html', error='No file uploaded')

        file = request.files['file']
        if file.filename == '':
            return render_template('index1.html', error='No file selected')

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        label = predict_image(file_path)

        info = tumor_info[label]
        return render_template('index1.html', file_path=file_path, label=label, info=info)


    return render_template('index1.html')
if __name__ == '__main__':
    app.run(debug=True)