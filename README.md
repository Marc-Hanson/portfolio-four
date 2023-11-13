# **Bewdley Spirits**

Bewdley Spirits is a full-stack project built to display products and upcoming events for the company of the same name. It has CRUD functionality for registered users, and a username and password ensures data privacy, email authentication is not yet enabled.  The user authentication system chosen for this project was the django-allauth plugin, as Django is the framework I used to build the app.

The project was designed with a MVP project plan to keep the different aspects of it managable. I used an Agile orientated approach to developing the product and my kanban board can be found in my repo as an attached GitHub project called 'Bewdley Spirits'.

The deployed site can be visited by clicking [**here**](https://portfolio-four-de53c67a8b9a.herokuapp.com/).

The site code can be viewed in this [**GitHub Repository**](https://github.com/Marc-Hanson/portfolio-four).

I designed the app for submission as my 'Portfolio Project 4', part of the [**Code Institute Fullstack Software Development Diploma**](https://codeinstitute.net/ie/full-stack-software-development-diploma/). The aim of this project is to build a full-stack site based on business-oriented logic, used to control a centrally-owned dataset. A requirement is to set up an authentication mechanism and provide role-based access to the site's data, and for the site to be fully deployed for public use. The required technologies for the project are:

- HTML, CSS, JavaScript(not compulsory), Python + Django
- A relational database (recommending MySQL or PostgreSQL)

PostgreSQL was used as my database management system, via ElephantSQL, to install and manage the SQL database. Heroku was used to deploy the project, and GitHub for version control.

## **Table of Contents**

- [**Bewdley Spirits**](#bewdley-spirits)
  - [**Table of Contents**](#table-of-contents)
  - [**User Experience**](#user-experience)
  - [**User Stories**](#user-stories)
  - [**Design and Scope**](#design-and-scope)
    - [*Agile Approach*](#agile-approach)
    - [*Wireframes*](#wireframes)
    - [*Database Schema*](#database-schema)
    - [*UI Design Changes*](#ui-design-changes)
  - [**Features**](#features)
    - [*Existing Features*](#existing-features)
    - [*Security Features and Admin Functionality*](#security-features-and-admin-functionality)
    - [*User Authentication*](#user-authentication)
    - [*Database Security*](#database-security)
    - [*Admin Access*](#admin-access)
    - [*Future Features*](#future-features)
  - [**Testing**](#testing)
    - [*Automated Testing*](#automated-testing)
    - [*Manual Testing*](#manual-testing)
    - [*Validator Testing*](#validator-testing)
  - [**Technologies Used**](#technologies-used)
    - [*Main Languages Used*](#main-languages-used)
    - [*Frameworks, Libraries \& Programs Used*](#frameworks-libraries--programs-used)
    - [*Installed Packages*](#installed-packages)
  - [**Deployment**](#deployment)
  - [**Acknowledgements and Credits**](#acknowledgements-and-credits)

## **User Experience**

Bewdley Spirits is a real life company based in Bewdley, Worcestershire. The site was designed around their logo and kept to a grey scale, simple black and white design to keep contrast and readability high and a uniform look
across the site. Shades of blue were used to accent important areas of the site, such as reviews and upcoming events as well as hover states on clickable text. The navigation bar consists of the same logo and links for logging in and logging out as well as viewing products and the storefront. The app was designed with a desktop-first approach but is easily and elegantly scaled down for tablet and mobile devices using inline Tailwind CSS.

![amiresponsive](/static/images/readme/responsive.png)

## **User Stories**

There were three user types used when designing the app: admin (with backend access to add events/products and approve reviews), visitors, and all other users who register to use the app. The general user provides a username and password to access their data, and this also protects the privacy of their data.
The following user stories were created for all three types of user.

1* As an **Administrator**, I want to **be able to create events** so that **visitors to the site know of in-person shows**.

2* As an **Administrator**, I want **created events to strikeout and delete after expiration** so that **users can see recent events but not long passed ones**.

3* As an **Administrator**, I want **to be able to control user reviews** so that **people don't leave advertising or other items on my review page**.

4* As an **Administrator**, I want **a page to display our products** so that **visitors can see what we sell**.

5* As an **Administrator**, I want **a custom storefront** so that **user stay engaged on our site for longer**.

6* As an **Administrator**, I want **users to join a mailing list** so that **news and offers can be sent to them directly**.

7* As a **visitor**, I want **to be able to see reviews** so that **I know the page and products are reputable**.

8* As a **visitor**, I want **to view available products** so that **I know more about the business**.

9* As a **visitor**, I want **to be able to signup for an account** so that **I can leave a review and sign up for news**.

10* As a **visitor**, I want **access to a chatbot** so that **customer support is offered 24/7**.

11* As a **registered user**, I want **to be able to leave a review** so that **the business and other visitors know my opinion of the product**.

12* As a **registered user**, I want **to be able to edit or delete my review** so that **my most recent experience can be portrayed**.

13* As a **registered user**, I want **access to a members area** so that **users can share ways to use the product and build a community**.

14* As a **registered user**, I want **to be able to join a mailing list** so that **the latest news and offers are sent directly to my inbox**.

## **Design and Scope**

The scope of the project was to build a MVP with as extras as possible, if time permitted, and the user stories were used as a guide for this.

### *Agile Approach*

Each of the fourteen user stories were written as "issues" in Github and mapped to a Kanban Board ("Bewdley Spirits" attached as a Github project in my repository). The user stories labelled  "must have" for the MVP were completed within my first iteration, so that by the end of the first Agile sprint, a workable app with CRUD functionality had been produced. The user stories labelled "should have" were completed after the 'must have' functionalities were in place, and 'could have' user stoies are planned for the next iteration of this app. The "won't have" user story tasks are planned for later completion as they are currently beyond my scope, this project will be ongoing as it is for use outside of my Code Institute Diploma.

This project was time-managed by setting due-dates for each user story and allowing extra time for unforseen issues and experimenting. Both Code Institute blog projects were used as rough time frames as to how long each part of my page would take.

### *Wireframes*

The basic wireframes are available as five PNG files; the first which shows the initial landing page and header, which is the first page that loads on the site.

![wireframe top of page](/static/images/readme/wireframe-header.png)

This 40% width and centered content was kept uniform for each section of the site, with the company logo and social links in a simple footer.

![wireframe bottom of page](/static/images/readme/wireframe-footer.png)

A central box containing all page content would be used for login / logout/ signup and page errors.

![wireframe information pages](/static/images/readme/wireframe-information.png)

Reviews would be displayed in a carousel style, with 2 reviews side by side per page.

![wireframe reviews](/static/images/readme/wireframe-reviews.png)

And a products page would feature 2 products side by side with the product name above and information below a bightly coloured image.

![wireframe products](/static/images/readme/wireframe-products.png)

### *Database Schema*

I created the simplest possible database schema for my app, and the corresponding entity relationship diagram below was drawn using QuickDatabaseDiagrams based around the classes to be used. Beyond the units employed from Django, all models (in models.py) were created from scratch and cover reviews being created, read, updated and deleted as well as two classes just for admin use to display information on the page. I used class-based views, as taught in the Code Institute lessons on creating the blog "I think therefore I blog" (in views.py).

![database schema](/static/images/readme/database-schema.png)

As everything in this project was original and custom, writing both the models and views was a learning experience and many changes were made as I got to grasp with Djangos MVT architecture.

### *UI Design Changes*

Initially the site was planned to use the colour palette from the companies labels. But very early on this was scrapped as the site felt messy and unclear. The black and white company logo was used as a fixed background along with a black and white header/footer. A blue hover state was later added to match other blue elements used on the app. I felt that using the logo as a wallpaper would help build the brand and tried to use a simplified version of this logo when ever possible.

All artwork used was created by my brother and permssion was given for all of it's use.

![header feedback](/static/images/readme/readme-feedback.png)

After my midway meeting with my mentor a Feedback button was introduced to the navbar for registered users, this was linked to the review form to allow people to find it easier.

## **Features**

There are three main pages to the Bewdley Spirits app, each with the "base" header and footer added. The"about" page appears altered with extra information on it for users that are logged in, which then shows the "form" page inside the "about" page. Or for users that have left a review, being shown a link to the "review" page in place of the "form". There are a number of features I would like to add in future to improve the app beyond the MVP level.

### *Existing Features*

Header and Footer are both rendered from the base HTML file.
![header](/static/images/readme/readme-header.png)
![footer](/static/images/readme/readme-footer.png)

List of pages to the site:

- The 'Home' Page which provides an introduction, displays upcoming events, and information about the companies products and services. Along with a link to an external storefront.
![landing page](/static/images/readme/readme-landing.png)
![upcoming events](/static/images/readme/readme-events.png)
  
- The 'Products' page to display products that the company makes.These have been added to the database by an admin.
![products](/static/images/readme/readme-products.png)
  
- About Us, this page has been broken in to several html files to make the code more verbose. The "carousel.html" is displayed and contains approved reviews from users, paginated by 2 with navigation buttons. If the user has already left a review a button is displayed to send the user to the "your_review.html" page where their review can be updated(this then requires the review to be approved again) or deleted. Or if the user has no review it displays a custom form from the "form.html" that allows the user to create a review before approval.
![about](/static/images/readme/readme-about.png)  
![reviews](/static/images/readme/readme-review.png)  
![form](/static/images/readme/readme-form.png)  
![button](/static/images/readme/readme-button.png)  

**The login status of the user is reflected in the data available to the user on their navigation journey. If a user is logged in, the nav bar will display the 'Feeback' and 'Logout' links. If the user is logged out, These links are replaced by 'Register' and 'Login'. Data from the review left by a user is only available via the account that created the data, with the exception of the admin superuser who has access to the backend of the site.**

The favicon used in this site is also custom built, converted from the 'ghost.webp' image file provided in this project.

### *Security Features and Admin Functionality*

### *User Authentication*

I have used Djangos allauth to manage user access based on permissions. Where the user isn't passing authentication due to an incorrect password and username, login is refused.

### *Database Security*

The Database URL, Cloudinary URL and Secret Key are stored in my env.py file so that no unwarranted access to the database is possible. My custom forms are only visible to users that are logged in, and all input is decured using Cross-Site Request Forgery (CSRF) Tokens.

### *Admin Access*

Django comes with admin control functionality, and the control panel is easy to use. It can be accessed for my app [**here**](https://portfolio-four-de53c67a8b9a.herokuapp.com/admin/login/?next=/admin/)
There are options here to view content, add events to the index page, add products to the product page, manage user permissions, and approve or reject reviews left by users.

### *Future Features*

Proposed future features:

1. Adding a mailing list is the easiest to complete of my issues, most of the groundwork has been done already.

2. A small members forum page for user to dicuss the products and how they enjoy them most.

3. AI chat bot to provide FAQ answers and customer support.

4. A custom storefront for the site to remove the need for an external store link.

## **Testing**

### *Automated Testing*

I gave myself extra time during this project to play with automated testing and to try to develop a greater understanding. Because of this I have written tests for the apps 'urls.py', testing both the class based views and function based views resolve correctly. The apps 'models.py' was also tested using a setUp function with mock data to test that both of the admin models for creating events and products accepted data. As well as the user accessible review function was taking data and creating reviews as intended.
When testing the apps 'views.py' the only checks done were that the pages loaded the correct template and that the server code was 200 for every page. Due to
IDE issues over 9-11 November I ran short of time testing form inputs and custom error page handling. These were tested manually but no automated tests were created at this time.
Ideally the app would have used a 'forms.py' to allow for form testing but all forms used in this project were rendered from a html template.

### *Manual Testing*

This was my first full stack pooject and as such I spent as much time playing with code as possible, testing how files work and how MVT projects files interact with each other. Everything in this project was built from scratch with a lot of trial and error, as such there were thousands of problems and fixes that were implemented along the way, the greatest of which are documented here. But as a learning experience I allowed myself to make many, many errors and to always try to fix the problem alone before searching for help on StackOverflow or the CodeInstitute slack channel.

- base.html all navigation links work.
- base.html all external links in footer work correctly.
- index.html upcoming events all display correctly.
- index.html external links were all tested and open correctly.
- index.html shop button working and opens external link.
- products.html all images display correctly and have alt text.
- products.html shop button working and opens external link.
- about.html displays reviews correctly.
- about.html displays feedback section only to signed in users.
- about.html form elements all working as expected.
- you_review.html update and delete buttons working as expected.

- Form
This projects form was the biggest challenge I encountered during development. I chose to use a seperate html document for the form to make the code more verbose and allow me to syle all of it's components with tailwind to keep a uniform look across the site. I wanted reviews to be unique for users to keep the review area uncluttered, and to provide easy access for a user to their review for editing/updating. Seperate urls were created for users leaving their first review, updatng a current review or deleting their review. This solution isn't ideal and it's something I would like to change in the future, migrating the form to forms.py and refactoring the functions for leaving reviews. The form was tested, working and submitted for the first ireration of the app.

- Images not displaying after deployment.
After a deployment to Heroku my static image files were no longer displaying, after searching through Code Institutes Slack channels I found that several others had experienced the same issue. The easiest way to fix this was to change the 'background url' link in my html template and to set the background instead in my style.css file and use my cloudinary link. The image inside the footer was also fixed by using the cloudinary image instead of locally hosted files.

- Using temporary local databases for testing.
During automated testing I received the following error, "Creating test database for alias 'default'... Got an error creating the test database: permission denied to create database". This was caused by my database variables being defined in the apps env.py file and then changed in the apps settings.py. After searching through StackOverflow the easiest solution was to comment out the 'DATABSE_URL' inside the apps env.py file during testing to allow a temporary local database to be created, used and deleted. This line of code was uncommented again once testing had concluded.

### *Validator Testing*

- HTML files were passed through W3 Validation with no errors found.
![html_validation](/static/images/readme/html-w3.png)
- CSS files were passed through W3 Validation with no errors found.
![css_validation](/static/images/readme/css-w3.png)
- .py files were passed through Code Institutes Python Linter.
![python_validation](/static/images/readme/python-linter.png)
-Lighthouse was also used to check the websites accessability.
![lighthouse](/static/images/readme/lighthouse.png)
The greatest issues caught by Lighthouse was deployment through Heroku.
![lighthouse_error](/static/images/readme/lighthouse-error.png)

## **Technologies Used**

### *Main Languages Used*

- HTML
- CSS
- Javascript
- Python
- Django
- PostgreSQL

### *Frameworks, Libraries & Programs Used*

- Google Fonts - for the font families.
- Font Awesome - to add icons to the social links in the footer element.
- CodeAnywhere - to create my html files & styling sheet before pushing the project to Github.
- GitHub - to store my repository for submission.
- Wireframe.cc - were used to create mockups of the project prior to starting.
- Am I Responsive? - to ensure the project looked good across all devices.
- Favicon - to provide the code for the icon in the tab bar.
- Django
- Tailwind
- QuickDatabaseDiagrams

### *Installed Packages*

- django
- gunicorn
- dj_database_url
- psycopg2
- dj3-cloudinary-storage
- django-allauth

## **Deployment**

The site was deployed to Heroku. The steps to deploy are as follows:

- Install Django & Gunicorn:
```pip3 install django gunicorn```
- Install Django database & psycopg:
```pip3 install dj_database_url psycopg2```
- Install Cloudinary & Django-allauth:
```pip3 install dj3-cloudinary-storage django-allauth```
- Create the requirements.txt file with the following command:
```pip3 freeze --local > requirements.txt```
- Create a django project using:
```django-admin startproject **projectname**```
- Create an app with:
```python3 manage.py startapp **appname**```
- Add app to installed apps in settings.py file within our project directory.
- Migrate changes using:
```python3 manage.py migrate```
- Navigate to [Heroku](www.heroku.com) & create a new app.
- Navigate to the Settings Tab, to add the following key/value pairs to the configvars:
  1. [SECRET_KEY] = **random key**
  2. [PORT] = 8000
  3. [CLOUDINARY_URL] = **api environment variable**
  4. [DATABASE_URL] = **api environment variable**
- Create an env.py file and import os.
- Add the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the env.py file.
- Add the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the settings.py file.
- Add Heroku to the ALLOWED_HOSTS in settings.py.
- Create Procfile.
- Push the project to Github.
- Connect github account to Heroku through the Deploy tab.
- Connect github project repository, then click on the "Deploy" button.

## **Acknowledgements and Credits**

- The products, brands, names and artwork used in this site are all family owned and permission was gained before their use.
- StackOverflow was a source of many answers during development.
- CodeInstitutes slack channels were used for problem solving.
- Inspiration and knowledge was taken from the Code Institute 'I think Therefore I Blog' project.
- CSS templating and ideas from [**Tailwind Components**](https://tailwindcomponents.com/).
- [**Dumbfounds YouTube**](https://www.youtube.com/playlist?list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM) playlist on Django testing for extra help on automated testing.
