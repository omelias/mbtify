# MBTIFY
#### Description: A Spotify API powered, MBTI related website for the Final Project of CS50's Introduction to Computer Science. Users log in with their Spotify account to see 5 of their songs, as they match with a selected MBTI type.

‎
‎

## INSTALLATION / BUILT WITH

For my project, I used a variety of programming languages and frameworks, including Python, Flask, SQL, HTML, CSS, Jinja, and JavaScript.

I installed [`spotipy`](https://spotipy.readthedocs.io/en/master/), which is a very useful Python library, if you're working with Spotify API.
```
$ pip install spotipy
```
I got my static backgrounds from [CSS Gradient](https://cssgradient.io/), my animated background from [CSS Gradient Animator](https://www.gradient-animator.com/), social media icons in the footer from [Font Awesome](https://fontawesome.com/) and my website icon from [flaticon.com](https://www.flaticon.com/).

‎
‎

## HOW TO USE?

To learn more about how Spotify API works, you can visit the [Spotify for Developers](https://developer.spotify.com/). There, you can find detailed documentation for the [Spotify Web API](https://developer.spotify.com/documentation/web-api/). Spotify provides clear and concise instructions, making it easy to understand each step of the process.

In order to use the Spotify API in a program, you must have a Client Id, a Client Secret, and a Redirect Uri. If you are using the Spotipy library, you will need to export these three values separately in the terminal window.

```
$ export SPOTIPY_CLIENT_ID='client_id'
$ export SPOTIPY_CLIENT_SECRET='client_secret'
$ export SPOTIPY_REDIRECT_URI='redirect_uri'
```
(For information on how to create an app and obtain the necessary export values, please refer to PROJECT IN DETAIL.)

Once you have exported the values, you can use the Flask framework to run the program and access the link.

```
$ flask run
```
‎
‎

## PROJECT IN DETAIL

My program uses the Spotify API to authorize a user and obtain a token to access their Spotify data. Using SQL queries and a SQL database, my program stores this information in the mbtify.db database. Once the user has successfully logged in, Spotify redirects them to a page where they can select an MBTI type to view five of their saved songs that are related to that MBTI type. I have developed a basic algorithm to determine the relationship between MBTI types and songs.

‎
#### **-CLIENT ID, CLIENT SECRET AND REDIRECT URI**
To use the Spotify API, you must first log in to [My Dashboard](https://developer.spotify.com/dashboard/login) using your Spotify account. Once logged in, click **CREATE AN APP**. Provide an app name and description for your app, and check the box to agree to the Spotify Developer Terms of Service and Branding Guidelines. This will generate a unique Client Id and Client Secret for your app. Additionally, you must set a Redirect Uri. To do this, click **EDIT SETTINGS** and add a Redirect Uri. A Redirect Uri is a address where users will be redirected after successfully authenticating their Spotify accounts through your website. Once you have obtained these values, export them in a terminal window."

‎
#### **-DATABASE**
I have created a SQL database to store user Spotify data whenever they log in. The Spotify API provides developers with access to a wide range of user data and information, and I have used the "user-library-read" scope, which allows me to access a user's Spotify library. (There are many other scopes that you can use in your program.) Additionally, my program automatically deletes user data and information after five minutes.

‎
#### **-HOW MBTI TYPES MATCH WITH SONGS?**
I receive the audio features (danceability, energy, speechiness, acousticness, valence, and tempo) of the latest 100 tracks in a user's library and store this information in my database along with the track names, artist names, genres and album covers. (It is not possible to directly obtain the covers from individual tracks, so you can only obtain them from album covers.)

For instance, valence indicates the musical positiveness conveyed by a track. Tracks with high valence (closer to 1.0) sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence (closer to 0.0) sound more negative (e.g. sad, depressed, angry). For example, if a song is in the INTJ category, its valence is more likely to be closer to 0.0. You can learn more about the algorithms behind the MBTI types from app.py.
