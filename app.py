import os
from cs50 import SQL
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from flask import Flask, render_template, redirect, request, session, make_response,session,redirect
from flask_session import Session
import requests


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set database variable.
db = SQL("sqlite:///mbtify.db")

# Get secret_key for flask.
app.secret_key = os.urandom(24)

API_BASE = 'https://accounts.spotify.com'
# Provide unique client_id, client_secret and redirect_uri.
CLI_ID = "client_id"
CLI_SEC = "client_secret" 
REDIRECT_URI= "redirect_uri"
SCOPE = 'user-library-read'
position = 0
LOGIN = False
SHOW_DIALOG = True

# Index page
@app.route("/")
def index():
    return render_template("index.html")


# Spotify's authorization screen
@app.route("/auth", methods=["POST"])
def auth():
    auth_url = f'{API_BASE}/authorize?client_id={CLI_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={SCOPE}&show_dialog={SHOW_DIALOG}'
    return redirect(auth_url)


# Callback to /logged route after the successful authorization
@app.route("/api_callback")
def api_callback():
    session.clear()
    code = request.args.get("code")

    auth_token_url = f"{API_BASE}/api/token"
    res = requests.post(auth_token_url, data={
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":"https://omelias-code50-106240728-q75q7jvp5244jg-5000.githubpreview.dev/logged",
        "client_id":CLI_ID,
        "client_secret":CLI_SEC
        })

    res_body = res.json()
    session["token"] = res_body.get("access_token")

    return redirect("/")


# MBTI type selection form appears after the successful authorization
@app.route("/logged")
def logged():
    return render_template("logged.html")


# MBTI routes:

@app.route("/intj", methods=["POST"])
def intj():
    if request.method == "POST":
        intj_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE 0.5 >= danceability >= 0.15 AND 0.9 >= energy >= 0.2 AND speechiness <= 0.55  AND acousticness <= 0.18 AND valence <= 0.6 AND 175.00 >= tempo <= 80.000 OR genre LIKE '%rock%' OR genre LIKE '%metal%' OR genre LIKE '%classical%' ORDER BY RANDOM() LIMIT 5")
        return render_template("intj.html", intj_results=intj_results)


@app.route("/intp", methods=["POST"])
def intp():
    if request.method == "POST":
        intp_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE 0.8 >= danceability >= 0.3 AND 0.9 >= energy >= 0.25 AND speechiness <= 0.1 AND acousticness <= 0.15 AND 0.75 >= valence >= 0.25 AND 170.00 >= tempo <= 95.000 OR genre LIKE '%anime%' OR genre LIKE '%electronic%' ORDER BY RANDOM() LIMIT 5")
        return render_template("intp.html", intp_results=intp_results)


@app.route("/entj", methods=["POST"])
def entj():
    if request.method == "POST":
        entj_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE 0.65 >= danceability >= 0.15 AND 0.9 >= energy >= 0.3 AND 0.15 >= speechiness >= 0.03 AND acousticness <= 0.1 AND valence <= 0.7 AND tempo <= 175.000 AND tempo >= 80.000 OR genre LIKE '%classical%' OR genre LIKE '%jazz%' OR genre LIKE '%electronic%' ORDER BY RANDOM() LIMIT 5")
        return render_template("entj.html", entj_results=entj_results)


@app.route("/entp", methods=["POST"])
def entp():
    if request.method == "POST":
        entp_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE danceability <= 0.5 AND 0.96 >= energy >= 0.5 AND speechiness <= 0.15 AND 0.65 >= valence >= 0.15 AND tempo <= 175.000 AND tempo >= 95.000 OR genre LIKE '%metal%' OR genre LIKE '%rock%' ORDER BY RANDOM() LIMIT 5")
        return render_template("entp.html", entp_results=entp_results)


@app.route("/infj", methods=["POST"])
def infj():
    if request.method == "POST":
        infj_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE danceability <= 0.65 AND energy <= 0.7 AND speechiness <= 0.5  AND acousticness <= 0.35 AND valence <= 0.55 AND tempo <= 150.000 AND tempo >= 70.000 OR genre LIKE '%indie%' OR genre LIKE '%classical%' OR genre LIKE '%alternative%' ORDER BY RANDOM() LIMIT 5")
        return render_template("infj.html", infj_results=infj_results)


@app.route("/infp", methods=["POST"])
def infp():
    if request.method == "POST":
        infp_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE danceability <= 0.7 AND energy <= 0.7 AND speechiness <= 0.5 AND acousticness <= 0.5 AND valence <= 0.4 AND tempo <= 140.000 AND tempo >= 70.000 OR genre LIKE '%alternative%' OR genre LIKE '%punk%' OR genre LIKE '%indie%' ORDER BY RANDOM() LIMIT 5")
        return render_template("infp.html", infp_results=infp_results)


@app.route("/enfj", methods=["POST"])
def enfj():
    if request.method == "POST":
        enfj_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE 0.85 >= danceability >= 0.25 AND 0.85 >= energy >= 0.3 AND speechiness <= 0.5 AND acousticness <= 0.5 AND valence <= 0.65 AND tempo <= 160.000 AND tempo >= 80.000 OR genre LIKE '%blues%' OR genre LIKE '%jazz%' ORDER BY RANDOM() LIMIT 5")
        return render_template("enfj.html", enfj_results=enfj_results)


@app.route("/enfp", methods=["POST"])
def enfp():
    if request.method == "POST":
        enfp_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE 0.99 >= danceability >= 0.85 AND 0.99 >= energy >= 0.85 AND speechiness <= 0.55  AND acousticness <= 0.2 AND 0.99 >= valence >= 0.8 AND tempo <= 170.000 AND tempo >= 95.000 OR genre LIKE '%electronic%' OR genre LIKE '%pop%' ORDER BY RANDOM() LIMIT 5")
        return render_template("enfp.html", enfp_results=enfp_results)


@app.route("/istj", methods=["POST"])
def istj():
    if request.method == "POST":
        istj_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE danceability <= 0.6 AND energy <= 0.6 AND speechiness <= 0.4 AND acousticness <= 0.7 AND valence <= 0.6 AND tempo <= 130.000 AND tempo >= 65.000 OR genre LIKE '%classical%' ORDER BY RANDOM() LIMIT 5")
        return render_template("istj.html", istj_results=istj_results)


@app.route("/isfj", methods=["POST"])
def isfj():
    if request.method == "POST":
        isfj_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE danceability <= 0.7 AND energy <= 0.8 AND speechiness <= 0.5  AND acousticness <= 0.7 AND valence <= 0.6 AND tempo <= 130.000 AND tempo >= 70.000 OR genre LIKE'%indie%' OR genre LIKE '%religious%' ORDER BY RANDOM() LIMIT 5")
        return render_template("isfj.html", isfj_results=isfj_results)


@app.route("/estj", methods=["POST"])
def estj():
    if request.method == "POST":
        estj_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE danceability <= 0.6 AND energy <= 0.85 AND speechiness <= 0.4  AND acousticness <= 0.6 AND valence <= 0.45 AND tempo <= 160.000 AND tempo >= 75.000 OR genre LIKE '%electronic%' OR genre LIKE '%hip hop%' ORDER BY RANDOM() LIMIT 5")
        return render_template("estj.html", estj_results=estj_results)


@app.route("/esfj", methods=["POST"])
def esfj():
    if request.method == "POST":
        esfj_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE 0.99 >= danceability >= 0.75 AND 0.99 >= energy >= 0.8 AND speechiness <= 0.5 AND acousticness <= 0.2 AND 0.97 >= valence >= 0.75 AND tempo <= 150.000 AND tempo >= 100.000 OR genre LIKE '%pop%' OR genre LIKE '%country%' ORDER BY RANDOM() LIMIT 5")
        return render_template("esfj.html", esfj_results=esfj_results)


@app.route("/istp", methods=["POST"])
def istp():
    if request.method == "POST":
        istp_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE danceability <= 0.6 AND 0.9 >= energy >= 0.35 AND speechiness <= 0.2  AND acousticness <= 0.2 AND valence <= 0.5 AND tempo <= 180.000 AND tempo >= 85.000 OR genre LIKE '%rock%' OR genre LIKE '%metal%' ORDER BY RANDOM() LIMIT 5")
        return render_template("istp.html", istp_results=istp_results)


@app.route("/isfp", methods=["POST"])
def isfp():
    if request.method == "POST":
        isfp_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE 0.85 >= danceability >= 0.4 AND energy <= 0.85 AND speechiness <= 0.4 AND acousticness <= 0.5 AND valence <= 0.6 AND tempo <= 150.000 AND tempo >= 80.000 OR genre LIKE '%ambient%' OR genre LIKE '%pop%' ORDER BY RANDOM() LIMIT 5")
        return render_template("isfp.html", isfp_results=isfp_results)


@app.route("/estp", methods=["POST"])
def estp():
    if request.method == "POST":
        estp_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE 0.99 >= danceability >= 0.6 AND 0.9 >= energy >= 0.35 AND 0.6 >= speechiness >= 0.3  AND acousticness <= 0.2 AND valence <= 0.5 AND tempo <= 180.000 AND tempo >= 85.000 OR genre LIKE '%hip hop%' OR genre LIKE '%rap%' ORDER BY RANDOM() LIMIT 5")
        return render_template("estp.html", estp_results=estp_results)


@app.route("/esfp", methods=["POST"])
def esfp():
    if request.method == "POST":
        esfp_results = db.execute("SELECT DISTINCT(track_name), artist_name, album_cover FROM audio WHERE 0.99 >= danceability >= 0.6 AND 0.99 >= energy >= 0.75 AND speechiness <= 0.3 AND acousticness <= 0.25 AND valence >= 0.6 AND tempo <= 160.000 AND tempo >= 100.000 OR genre LIKE '%pop%' OR genre LIKE '%rap%' OR genre LIKE '%hip hop%' ORDER BY RANDOM() LIMIT 5")
        return render_template("esfp.html", esfp_results=esfp_results)



# Read users' Spotify library
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Get latest 50 songs
results1 = sp.current_user_saved_tracks(limit=50, offset=0, market=None)

for track in results1["items"]:

    # Track name
    track_name = track["track"]["name"]
    track_uri = track["track"]["uri"]

    # Artist information
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    artist_name = track["track"]["artists"][0]["name"]
    artist_genres = artist_info["genres"]

    # Iterate over genres and get one genre
    for genre in artist_genres:
        genre = genre

    # Get album cover
    for height, url, width in track["track"]["album"]["images"]:
        url = track["track"]["album"]["images"][0]["url"]
        album_cover = url

    # Get Audio Featues
    features = sp.audio_features(track_uri)[0]

    if features != None:
            AudioFeatures = [features['danceability'], features['energy'], features['loudness'], features['speechiness'],
                            features['acousticness'], features['valence'], features['tempo']]

    # Insert users' track information into audio table
    db.execute("INSERT INTO audio (danceability, energy, speechiness, acousticness, valence, tempo, track_name, artist_name, genre, album_cover) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                features['danceability'], features['energy'], features['speechiness'], features['acousticness'], features['valence'], features['tempo'], track_name, artist_name, genre, album_cover)

# Get latest 50 songs with an offset of 50 (Because of the limitation, we can't get 100 songs at a single time)
results2 = sp.current_user_saved_tracks(limit=50, offset=50, market=None)

for track in results2["items"]:

    # Track name
    track_name = track["track"]["name"]
    track_uri = track["track"]["uri"]

    # Artist information
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    artist_name = track["track"]["artists"][0]["name"]
    artist_genres = artist_info["genres"]

    # Iterate over genres and get one genre
    for genre in artist_genres:
        genre = genre

    # Get album cover
    for height, url, width in track["track"]["album"]["images"]:
        url = track["track"]["album"]["images"][0]["url"]
        album_cover = url

    # Get Audio Featues
    features = sp.audio_features(track_uri)[0]

    if features != None:
            AudioFeatures = [features['danceability'], features['energy'], features['loudness'], features['speechiness'],
                            features['acousticness'], features['valence'], features['tempo']]

    # Insert users' track information into audio table
    db.execute("INSERT INTO audio (danceability, energy, speechiness, acousticness, valence, tempo, track_name, artist_name, genre, album_cover) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                features['danceability'], features['energy'], features['speechiness'], features['acousticness'], features['valence'], features['tempo'], track_name, artist_name, genre, album_cover)
    

# Delete all user information from database after five minutes
def delete_data():
    time.sleep(300)
    db.execute("DELETE FROM audio")

thread = threading.Thread(target=delete_data)
thread.start()
