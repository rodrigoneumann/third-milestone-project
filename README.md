<div align="center">
<img src="https://github.com/rodrigoneumann/third-milestone-project/raw/master/semgmtapp/static/img/readme-img.png" target="_blank" rel="noopener" alt="Swift Estates">
<h2>Swift Estates Property Management</h2>
</div>

This property management platform was designed with the main purpose of being a tool that allows the easy management and visualization of properties for agents of a real estate agency in the Portsmouth-Uk and nearby locations.
On the platform, the registered agent will be able to add, edit and delete the properties that have been added by him and will be able to view all the properties added by other agents, whether for sale or rent. Which greatly facilitates the real estate agency's internal work.
It is also possible for the agent to manage their profile on the platform, such as changing their password, changing their photo or even deleting their registration.
#### You can access the platform [here.](https://swift-estates.herokuapp.com)


## Table of Contents

1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
      - [**Typography**](#typography)
      - [**Colours**](#colours)
      - [**Icons**](#icons)
    - [**Wireframes**](#wireframes)

- [UX](#ux)
  - [User Stories](#user-stories)
    - [As a user of this platform, I will be able to:](#as-a-user-of-this-platform-i-will-be-able-to)
  - [Design](#design)
    - [Typography](#typography)
    - [Colours](#colours)
    - [Icons](#icons)
  - [Wireframes](#wireframes)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Base](#base)
    - [Register a new agent](#register-a-new-agent)
    - [Agent Login](#agent-login)
    - [Agent Profile](#agent-profile)
      - [Update Photo](#update-photo)
      - [Update Password](#update-password)
      - [Delete Account](#delete-account)
    - [Listing ads](#listing-ads)
    - [Add a new property](#add-a-new-property)
    - [Update a property](#update-a-property)
    - [Delete a property](#delete-a-property)
    - [My ads](#my-ads)
    - [Error Page](#error-page)
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
  - [Tools](#tools)
  - [Libraries](#libraries)
  - [Languages](#languages)
- [Testing](#testing)
    - [Tools used for testing](#tools-used-for-testing)
      - [Validators](#validators)
      - [Responsiveness](#responsiveness)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
      - [Instructions](#instructions)
  - [Remote Deployment](#remote-deployment)
      - [Instructions](#instructions-1)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
      - [Images](#images)
    - [Code](#code)
  - [Acknowledgements](#acknowledgements)

3. [**Technologies Used**](#technologies-used)
     - [**Tools**](#tools)
     - [**Libraries**](#libraries)
     - [**Languages**](#languages)

4. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Responsiveness**](#responsiveness)

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
I used the grids, nav, carousel and bootstrap colours in this project.
The main idea for the design of this project was to have a serious and professional appearance at the same time, with a light colour, a box with rounded corners and soft shadows, which convey sophistication and provide a pleasant user experience.

### Typography

- The main font used in this project is **Robotto**. I think that's a well designed and easy to read font. An extra reason for using this font is the excellent display on small screens.
- In the main titles of the site, the font **Poppins** was used, which also has a good design and combines nicely with the main font.


### Colours

- In the colour scheme, I used shades that favoured the easy visualization of the information.
- In the navbar and footer, I used the white background with letters in a dark grey tone, giving a greater contrast for logo information and menu options. As well as a light shadow in the division with the Body.
- In the background, I used an image of the wooden floor with a slight change in opacity to make it a little lighter.
- In the boxes for adding and editing properties, login and user registration, a title with a dark grey background with white letters was used to give greater contrast.
- The buttons have a dark tone with white letters and black borders, making an interesting effect.
- Some images with white dolls were used in the user's standard photo and when the user has not yet included an ad.

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

### Base

All pages have the navigation bar with the logo and all visible links and footer.

* **Unregistered user**
<div align="center">
<img src="https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/static/img/Readme/visitor.png" target="_blank" rel="noopener" alt="Swift Estates">
</div>
If the access is made by an unregistered user it will be able to view the main page with both carousels with the latest ads registered for sale and for rent. this visitor can also access the link to view all ads registered on the platform.
The user registration and login link will also be visible to the visitor.

* **Registered user**
<div align="center">
<img src="https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/static/img/Readme/logged_user.png" target="_blank" rel="noopener" alt="Swift Estates">
</div>
A logged-in agent will have access links to add a new property, my ads, profile and a logout button available.

### Register a new agent
<div align="center">
<img src="https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/static/img/Readme/register.png" target="_blank" rel="noopener" alt="Swift Estates">
</div>

When accessing the registration screen, the agent has to choose the username and password for the platform.
Some checks are made on the database before the new inclusion, as if the username already exists in the database, if so, an error message is displayed.
It is also necessary that the username and password have more than 5 alphanumeric characters.

### Agent Login
<div align="center">
<img src="https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/static/img/Readme/login.png" target="_blank" rel="noopener" alt="Swift Estates">
</div>
### Agent Profile
<div align="center">
<img src="https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/static/img/Readme/profile.png" target="_blank" rel="noopener" alt="Swift Estates">
</div>
#### Update Photo
<div align="center">
<img src="https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/static/img/Readme/update_photo.png" target="_blank" rel="noopener" alt="Swift Estates">
</div>
#### Update Password
<div align="center">
<img src="https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/static/img/Readme/change_password.png" target="_blank" rel="noopener" alt="Swift Estates">
</div>
#### Delete Account
<div align="center">
<img src="https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/static/img/Readme/delete_account.png" target="_blank" rel="noopener" alt="Swift Estates">
</div>
### Listing ads
<div align="center">
<img src="https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/static/img/Readme/property_list.png" target="_blank" rel="noopener" alt="Swift Estates">
</div>
### Add a new property
<div align="center">
<img src="https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/static/img/Readme/add_new_property.png" target="_blank" rel="noopener" alt="Swift Estates">
</div>
### Update a property
<div align="center">
<img src="https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/static/img/Readme/edit_property.png" target="_blank" rel="noopener" alt="Swift Estates">
</div>
### Delete a property

### My ads

### Error Page
<div align="center">
<img src="https://raw.githubusercontent.com/rodrigoneumann/third-milestone-project/master/semgmtapp/static/img/Readme/error.png" target="_blank" rel="noopener" alt="Swift Estates">
</div>
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
  - [Am I Responsive](http://ami.responsivedesign.is/)
      - Used to get images for the README in different screen sizes. 
  
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

#### Validators
- HTML

  - [The W3C Markup Validation Service](https://validator.w3.org/)

- CSS

  - [The W3C Markup Validation Service](https://jigsaw.w3.org/css-validator)

- JavaScript

  - [JS Hint](https://jshint.com/)

- Python
  - [PEP8](http://pep8online.com/) - The Python scripts were checked with pep8online. almost all the errors were solved, the only ones that persisted were of lines longer than 79 characters in some cases, however, in most cases they are in MongoDB query lines.

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

You will need the following tools installed on your system:

- [Python 3](https://www.python.org/downloads/)
- An IDE such as [Visual Studio Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/download/)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) 
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

## Local Deployment
The following instructions are based on use on a Windows 10 OS and IDE VS Code. If your OS is different, the commands may be different, but the process, in general, remains the same.

#### Instructions

- Save a copy of the Github repository located at https://github.com/rodrigoneumann/third-milestone-project.
  - Unzip the repo into the chosen folder.
- If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/rodrigoneumann/third-milestone-project
```

- Within the chosen directory, create a virtual environment with the command:
```
python -m venv venv
```  

- Activate the virtual environment with the command:
```
.\venv\bin\activate 
```

- Install all required modules with the command: 
```
pip install -r requirements.txt
```

- Create a file called `.flaskenv` if not exists.

- Inside the `.flaskenv` file check for the following entries:
```
FLASK_ENV=development
FLASK_APP=app.py
```

- Create a `.env` file with your credentials:
e.g
```
MONGO_URI="insert your mongo URI details here"
SECRET_KEY="insert your secret key here"
```

- Create a database in MongoDB Atlas called **semgmtapp** with a collection called **users**

- Run the application with the command
```
flask run
```
- Open the website at `http://127.0.0.1:5000`

## Remote Deployment

#### Instructions
To deploy this app to Heroku you need to follow the steps below:

- Create a **requirements.txt** file so that Heroku can install all the dependencies required to run the app.
  `pip freeze > requirements.txt`

- Create a **Procfile** with the command:
  `echo web: python app.py > Procfile`

- In this step, you have to create a free account on the [Heroku website](https://signup.heroku.com/).
-  Login to the account, click on new and then create a new app. In the following screen, you need to give a name and choose the Europe region.
-  In the menu access the **Deploy** option, after that click on Connect to Github. Just below provide the information from the app's repository on GitHub and select the option Enable Automatic Deploy.
- On the Dashboard of the APP, click on Settings and then click on the option **Reveal config Vars**.
- Now you need to add the following variables to **Reveal config Vars**:
  - **IP**: `0.0.0.0`
  - **PORT**: `5000`
  - **MONGO_URI**: `link to your Mongo DB`
  - **SECRET_KEY**: `your chosen secret key`
- You are now ready to access the deployed app on Heroku.

# Credits

## Content
Most of the texts of this project were written by me.
Only the description of the properties in the ads was copied from other estate ads **for example only**.

## Media
#### Images
The logo vector was inspired in this [Logo](http://www.eatlogos.com/building_logos/building_free_logos_download.php?eatlogos=vector_construction_house_logo&le_id=432) and changed for my needs.
- The images in this project were sourced from [Pixabay](http://www.pixabay.com):
  - **House** and **building** images for the banner was sourced from [rachelmatthews7](https://pixabay.com/pt/users/rachelmatthews7-1955936/) profile.
  - **House Icon** for the favicon was sourced from [Clker-Free-Vector-Images](https://pixabay.com/pt/vectors/casa-home-s%C3%ADmbolo-em-branco-305683/) profile.
  - The **white** character on the My_ads when there are no ads in profile and no photo in profile was sourced from [Peggy_Marco](https://pixabay.com/pt/users/peggy_marco-1553824/) profile.
  - **No photo** ad image was sourced from: [OpenClipart-Vectors](https://pixabay.com/vectors/house-home-real-estate-architecture-2026116/) profile
  - The "wood floor" used in background image was sourced from [Pexels](https://pixabay.com/photos/floor-wood-parquet-wooden-brown-1846849/) profile.
  - The **Red house Icon** used in the carousel when no ads were sourced from [OpenClipart-Vectors](https://pixabay.com/vectors/real-estate-estate-home-house-155524/) profile.
  - The main **banner image* for the README was sourced by [www.pixeden.com](https://www.pixeden.com/free-design-web-resources).
- Images for the **properties** that were added by me was sourced by Pixabay as well, but other users can provide different sources for its ads.

### Code
- The code for the carousel on the main page was used directly from the [Bootstrap](https://getbootstrap.com/docs/4.0/components/carousel/) library.
- Flask architecture design based on blueprints learned and understanding ideas from here. [CodeShow](https://www.youtube.com/watch?v=-qWySnuoaTM&t=5706s) 
- The code for adding the correct prefixes to CSS was created using [AutoPrefixer](https://autoprefixer.github.io/).

## Acknowledgements
Very Special Thanks to:
- My mentor in Code Institute **Sandeep Aggarwal** who had all the patience to explain and make me understand certain concepts and peculiarities of the project content.
- All people, including family, friends, and colleagues who have tested the platform on their real devices, reporting to me about any usability issues and giving improvement tips to improve the usability.
- To all of the Code Institute Slack community for the help in my issues and review to my project code.