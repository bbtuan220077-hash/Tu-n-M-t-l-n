from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Portfolio Tuấn</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial;
}

body{
background:linear-gradient(135deg,#1e3c72,#2a5298);
color:white;
text-align:center;
}

/* MENU */

nav{
background:black;
padding:15px;
position:sticky;
top:0;
}

nav a{
color:white;
margin:0 15px;
text-decoration:none;
font-weight:bold;
}

nav a:hover{
color:#00ffff;
}

/* HERO */

.hero{
padding:60px;
animation:fadein 2s;
}

.avatar{
width:170px;
border-radius:50%;
border:5px solid white;
margin-bottom:20px;
}

/* CARD */

.card{
background:white;
color:black;
margin:30px auto;
padding:30px;
width:80%;
border-radius:15px;
box-shadow:0 10px 25px rgba(0,0,0,0.3);
}

/* SKILLS */

.skills{
display:flex;
justify-content:center;
flex-wrap:wrap;
gap:15px;
}

.skill{
background:#2a5298;
color:white;
padding:10px 20px;
border-radius:20px;
}

/* PROJECT */

.project{
margin:10px;
padding:20px;
border-radius:10px;
background:#eee;
}

/* BUTTON */

.btn{
display:inline-block;
margin:10px;
padding:12px 25px;
background:#2a5298;
color:white;
border-radius:25px;
text-decoration:none;
}

.btn:hover{
background:#1e3c72;
}

/* ANIMATION */

@keyframes fadein{
from{
opacity:0;
transform:translateY(30px);
}
to{
opacity:1;
transform:translateY(0);
}
}

</style>

</head>

<body>

<!-- MENU -->

<nav>
<a href="#">Trang chủ</a>
<a href="#about">Giới thiệu</a>
<a href="#skills">Kỹ năng</a>
<a href="#projects">Dự án</a>
<a href="#contact">Liên hệ</a>
</nav>

<!-- HERO -->

<div class="hero">

<img class="avatar" src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png">

<h1>Xin chào, tôi là Tuấn</h1>
<p>Sinh viên IT | Python Developer</p>

</div>

<!-- ABOUT -->

<div class="card" id="about">

<h2>Giới thiệu</h2>

<p>
Tôi là sinh viên công nghệ thông tin.  
Tôi đang học lập trình Python, Web Development và xây dựng các dự án phần mềm.
</p>

</div>

<!-- SKILLS -->

<div class="card" id="skills">

<h2>Kỹ năng</h2>

<div class="skills">

<div class="skill">Python</div>
<div class="skill">HTML</div>
<div class="skill">CSS</div>
<div class="skill">JavaScript</div>
<div class="skill">MySQL</div>
<div class="skill">Flask</div>

</div>

</div>

<!-- PROJECT -->

<div class="card" id="projects">

<h2>Dự án</h2>

<div class="project">
<h3>Website Portfolio</h3>
<p>Website cá nhân viết bằng Python Flask</p>
</div>

<div class="project">
<h3>Quản lý sản phẩm</h3>
<p>Hệ thống quản lý sản phẩm dùng MySQL</p>
</div>

</div>

<!-- CONTACT -->

<div class="card" id="contact">

<h2>Liên hệ</h2>

<a class="btn" href="https://www.facebook.com/chu.kieu.tuan/" target="_blank">Facebook</a>

<a class="btn" href="https://www.tiktok.com/@tunhayhat77?is_from_webapp=1&sender_device=pc" target="_blank">TikTok</a>

<a class="btn" href="https://github.com" target="_blank">GitHub</a>

</div>

</body>
</html>
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)