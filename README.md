# TopTrackTracker

**TopTrackTracker** is a Flask-based web app that allows users to view their latest Liked Songs on Spotify. It leverages the Spotipy library to authenticate with the Spotify API and retrieve the user's saved tracks. The application presents the user with a list of their 10 latest Liked Songs, including details such as the artist, song name, popularity, and a link to listen on Spotify.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/your-repo.git

2. Install the required dependencies:
   pip install -r requirements.txt

## Usage

1. Set up the necessary environment variables:

SPOTIPY_CLIENT_ID: The client ID for your Spotify application.
SPOTIPY_CLIENT_SECRET: The client secret for your Spotify application.
SPOTIPY_REDIRECT_URI: The redirect URI for your Spotify application.

2. Run the Flask application:
   python application.py

3. Open your web browser and navigate to http://localhost:5000 to access the application.

## Configuration

You can customize the behavior of the application by modifying the following variables in application.py:

client_id: Your Spotify application's client ID.
client_secret: Your Spotify application's client secret.
redirect_uri: Your Spotify application's redirect URI.

## Contributing

Contributions to the project are welcome. To contribute, please follow these steps:

Fork the repository.
Create a new branch.
Make your changes and commit them.
Push your changes to your forked repository.
Submit a pull request.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
