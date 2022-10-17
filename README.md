# MBTIFY
#### Description: A Spotify API powered, MBTI related website for the Final Project of CS50's Introduction to Computer Science. Users log in with their Spotify account to see 5 of their songs, as they match with a selected MBTI type.

‎
‎

## INSTALLATION / BUILT WITH

I worked with Python, Flask, SQL, HTML, CSS, Jinja and JavaScript for my project.

I installed [`spotipy`](https://spotipy.readthedocs.io/en/master/), which is a very useful Python library, if you're working with Spotify API.
```
$ pip install spotipy
```
I got my static backgrounds from [CSS Gradient](https://cssgradient.io/), my animated background from [CSS Gradient Animator](https://www.gradient-animator.com/), social media icons in the footer from [Font Awesome](https://fontawesome.com/) and my website icon from [flaticon.com](https://www.flaticon.com/).

‎
‎

## HOW TO USE?

You can check the [Spotify for Developers](https://developer.spotify.com/) to discover how Spotify API works and read the documentation from [Spotify Web API](https://developer.spotify.com/documentation/web-api/). Spotify makes it super easy to understand every step from authentication to getting a user's top artists.

Every Spotify API powered program requires a Client Id, Client Secret and a Redirect Uri. Since I also work with Spotipy, it requires to export these three essentials, separately, in terminal window.
```
$ export SPOTIPY_CLIENT_ID='client_id'
$ export SPOTIPY_CLIENT_SECRET='client_secret'
$ export SPOTIPY_REDIRECT_URI='redirect_uri'
```
(To understand how to create an app and get those exported information, please read PROJECT IN DETAIL.)

After exporting the information above, you can run flask framework to access the link of the website.
```
$ flask run
```
‎
‎

## PROJECT IN DETAIL

My program, initially authorizes a user into their Spotify account and gets a token to access their Spotify data. With SQL queries and a SQL database, my program stores users' data and information in mbtify.db database. After a user successfully logs in, Spotify redirects the user to a page, where the users can choose an MBTI type to see 5 of their songs (saved in their Spotify library), related to the selected MBTI type. I have a basic algorithm for the relation between MBTI types and songs.

‎
#### **-CLIENT ID, CLIENT SECRET AND REDIRECT URI**
To work with Spotify API, firstly go to [My Dashboard](https://developer.spotify.com/dashboard/login) and log in with your Spotify account. Then click **CREATE AN APP**. Provide an app name and a description, and check the box to agree with Spotify's Developer Terms of Service and Branding Guidelines. Then you can get your unique Client Id and Client Secret. But you also have to set a Redirect Uri. Click **EDIT SETTINGS** and add a Redirect Uri. A Redirect Uri is the address where you want users to be redirected when they successfully authentiacte their Spotify accounts with your website. Copy all three of these information and export them in terminal window.

‎
#### **-DATABASE**
I've created a SQL database to get a user's Spotify data whenever they log in. Spotify gives a controversially wide access to developers in terms of users' data and information. I only worked with the scope called user-library-read, where I can access every user's Spotify library. (There are lots of other scopes you can add to your program.)

‎
#### **-HOW MBTI TYPES MATCH WITH SONGS?**
I recieve audio features (danceability, energy, speechiness, acousticness, valence and tempo) of the latest 100 tracks in users' library and store those tracks' audio information in my database along with tracks' names, tracks' artist names, tracks' genres and album cover where tracks belong (because Spotify doesn't allow to get track covers.).

For instance, valence indicates the musical positiveness conveyed by a track. Tracks with high valence (closer to 1.0) sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence (closer to 0.0) sound more negative (e.g. sad, depressed, angry). For example, if a song is in INTJ category, its valence is more likely to be closer to 0.0. You can learn more about the algorithms behind the MBTI types from app.py.
