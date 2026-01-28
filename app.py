import os
import uuid
from flask import Flask, render_template, request, send_file, redirect, url_for, flash

from lsb import steganography_LSB
from pvd import steganography_PVD
from dct import steganography_DCT

app = Flask(__name__)
app.secret_key = "dev"  # for flash messages

UPLOAD_DIR = "uploads"
OUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)

METHODS = {
    "LSB": steganography_LSB,
    "PVD": steganography_PVD,
    "DCT": steganography_DCT,
}

@app.get("/")
def index():
    return render_template("index.html", methods=list(METHODS.keys()))

@app.post("/encode")
def encode():
    method = request.form.get("method", "LSB")
    if method not in METHODS:
        flash("Invalid method selected.")
        return redirect(url_for("index"))

    cover = request.files.get("cover")
    secret = request.files.get("secret")
    if not cover or not secret:
        flash("Please upload both cover and secret images.")
        return redirect(url_for("index"))

    run_id = str(uuid.uuid4())[:8]
    cover_path = os.path.join(UPLOAD_DIR, f"{run_id}_cover_{cover.filename}")
    secret_path = os.path.join(UPLOAD_DIR, f"{run_id}_secret_{secret.filename}")

    cover.save(cover_path)
    secret.save(secret_path)

    out_path = os.path.join(OUT_DIR, f"{run_id}_{method}_output.png")

    # Call your existing function (paths in, path out)
    METHODS[method](cover_path, secret_path, out_path)

    return send_file(out_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
