# Title

The live website can be viewed [here]()      
<img src="" alt="mockup" target="_blank" rel="noopener" width="850">

****************ADDDDDDDDDDD small ad


---


## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
3. [**Information Architecture**](#information-architecture)
    - [**Database Choice**](#database-choice)
    - [**Data Modelling**](#data-modelling)

4. [**Technologies Used**](#technologies-used)
    - [**Languages**](#languages)
    - [**Libraries and Frameworks**](#libraries-and-frameworks)
    - [**Tools**](#tools)
    - [**Databases**](#databases)

5. [**Testing**](#testing)
6. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Heroku Deployment**](#heroku-deployment)

7. [**Credits**](#credits)
    - [**Code**](#code)
    - [**Content and Media**](#content-and-media)
    - [**Acknowledgements**](#acknowledgements)
8. [**Disclaimer**](#disclaimer)

---

## UX

### Project Goals
#### Target Audience
- 
- 
- 
- 
-    

#### Visitor/user goals:
- 
- 
- 

#### Business goals(site owner's goals):
- 
- 
- 

### User Stories    
#### Common user stories (guests, new users and authenticated users)
- As a user, I expect
- As a user, I expect
- As a user, I want 
- As a user, I want to 
- As a user, I want to 
- As a user, I want to 
- As a user, I want to  

#### New Users
- As a user, I want to 
- As a user, I want to 

#### Returning users
- As a user, I want to 
- As a user, I want to 
- As a user, I want to 

#### Website Owner(admin)
- As a user, I want to 
- As a user, I want to 

### Design
#### Framework
- [Bootstrap](https://www.bootstrapcdn.com/), front-end framework is chosen for this project for its modern interface, ease of use and ability to be easily customized. It is used for creating features such as navbar, cards, forms, modals, as well as for the layout.
- 

#### Colour Scheme

![Color Palette]()
#### Typography
There are three fonts used across the project that I find a good combination: 
- [Roboto](https://fonts.google.com/specimen/Roboto) used as the main body font, Roboto has a dual nature. It has a mechanical and geometric look with friendly and open curves. With a clean look complements perfectly the fonts used as logo and headings.
- [Dancing Script](https://fonts.google.com/specimen/Dancing+Script) - Used in heading in mashead section of homepage, recreating a fell for handwriting font.  
- [Exo](https://fonts.google.com/specimen/Exo) - elegant, versatile and clean, complements well with Roboto font and balances Dancing script irregularities, used for headings.

#### Icons
Icons are used widely, as they are a good tool to improve the user experience. They convey instant methaphorical meaning and they are conventionally accepted worldwide. •••***===

### Wireframes
[Balsamiq Wireframes](https://balsamiq.com/) tool was used to create all wireframes for the project.   

Original wireframes for desktop, tablet and mobile can be found [here]().


**Note:** The website was changed and evolved through the development process and several improvements were applied.
The wireframes served as guidelines but some details such as positioning, placement of 
 images, buttons and other refinements diverge from the original wireframes.    
 Apart from that, there are some features that are included into original wireframes (such as reviews, social account login, user's avatar, image galleries for services/products), 
 but were considered of secondary importance and were not implemented yet due to time constraints. This is reflected and described in details in [Features left to implement](#features-left-to-implement) section, and I intend to come back to them and implement them in future when I can dedicate more time to it.


<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---

## Features
SandrArt website is composed by .............. applications: `.....`, `.......`.

### Existing Features     
#### Navbar
The navbar is fixed at the top of the page all the time, this allows a user to easily navigate throughout the website.
 The **logo** is located in the top left corner on a desktop and in the center on the smaller devices. 
 ......    
 
Navbar also contains ........   

#### Footer
Footer consists of 2 parts: main footer section and additional footer section which is displayed only on the large screens.   

Main footer section is stuck to the bottom of the page and displayed across all the screens. It contains ....

#### Home page
The Home page serves to attract .... x sections:
- **Masthead** section contains a ....
- **Gallery** section  contains .....
- **...**  section  contains .....  
- **...** section ...  
- **...**  section  contains .....  
- **...** section ...

#### About page
The page provides a user information about ....    

#### ... page
This page represents 

#### ... page
This page represents

#### ... page
This page represents

### Features Left to Implement
There are some features that I considered 
#### ....
This will be the first priority feature I would like to implement in future. Users would be able ...
#### ....
This feature would allow users to ...
#### ....
This feature allows users to ...


<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>


---
## Information Architecture
### Database choice
During the development phase I worked with **sqlite3** database which is installed with Django.   
For deployment(production), a **PostgreSQL** database is provided by Heroku as an add-on.
- The **User model** used in this project is provided by Django as a part of defaults `django.contrib.auth.models`. More information about Django’s authentication system can be found [here](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/).

### Data Modelling
#### Profile App
##### Profile


#### Products
##### Product


##### Collection
 


#### Checkout App
##### Order


##### Order Item Details 


<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---

## Technologies Used

### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/) 
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) - templating language for Python, to display back-end data in HTML.

### Libraries and Frameworks
- [Django](https://www.djangoproject.com/) - Python framework for building the project.
- [Bootstrap 5](https://www.bootstrapcdn.com/) - as the front-end framework for layout and design.
- [Google Fonts](https://fonts.google.com/) - to import fonts.
- [FontAwesome](https://fontawesome.com/) - to provide icons used across the project. 
- [JQuery](https://jquery.com/) - to simplify DOM manipulation and to initialize Bootstrap functions.
- [Gunicorn](https://pypi.org/project/gunicorn/) - a Python WSGI HTTP Server to enable deployment to Heroku.
- [Psycopg2](https://pypi.org/project/psycopg2/) - to enable the PostgreSQL database to function with Django.
- [Stripe](https://stripe.com/ie) - to handle financial transactions.

### Tools
- [GitPod](https://www.gitpod.io/) - an online IDE for developing this project.
- [Git](https://git-scm.com/) - for version control.
- [GitHub](https://git-scm.com/) - for remotely storing project's code.
- [PIP](https://pip.pypa.io/en/stable/installing/) - for installation of necessary tools.
- [Heroku](https://heroku.com/) - to host the project.
- [Balsamiq](https://balsamiq.com/) - to create wireframes.
- [AWS S3 Bucket](https://aws.amazon.com/) -  to store static and media files in prodcution.
- [cloudinary](https://cloudinary.com/) - to store images and obtain images urls.
- [tinypng](https://tinypng.com/) - to compress image sizes.
- [tradegecko.com](https://www.tradegecko.com/sku-generator-download) - to generate SKU number.
- [Adobe Color](https://color.adobe.com/) - to extract colour scheme and create palete used in the README.

### Databases
- [SQlite3](https://www.sqlite.org/index.html) - a development database.
- [PostgreSQL](https://www.postgresql.org/) - a production database.

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---
## Testing
Testing information can be found in a separate [TESTING.md]() file

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---

## Deployment
The Sandr@rt project was developed using the [GitPod](https://www.gitpod.io/) online IDE and
using Git & GitHub for version control. It is hosted on the [Heroku](https://heroku.com/) platform, with static files on WhiteNoise and user-uploaded images being hosted in AWS S3 Basket.
### Local Deployment

#### Directions
1. You can clone .....

2. ...

### Heroku Deployment
##### Hosting media files with AWS

##### Senging email via Gmail

##### Google Maps API key set up

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---

## Credits
### Code
- The project's code was developed by following the [Code Institute](https://codeinstitute.net/) video lessons and based on the understanding of the Boutique Ado Django Mini-Project, but was customized, modified and enhanced to fit the project purposes.
- README page structure and project inflormation architecture was inspired in the excellent milestone projects of code institute graduate [Irina](https://github.com/irinatu17) as I searched for inspiration and examples of milestone projects that had fullfilled milestone requirements in order to better understand my work flaws.

### Content and Media
- 

### Acknowledgements
I would like to thank everyone who has helped me throughout the development of this project:      
- **My mentor** []() for ....        
- ......... and other **Code Institute tutors** for their help to debug issues, assistance and support.    
- Many thanks to my fellow students, **Slack community** for help and support and my **family** for the pacient and support.        

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---

## Disclaimer
This site is made for **educational purposes** however it is intended to use it as a **business platform** in near future.        


<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>


##  Credits
-  Used bootstrap theme [agency](https://startbootstrap.com/theme/agency) to inspire me in for homepage structure
-   Used previous work and as templates to write README page and [taste world snacks](https://github.com/ceciliabinck/taste-world-snacks.git) deployment as guidance to write up my deployment
-   I have copied and pasted small pieces of work from my first attempt at this project, in the repository [sl_art](https://github.com/veraleitaodev/sl_art/) and [sandra_art](https://github.com/veraleitaodev/sandra_art/) as these were my first attempts to fullfil my milestone project, I have changed project as it was limiting me on the number of skills I could demonstrate.  
In insight, I will improve UX planning before implementing the project to verify it meets all requirements.
-  Logo created and puchased from [wix.com](https://www.wix.com/logo/maker)
-  css gradient code from [cssportal.com](https://www.cssportal.com/css-text-gradient-generator/)
- help in understanding how to use django in a carousel https://stackoverflow.com/questions/30119351/how-to-make-an-object-slider-in-django
- logo - Wix
- blog content - https://kripalu.org/about/kripalu/faculty/sat-bir-s-khalsa
-https://stackoverflow.com/questions/30864011/display-only-some-of-the-page-numbers-by-django-pagination