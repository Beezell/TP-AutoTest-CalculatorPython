import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, render_template_string
from app.calculatrice import addition, soustraction, multiplication, division, puissance

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Calculatrice Web</title>
<h1>Simple Calculatrice</h1>
<form method=post>
  <input name=a type=number step="any" required> 
  <select name=operation>
    <option value="addition">+</option>
    <option value="soustraction">-</option>
    <option value="multiplication">*</option>
    <option value="division">/</option>
    <option value="puissance">^</option>
  </select>
  <input name=b type=number step="any" required>
  <button  type=submit value=Calculer>
</form>

{% if result is not none %}
  <h2>Résultat : {{ result }}</h2>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def calculatrice():
    result = None
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        operation = request.form["operation"]
        try:
            match operation:
                case "addition":
                    result = addition(a, b)
                case "soustraction":
                    result = soustraction(a, b)
                case "multiplication":
                    result = multiplication(a, b)
                case "division":
                    result = division(a, b)
                case "puissance":
                    result = puissance(a, b)
        except Exception as e:
            result = f"Erreur : {e}"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
