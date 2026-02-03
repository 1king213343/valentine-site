from flask import Flask, render_template_string

app = Flask(__name__)

SECRET_PATH = "pink-roses-2147"

HOME_HTML = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Quick Note</title>
<style>
body { font-family: Arial; padding: 40px; }
.card { max-width: 500px; padding: 20px; border: 1px solid #ddd; border-radius: 15px; }
</style>
</head>

<body>
<div class="card">
<h2>Hey 😊</h2>
<p>I made something small for you.</p>
<p>Hint: the surprise is not on this page.</p>
</div>
</body>
</html>
"""

SECRET_HTML = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>💖</title>

<style>
body {
  font-family: Arial, sans-serif;
  background: #ffe6f0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.card {
  background: white;
  padding: 30px;
  border-radius: 20px;
  text-align: center;
}

button {
  padding: 12px 25px;
  margin: 10px;
  font-size: 18px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
}

.yes { background: #ff4d88; color: white; }
.no { background: #ccc; }
.hidden { display: none; }
</style>
</head>

<body>

<div class="card">

<h2>💖 Will you be my Valentine? 💖</h2>

<div id="mainButtons">
<button class="yes" onclick="sayYes()">YES 💕</button>
<button class="no" onclick="startNo()">NO 😅</button>
</div>

<div id="noFlow" class="hidden">
<p id="questionText"></p>
<button onclick="nextNo()">Continue 😄</button>
</div>

<div id="yesMessage" class="hidden">
<h2>Yaaay 💕</h2>
<p>You just made me very happy 😊</p>
</div>

</div>

<script>

let noQuestions = [
"Are you sure? 😢",
"Like really really sure? 🥺",
"What if I bring chocolates? 🍫",
"What if I bring flowers? 🌹",
"Okay last chance... Think carefully 😌"
];

let noIndex = 0;

function startNo(){
document.getElementById("mainButtons").classList.add("hidden");
document.getElementById("noFlow").classList.remove("hidden");
document.getElementById("questionText").innerText = noQuestions[0];
}

function nextNo(){
noIndex++;
if(noIndex < noQuestions.length){
document.getElementById("questionText").innerText = noQuestions[noIndex];
}else{
sayYes();
}
}

function sayYes(){
document.getElementById("mainButtons").classList.add("hidden");
document.getElementById("noFlow").classList.add("hidden");
document.getElementById("yesMessage").classList.remove("hidden");
}

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME_HTML)

@app.route(f"/{SECRET_PATH}")
def secret():
    return SECRET_HTML

if __name__ == "__main__":
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

