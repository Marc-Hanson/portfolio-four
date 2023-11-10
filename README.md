# **Bewdley Spirits**

Bewdley Spirits is a full-stack project built to display products and upcoming events for the company of the same name. It has CRUD functionality for registered users, and a username and password ensures data privacy. The user authentication system chosen for this project was the django-allauth plugin, as Django is the framework I used to build the app.

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
      - [Agile Approach](#agile-approach)
      - [Wireframes](#wireframes)
      - [Database Schema](#database-schema)
      - [UI Design Changes](#ui-design-changes)
  - [**Features**](#features)
    - [**Existing Features**](#existing-features)

## **User Experience**

Bewdley Spirits is a real life company based in Bewdley, Worcestershire. The site was designed around their logo and kept to a grey scale, simple black and white design to keep contrast and readability high and a uniform look
across the site. Shades of blue were used to accent important areas of the site, such as reviews and upcoming events as well as hover states on clickable text. The navigation bar consists of the same logo and links for logging in and logging out as well as viewing products and the storefront. The app was designed with a desktop-first approach but is easily and elegantly scaled down for tablet and mobile devices using inline Tailwind CSS.

![amiresponsive](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/wbyp5rxm7lswivovt2eg)

### **User Stories**

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

### **Design and Scope**

The scope of the project was to build a MVP with as extras as possible, if time permitted, and the user stories were used as a guide for this.

#### Agile Approach

Each of the fourteen user stories were written as "issues" in Github and mapped to a Kanban Board ("Bewdley Spirits" attached as a Github project in my repository). The user stories labelled  "must have" for the MVP were completed within my first iteration, so that by the end of the first Agile sprint, a workable app with CRUD functionality had been produced. The user stories labelled "should have" were completed after the 'must have' functionalities were in place, and 'could have' user stoies are planned for the next iteration of this app. The "won't have" user story tasks are planned for later completion as they are currently beyond my scope, this project will be ongoing as it is for use outside of my Code Institute Diploma.

This project was time-managed by setting due-dates for each user story and allowing extra time for unforseen issues and experimenting. Both Code Institute blog projects were used as rough time frames as to how long each part of my page would take.

#### Wireframes

The basic **wireframes** are available as five PNG files; the first which shows the initial landing page and header, which is the first page that loads on the site.

![wireframe top of page](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/wireframe-header.bd70d1dc122d)

This 40% width and centered content was kept uniform for each section of the site, with the company logo and social links in a simple footer.

![wireframe bottom of page](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/wireframe-footer.215df7e7fe2e)

A central box containing all page content would be used for login / logout/ signup and page errors.

![wireframe information pages](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/wireframe-information.0cd6eaa0a7c1)

Reviews would be displayed in a carousel style, with 2 reviews side by side per page.

![wireframe reviews](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/wireframe-reviews.ac0c19b4e758)

And a products page would feature 2 products side by side with the product name above and information below a bightly coloured image.

![wireframe products](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/wireframe-products.726b823c055c)

#### Database Schema

I created the simplest possible database schema for my app, and the corresponding entity relationship diagram below was drawn using QuickDatabaseDiagrams based around the classes to be used. Beyond the units employed from Django, all models (in models.py) were created from scratch and cover reviews being created, read, updated and deleted as well as two classes just for admin use to display information on the page. I used class-based views, as taught in the Code Institute lessons on creating the blog "I think therefore I blog" (in views.py).

![database schema](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/database-schema.03e07620b40)

As everything in this project was original and custom, writing both the models and views was a learning experience and many changes were made as I got to grasp with Djangos MVT architecture.

#### UI Design Changes

Initially the site was planned to use the colour palette from the companies labels. But very early on this was scrapped as the site felt messy and unclear. The black and white company logo was used as a fixed background along with a black and white header/footer. A blue hover state was later added to match other blue elements used on the app. I felt that using the logo as a wallpaper would help build the brand and tried to use a simplified version of this logo when ever possible.

All artwork used was created by my brother and permssion was given for all of it's use.

![header feedback](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/readme-feedback.619492f7e5bf)

After my midway meeting with my mentor a Feedback button was introduced to the navbar for registered users, this was linked to the review form to allow people to find it easier.

## **Features**

There are three main pages to the Bewdley Spirits app, each with the "base" header and footer added. The"about" page appears altered with extra information on it for users that are logged in, which then shows the "form" page inside the "about" page. Or for users that have left a review, being shown a link to the "review" page in place of the "form". There are a number of features I would like to add in future to improve the app beyond the MVP level.

### **Existing Features**

Header and Footer are both rendered from the base HTML file.
![header](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/readme-header.ccec96628d44)
![footer](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/readme-footer.b41ffec66660)

List of pages to the site:

1. Home Page, which provides an introduction, displays upcoming events, and information about the companies products and services. Along with a link to an external storefront.
![landing page](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/wbyp5rxm7lswivovt2eg)
![upcoming events](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/readme-events.29ee2c42dac2)

2. Products, to display products that the compant makes.These have been added to the database by an admin.
![products](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/rd0u4xr8mli80tfgxc1h)

3. About Us, this page has been broken in to several html files to make the code more verbose. The "carousel.html" is displayed and contains approved reviews from users, paginated by 2 with navigation buttons. If the user has already left a review a button is displayed to send the user to the "your_review.html" page where their review can be updated(this then requires the review to be approved again) or deleted. Or if the user has no review it displays a custom form from the "form.html" that allows the user to create a review before approval.

![about](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/readme-about.0dc79e09428a)
![reviews](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/readme-carousel.40f6e658d781)
![form](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/readme-form.8917cd993d44)
![button](https://res.cloudinary.com/dldkvvyrw/image/upload/f_auto,q_auto/v1/static/images/readme/readme-button.4ec1fc3da3db)

**The login status of the user is reflected in the data available to the user on their navigation journey. If a user is logged in, the nav bar will display the 'Feeback' and 'Logout' links. If the user is logged out, These links are replaced by 'Register' and 'Login'. Data from the review left by a user is only available via the account that created the data, with the exception of the admin superuser who has access to the backend of the site.**

The favicon used in this site is also custom built, converted from the 'ghost.webp' image file provided in this project.
