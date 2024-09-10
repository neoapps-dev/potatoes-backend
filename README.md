<p align="center">
  <img src="https://github.com/neoapps-dev.png" alt="The Dev :)" width="120" height="120"/>
</p>
<div align="center">
    <h1>Potatoes</h1>
    <p>A very weird RFP (Reverse-Fetch Proxy) and domain system made with Python and Flask!</p>
    <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" />
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
    <a href="CODE_OF_CONDUCT.md"><img src="https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg?style=for-the-badge" /> </a>
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/neoapps-dev/potatoes-backend?style=for-the-badge">
</div>


## Deploying
Don't trust our [official server](https://potatoes-backend.vercel.app/)? No worries!

You can deploy your own server!

To do so, click on the button below!

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fneoapps-dev%2Fpotatoes-backend)

## Running locally
Don't trust [Vercel](https://vercel.com)? No worries!

You can run your own Potato server!

(NOTE: THIS WON'T CHANGE YOUR IP ADDRESS)

Alright, Let's get started!

1. **Installing Python**

   - **On Windows**: Download and install Python 3.12.6+ from [Python.org](https://python.org).
   - **On GNU/Linux**:
     - **Debian-based systems**:
       ```sh
       sudo apt update
       sudo apt install python3
       ```
     - **Arch-based systems**:
       ```sh
       sudo pacman -Sy
       sudo pacman -S python
       ```
     - **Other distributions**: Search for Python installation instructions specific to your distribution.
   - **On macOS**: Download and install Python 3.12.6+ from [Python.org](https://www.python.org/ftp/python/3.12.6/python-3.12.6-macos11.pkg).

    
2. **Installing Dependencies**

  ```sh
  pip install -r requirements.txt
  ```

3. **Running the server**

  ```sh
  python3 app.py
  ```

4. **Open your browser**

  Open your browser at [this](http://localhost:8080)

  you will see a "Not Found" error,
    
  Try [this](http://localhost:8080/google.potato) instead.

  You should see Google :)

## Contributing

If you want to contribute to Potatoes or report issues, please check out our [contributing guidelines](CONTRIBUTING.md) or [file an issue](https://github.com/neoapps-dev/potatoes-backend/issues).

## NOTE
This project is currently under construction and may not be fully functional yet. Stay tuned for updates!
