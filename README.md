[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/TechVictorKE/neighborhood-watch">
    <img src="https://github.com/TechVictorKE/neighborhood-watch/blob/master/security/static/img/anon.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Neighbourhood Watch</h3>

  <p align="center">
    <br />
    <a href="https://github.com/TechVictorKE/neighborhood-watch"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/TechVictorKE/neighborhood-watch">View Demo</a>
    ·
    <a href="https://github.com/TechVictorKE/neighborhood-watch/issues">Report Bug</a>
    ·
    <a href="https://github.com/TechVictorKE/neighborhood-watch/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Hood Watch Screen Shot][product-screenshot]](https://example.com)

If you are like me, you really don’t know what is happening in your neighborhood most of the time. What if an important meeting happens, theft or even death wouldn’t you like to know about it? This is a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts!

### Built With

* [Python](https://www.python.org/) for backend
* [HTML](https://html.com/) for web app structure
* [Bootstrap](https://getbootstrap.com/) and [Javascript](https://www.javascript.com/) for styling
* [Heroku](https://heroku.com)



<!-- GETTING STARTED -->
## Getting Started

* Live site can be accessed from the following [link]()
* Pre-configured Admin details are:<br>
Password: thejigisup <br>
Username: Kibocha

### Prerequisites

* Python 3.8

### Installation

1. Clone the repo
   ```
   git clone https://github.com/TechVictorKE/neighborhood-watch.git
   ```
2. Create virtual environment
   ```
   python3 -m venv venv
   ```
3. Install requirements
   ```
   pip install -r requirements.txt
   ```
4. Create migrations
   ```
   python3 manage.py makemigrations
   ```
   ```
   python3 manage.py migrate
   ```
5. Run application
   ```
   python3 manage.py runserver
   ```



<!-- USAGE EXAMPLES -->
## Usage

This application can be used to keep track pf the events happening around your neighbourhood.

Home(superuser):
<img src="https://github.com/TechVictorKE/neighborhood-watch/blob/master/security/static/img/screenshots/home1.png">

Home(normal users):
<img src="https://github.com/TechVictorKE/neighborhood-watch/blob/master/security/static/img/screenshots/home2.png">

Notifications:
<img src="https://github.com/TechVictorKE/neighborhood-watch/blob/master/security/static/img/screenshots/notifications.png">

Profile:
<img src="https://github.com/TechVictorKE/neighborhood-watch/blob/master/security/static/img/screenshots/profile.png">

Edit Profile:
<img src="https://github.com/TechVictorKE/neighborhood-watch/blob/master/security/static/img/screenshots/edit-profile.png">



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/TechVictorKE/neighborhood-watch/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See the [LICENSE.md](LICENSE.md) file for more information.



<!-- CONTACT -->
## Contact

Victor Kibocha - [@Victor_Kibocha](https://twitter.com/Victor_Kibocha) - vicikibocha@gmail.com

Project Link: [Github](https://github.com/TechVictorKE/)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* Moringa School





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TechVictorKE/neighborhood-watch.svg?style=for-the-badge
[contributors-url]: https://github.com/TechVictorKE/neighborhood-watch/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TechVictorKE/neighborhood-watch.svg?style=for-the-badge
[forks-url]: https://github.com/TechVictorKE/neighborhood-watch/network/members
[stars-shield]: https://img.shields.io/github/stars/TechVictorKE/neighborhood-watch.svg?style=for-the-badge
[stars-url]: https://github.com/TechVictorKE/neighborhood-watch/stargazers
[issues-shield]: https://img.shields.io/github/issues/TechVictorKE/neighborhood-watch.svg?style=for-the-badge
[issues-url]: https://github.com/TechVictorKE/neighborhood-watch/issues
[license-shield]: https://img.shields.io/github/license/TechVictorKE/neighborhood-watch.svg?style=for-the-badge
[license-url]: https://github.com/TechVictorKE/neighborhood-watch/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/victor-kibocha-b106b21bb/
[product-screenshot]: https://github.com/TechVictorKE/neighborhood-watch/blob/master/security/static/img/screenshots/home2.png
