<div align="center">
<img src="https://github.com/rodrigoneumann/third-milestone-project/raw/master/semgmtapp/static/img/readme-img.png" target="_blank" rel="noopener" alt="Swift Estates">
<h2>Swift Estates Property Management</h2>
</div>

This property management platform was designed with the main purpose of being a tool that allows the easy management and visualization of properties for agents of a real estate agency in the Portsmouth-Uk and nearby locations.
On the platform, the registered agent will be able to add, edit and delete the properties that have been added by him and will be able to view all the properties added by other agents, whether for sale or rent. Which greatly facilitates the real estate agency's internal work.
It is also possible for the agent to manage their profile on the platform, such as changing their password, changing their photo or even deleting their registration.
#### You can access the platform [here.](https://swift-estates.herokuapp.com)


## Table of Contents

1.  [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
      - [**Typography**](#typography)
      - [**Colours**](#colours)
      - [**Icons**](#icons)
    - [**Wireframes**](#wireframes)

2.  [**Features**](#features)
  - [**Existing Features**](#existing-features)
  - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Compatibility**](#compatibility)
    - [**Known Issues**](#known-issues)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Acknowledgements**](#acknowledgements)

---

# UX

## User Stories

### As a user of this platform, I will be able to:

- Access the platform from your favourite equipment, such as smartphones, tablets, laptops or PCs, without loss of content.
- View all properties registered on the platform and all its details, such as locating, number of bedrooms, number of bathrooms, value, type of negotiation, property description, and others, as a visitor (without having to be logged in) or logged in. 
- Create an agent account on the platform.
- Add new properties on the platform.
- Update the properties included by me on on the platform.
- Delete the properties included by me on the platform.
- Update my agent profile, how to add or change my photo. However, if I don't want to add a photo, a standard photo will be added to your profile
- Update my password.
- Delete my agent profile from the platform.
- View all properties filtered by type of negotiation, such as properties for sale or rent.
- View the latest properties for sale and rental on the home page in carousels, and be able to access them directly through it.
- Filter and view all my ads, for sale or rent.

## Design
This project was developed with a focus on a mobile approach first. However, with full responsiveness on other screen sizes.
I used the grids, nav, carousel and bootstrap colors in this project.
The main idea for the design of this project was to have a serious and professional appearance at the same time, with light colors, a box with rounded corners and soft shadows, which convey sophistication and provide a pleasant user experience.

### Typography

- The main font used in this project is **Robotto**. I think that's a well designed and easy to read font. An extra reason for using this font is the excellent display on small screens.
- In the main titles of the site, the font **Poppins** was used, which also has a good design and combines nicely with the main font.


### Colours

- In the color scheme I used shades that favored the easy visualization of the information.
- In the navbar and footer I used the white background with letters in a dark gray tone, giving a greater contrast for logo information and menu options. As well as a light shadow in the division with the Body.
- In the background I used an image of the wooden floor with a slight change in opacity to make it a little lighter.
- In the boxes for adding and editing properties, login and user registration, a title with a dark gray background with white letters was used to give greater contrast.
- The buttons have a dark tone with white letters and black borders, making an interesting effect.
- Some images with white dolls were used in the user's standard photo and when the user has not yet included any ad.

### Icons

The icons used in this project are provided by [Font Awesome 5.12.1](https://fontawesome.com/).
They were used in the social media icons in the footer.

## Wireframes

These wireframes were designed with Balsamiq Mockups 3. These were the first version of scope and some minor things have changed during the development for the final version.
* Mobile displays [here](https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/wireframes/wireframe_mobile.png)
* Medium displays [here](https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/wireframes/wireframe_tablet.png)
* Large displays [here](https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/wireframes/wireframe_desktop.png)

# Features

## Existing Features

## Features Left to Implement

# Technologies Used
## Tools
  - [Visual Studio Code](https://code.visualstudio.com/) 
      - IDE used for development of this project.
  - [Balsamiq Mockups 3](https://balsamiq.com/) 
    - Used to create the wireframes and planning this project
  - [Dev Tools](https://www.google.com/chrome/)
    - This project used the Dev Tools from 3 browsers: Chrome, Firefox and Safari. They were necessary to keep track and test the code during the development.
  - [Heroku](https://www.heroku.com) 
      - Used for app hosting and deploying.
  - [GitHub](https://github.com/)
      - This project uses **GitHub** to store and share all project code remotely.
  - [Git](https://git-scm.com/) 
      - It is used for version control
  - [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) 
      - It is the database used for this project.
  - [Photoshop 2020](http://www.adobe.com/Photoshop)
      - This project used **Photoshop 2020** to edit all the images.
  - [Illustrator 2020](http://www.adobe.com/illustrator)
      - This project used **Illustrator 2020** to create and edit the logo.
  - [Tinypng](https://tinypng.com/)
      -  Used to compress the size of images.
  - [Imgbb](https://imgbb.com) 
      - used to store some external images for this project.
  - [Am I Responsive](http://ami.responsivedesign.is/) to get images for the README in different screen sizes. 
  
## Libraries

  - [Bootstrap](https://www.bootstrapcdn.com/)
      - This project uses **Bootstrap** for better responsiveness and organization. It was also used for some CSS attributes and effects.
  - [FontAwesome](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/css/all.min.css)
      - The project uses **Font Awesome** to provide some icons. 
  - [Google Fonts](https://fonts.google.com/)
      - The project uses **Google fonts** to provide 'Roboto' ans 'Poppins' font.
  - [JQuery](https://jquery.com) 
      - Used to simplify DOM manipulation.
  - [Flask 1.1.1](http://flask.pocoo.org/)   
     - Back-end Python microframework.
  - [PyMongo 3.10.1](https://api.mongodb.com/python/current/) - Python API for MongoDB.
  - [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) 
      - It is the default templating language for flask used for display data from the python application in Html templates.

## Languages

  - In this project Is used **HTML5**, **CSS**, **JAVASCRIPT** and **PYTHON** as programming languages.

# Testing

During the development of this project, I had the experience of facing some problems, exhaustively testing the functionality of each part of the platform and managed to solve most of the problems that arose before writing this document.

I received help from some family and friends to do the tests on the platform resources and all the problems presented were solved without problems.

The tests were performed with a user logged in or not on the platform.

Tests of direct access to the system directly through the path without authentication or access to content restricted to another user were all blocked and worked without problems.

New agent registration tests, all existing user checks, profile options, how to change the password, change the link to the photo path and delete the account and everything worked without problems.

Tests to add new ads since all fields in the forms also responded well to the verification standards before sending the data to the server.

The request tests the data for a specific ad so that changes are made and sent back to the database also work smoothly.
All error or confirmation flash messages are also running smoothly.

### Tools used for testing

#### Code Validation
- HTML

  - [The W3C Markup Validation Service](https://validator.w3.org/)

- CSS

  - [The W3C Markup Validation Service](https://jigsaw.w3.org/css-validator)

- JavaScript

  - [JS Hint](https://jshint.com/)

- Python
  - [PEP8](http://pep8online.com/) - The Python scripts was checked with pep8online. almost all the errors were solved, the only ones that persisted were of lines longer than 79 characters in some cases, however in most cases they are in mongoDB query lines.

#### Responsiveness

* The Chrome and Firefox browser development tools were used to check for responsiveness and scaling issues on different screen sizes.

* This project was tested across multiple browsers (Chrome, Opera, Safari, Firefox, and IE) in different simulated and real devices.

- Phones

  - Galaxy Note 8
  - Galaxy Note 9
  - Gakaxy Note 10 (real device)
  - Galaxy S5
  - Galaxy S7+ (real device)
  - Galaxy S9/S9+ (real device)
  - Galaxy S10 (real device)
  - iPhone 5/SE
  - iPhone 6/7/8
  - iPhone 8 Plus (real device)
  - iPhone X (real device)
  - iPhone XR (real device)
  - iphone XS 
  - iphone XS Max (real device)
  - Huawei P30 Pro (real device)
  - Nexus 5X
  - Nexus 6P
  - Pixel 2
  - Pixel 2 XL

- Tablets
  - iPad (real device)
  - iPad Pro 10.5-inch
  - iPad Pro 12.9
  - Kindle Fire HDX
  - Nexus 10
  - Nexus 7

* Laptops

  - MacBook Pro 13" (real device)
  - Asus Swift 3 (real device)

* Windows 10 computer
  - Philips 1080p Full HD (real device)
 
**Were found some display issues with discontinued browsers such as IE and obsolete versions of Chrome and Opera.**

# Deployment

## Local Deployment
To run this project on your own systen please follow the instructions below:

You will need the following tools installed on your system:

- [Python 3](https://www.python.org/downloads/)
- An IDE such as [Visual Studio Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/download/)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) 
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)


#### Instructions
- Save a copy of the github repository located at https://github.com/rodrigoneumann/third-milestone-project.
  - Unzip the repo into the choosen folder.
- If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/rodrigoneumann/third-milestone-project
```

- Within the chosen directory, create a virtual environment with the command:
```
python -m .venv venv
```  

- Activate the virtual environment with the command:
```
venv\Scripts\activate 
```

- Install all required modules with the command: 
```
pip install -r requirements.txt
```

- Create a file called `.flaskenv` if not exists.

- Inside the .flaskenv file check for the following commands:
```
FLASK_ENV=development
FLASK_APP=app.py
```

- Create a database in Mongodb Atlas called **semgmtapp**
- Create 2 collections, one of then called **users** and another called **properties**

- Create an .env file with your credentials:
e.g
```
MONGO_URI="insert your mongo uri details here"
SECRET_KEY="insert your secret key here"
```

- Run the application with the command
```
python app.py
```
- Open the website at `http://127.0.0.1:5000`

## Remote Deployment

# Credits

## Content

## Acknowledgements
