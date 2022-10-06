# **Review | Alliance**
Review | Alliance is a resource for finding more about albums and concerts by the artists that you love! The site offers top reviews of albums and concerts by both *Review | Alliance approved staff* and *Review | Alliance users*. To create a more interactive and lively site all visitors can create their own user to start writing reviews and comment on other reviewers content. All comments and reviews need approval by Review | Alliance staff members to secure a digital hangout where everyone can feel safe from abuse, inappropriate language, etc. The approvals are being made from an admin dashboard that only is accessed by staff members with the correct access status. From a visual point of view the site has a clean look that makes navigation easier for the users.

This fictional site was created for Portfolio Project #4 (Full-Stack Toolkit) - Diploma in Full Stack Software Development Diploma at the [Code Institute](https://www.codeinstitute.net).

[View live website here](https://project-portfolio-4.herokuapp.com/)

![Review | Alliance responsive design](readme/assets/images/responsive.png)

# Table of Content

* [**Project**](<#project>)
    * [Objective](<#objective>)
    * [Site Users Goal](<#site-users-goal>)
    * [Site Owners Goal](<#site-owners-goal>)
    * [Project Management](<#project-management>)

* [**User Experience (UX)**](<#user-experience-ux>)
    * [Wireframes](<#wireframes>)
    * [User Stories](<#user-stories>)
    * [Site Structure](<#site-structure>)
    * [Flow chart](<#flow-chart>)
    * [Data Model](<#data-model>)
    * [Design Choices](<#design-choices>)

* [**Features**](<#features>)
    * [List Collection](<#list-collection>)
    * [Search Item In Collection](<#search-item-in-collection>)
    * [Add Item To Collection](<#add-item-to-collection>)
    * [Edit Item In Collection](<#edit-item-in-collection>)
    * [Remove Item From Collection](<#remove-item-in-collection>)
    * [Sort Collection](<#sort-item-in-collection>)
    * [Show Total value of collection](<#show-total-value-of-collection>)

* [**Features Left To Implement**](<#features-left-to-implement>)

* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
    * [Frameworks, Librarys & Software](<#frameworks-libraries--software>)
    * [Python Packages](<#python-packages>)

* [**Testing**](<#testing>)
  * [Code Validation](<#code-validation>)
  * [Additional Testing](<#additional-testing>)
  * [Known Bugs](<#known-bugs>)
* [Deployment](<#deployment>)
* [Credits](<#credits>)
* [Acknowledgements](<#acknowledgements>)

# **Project**

## Objective
I absolutely love music, both listening to it at home but going to live concerts as well. Therefore I have decided to do a review site that is as authentic and useful as possible. I also want to demonstrate my knowledge within the area of HTML, CSS, JavaScript, Python and the Django Framework.

## Site Users Goal
The user of 'Record | Alliance' loves music, to interact with others and to contribute with their knowledge to like minded.

## Site Owners Goal
The goal of the site owner is to deliver a site where the users in an intuitive way can read about the latest albums and concerts and contribute with their own reviews.

## Project Management

### Trello & Github Board
I've been using the application [Trello](https://trello.com/) and the project board in GitHub to keep my project together. It has been working really well and has helped me structure up my work a lot. Trello was used on a more general plan and GitHub was used to plan and organize my user stories.

![Trello Image](readme/assets/images/trello.png)

![User Stories](readme/assets/images/user_stories.png)

[Back to top](<#table-of-content>)

### Database Schema
I have used a modelling tool called [Graph Models](https://django-extensions.readthedocs.io/en/latest/graph_models.html) to create the database schema. In short it shows the relationships between the different models in the database connected to the application. Graph Models exports a *.dot file which easily can be converted to a more 'easy to read' design with the help of the application [dreampuf](https://dreampuf.github.io/GraphvizOnline/).

<details><summary><b>Database Schema</b></summary>

![Database Schema](readme/assets/images/database_schema.png)
</details><br/>

# **User Experience (UX)**

## Wireframes
The wireframes for the site were created in the software [Balsamiq](https://balsamiq.com). The wireframes have been created for desktop, tablet and mobile devices. The text content wasn't finalized during the wireframe process. It's worth mentioning that there are some visual differences compared to the wireframes, the reason being design choices that was made during the creation process.

![Wireframes](to be updated)

## User Stories
Below the user stories for the project are listed to clarify why particular feature matters. These will then be tested and confirmed in the [Testing](<#testing>) section.

### Site User
|  | | |
|:-------:|:--------|:--------|
| As a Site User | I can view a list of the music reviews so that I can select one to read | &check; |
| As a Site User | I can view a list of the concert reviews so that I can select one to read | &check; |
| As a Site User | I can click on a specific review so that I can read it in detail | &check; |
| As a Site User | I can like and unlike a review so that it is possible for me to interact with the review | &check; |
| As a Site User | I can view the number of likes on each review so that I can see how popular a specific review is | &check; |
| As a Site User | I can contact Review Alliance in an easy way so that I can interact with them if I have a need for it | &check; |
| As a Site User | I can navigate easy on the site through paginated list of posts so that I feel comfortable using the site | &check; |
| As a Site User | I can view comments on a specific review so that I can read the conversations between different users on the site | &check; |
| As a Site User | I can sign up an account so that I can like and comment on reviews, create a profile page, create own reviews and edit / remove my reviews | &check; |
| As a Site User | I can create a profile page so that other reviewers can read about who I am | &cross; |
| As a Site User | I can comment on a review so that I can be involved in the conversation | &check; |
| As a Site User | I can edit my comment so that I can change the content if needed | &check; |
| As a Site User | I can remove my review so that I have full control of my reviews | &check; |
| As a Site User | I can choose to see my own reviews so that I can find them easily | &check; |
| As a Site User | I can create a new review so that I can contribute to with new content to Review Alliance | &check; |
| As a Site User | I can log out from the site so that I can feel safe that nobody can access my information | &check; |
| As a Site User | I can create draft reviews so that I can finish writing the content later | &check; |
| As a Site User | I can get visual feedback when interacting with the content so that I can be sure how I have interacted with the page | &check; |

### Site Admin

|  | | |
|:-------:|:--------|:--------|
| As a Site Admin | I can log out from the site so that I can feel safe that nobody can access my information | &check; |
| As a Site Admin | I can create, read, update and delete reviews so that I can manage my review content | &check; |
| As a Site Admin | I can approve reviews so that I can secure high quality of the content | &check; |
| As a Site Admin | I can approve and disapprove comments so that I can secure a safe environment for the Site Users | &check; |
| As a Site Admin | I can create draft reviews so that I can finish writing the content later | &check; |
| As a Site Admin | I can access an admin area so that I can get a general understanding of logged in users, number of likes and number of posts | &check; |
| As a Site Admin | I can get visual feedback when interacting with the content so that I can be sure how I have interacted with the page | &check; |

[Back to top](<#table-of-content>)

## Site Structure

The Review | Alliance site is split up in two parts: **when the user is logged out** and **when the user is logged in**. Dependeing on login status different pages is available for the user. When the user is logged out the pages: *about*, *all*, *albums*, *concerts* are avaliable. When the user is logged in *about*, *all*, *albums*, *concerts*, *create review*, *view my reviews* and *show profile page* are available. If you are logged in as an administratorThe site has an minimalistic, clean and intuitive design that makes the site easy to navigate for the user.

Read more about the different choices in the [Features](<#features>) section.

[Back to top](<#table-of-content>)

## Design Choices

* ### Color Scheme

The color scheme chosen for the 'Review | Alliance' site was based on the Bootstrap dark background. The colors are Black (used on some text elements), Raisin Black (top navigation and footer), Rocket Metallic (used on most of the text elements), Cultured (body background) and White (used i.e. as card background). All colors are very clean and they create a professional look together and offers a good readability and contrast as well. I used the online service [Coolors](https://coolors.co/) to choose the color scheme.

![Color Palette image](readme/assets/images/coolors_palette.png)

* ### Typography
The fonts used for the game are 'Roboto' and 'Tinos'. Fallback font for both of them is sans-serif.

* 'Roboto' is used on all headlines including the brand logo. It's a very clean font that works really well for headlines and logos. It's easy to read and matches the minimalistic style that I wanted the site to 'breath'.

* 'Tinos' was chosen for the review excerpt and the review full text. It has a nice serif design and works really well for longer paragraphs of text.

![Google Fonts Impact](readme/assets/images/google_fonts_roboto.png)

![Google Fonts Tinos](readme/assets/images/google_fonts_tinos.png)

[Back to top](<#table-of-content>)

# **Features**
To be updated

## **Existing Features**

### **Navigation**
The navigation bar is very clean and straight forward. Depending if you  are logged in or not different menus is visible for the site user. An extra menu item is visible if you are logged in as an administrator.

*Links that are visible to logged out user*

* About - Includes information about Review | Alliance and presents the reviewers that are registered.
* All - Lists all reviews on the site independent of category type of review.
* Albums - Lists all album reviews.
* Concerts - Lists all concert reviews.
* Login / Sign Up - Gives the user the opportunity to log in or sign up if not ready a registered user at Review | Alliance.

<details><summary><b>Navigation Large - User Not Logged In</b></summary>

![Navigation Large - User Not Logged In](readme/assets/images/navbar_large_not_logged_in.png)
</details><br/>


<details><summary><b>Navigation Small - User Not Logged In</b></summary>

![Navigation Small - User Not Logged In](readme/assets/images/navbar_small_not_logged_in.png)
</details><br/>


*Links that are visible to logged in user*
All of the links that is visible to a not logged in user plus the ones below.

* Create New review - Lets the user create a new review.
* View My reviews - Lists all reviews created by the logged in user.
* Show Profile Page - Shows logged in users profile page.
* Log Out - Logs out the user.

<details><summary><b>Navigation Large - User Logged In</b></summary>

![Navigation Large - User Logged In](readme/assets/images/navbar_large_logged_in.png)
</details><br/>

<details><summary><b>Navigation Small - User Logged In</b></summary>

![Navigation Small - User Logged In](readme/assets/images/navbar_small_logged_in.png)
</details><br/>

*Link that is visible if user is administrator*
All of the links above plus the one below.
* Admin Area - Gives the administrator a view with information about i.e. total number of users, number of comments and number of posts. I this view the administrator also can publish / unpublish / approve / aunapprove reviews and approve / unapprove comments. The administrator can also remove / add genres in this view.

<details><summary><b>Navigation Large - Admin Logged In</b></summary>

![Navigation Large - Admin Logged In](readme/assets/images/navbar_large_admin_logged_in.png)
</details><br/>

<details><summary><b>Navigation Small - Admin Logged In</b></summary>

![Navigation Small - Admin Logged In](readme/assets/images/navbar_small_admin_logged_in.png)
</details><br/>

### **About**
In the about section the user can read about both who  Review | Alliance are but also about all reviewers that are registered on the site.

<details><summary><b>About Section - To be updated</b></summary>

![About](To be updated)
</details><br/>

### **All**
This page lists all the reviews that has been made at Review | Alliance. If the user is not logged in there is only a "read more" option visible for the user on each review card. If the user is logged in an *update* and *delete* option gets visible on the reviews that the user has written. The page shows 6 cards on bigger screens before a pagination mechanism kicks in. On smaller screens the cards are stacked vertically.

<details><summary><b>All Reviews - User Logged Out</b></summary>

![All Reviews - User Logged Out](readme/assets/images/all_reviews_logged_out.png)
</details><br/>

<details><summary><b>All Reviews - User Logged In</b></summary>

![All Reviews - User Logged In](readme/assets/images/all_reviews_logged_in.png)
</details><br/>

### **Albums**
This page lists all the album reviews that has been made at Review | Alliance. If the user is not logged in there is only a "read more" option visible for the user on each review card. If the user is logged in an *update* and *delete* option gets visible on the reviews that the user has written. No screenshots for this view due to the fact it's the same concept as in the all reviews section except that the review cards are filtered on the category 'album'.

### **Concerts**
This page lists all the concert reviews that has been made at Review | Alliance. If the user is not logged in there is only a "read more" option visible for the user on each review card. If the user is logged in an *update* and *delete* option gets visible on the reviews that the user has written. No screenshots for this view due to the fact it's the same concept as in the all reviews section except that the review cards are filtered on the category 'concert'.

### **Review Detail View**
The review detail shows the details about the review that the user has chosen in the all, albums or concert view. Depending on if the user is logged in the view looks a little bit different. If the user is logged in they get the possibility to like the review and also update and delete it if they have written it. A logged in user can also leave a comment (and update / delete their own comment as well).

<details><summary><b>Review Detail View - User Logged Out</b></summary>

![Review Detail View - User Logged Out](readme/assets/images/review_detail_logged_out.png)
![Review Detail View Comment - User Logged Out](readme/assets/images/review_detail_comment_logged_out.png)
</details><br/>

<details><summary><b>Review Detail View - User Logged In</b></summary>

![Review Detail View - User Logged In](readme/assets/images/review_detail_logged_in.png)
![Review Detail View Comment - User Logged In](readme/assets/images/review_detail_comment_logged_in.png)
</details><br/>

### **Update / Delete Comment**
If the user is logged in and has written a comment there is a possibility to edit and delete the comment. When the comment has been updated it needs to be re-approved by Review | Alliance.

<details><summary><b>Update Comment</b></summary>

![Update Comment](readme/assets/images/update_comment.png)
</details><br/>

### **Member Reviews**
The Member Review Page lists the reviews that the logged in user has written. The user can update and delete their review on this page and also gets information about the status of the review (if it's in draft mode, approved, etc.).

<details><summary><b>Member Reviews</b></summary>

![Member Reviews](readme/assets/images/member_reviews.png)
</details><br/>

### **Create Review**
On this page the registered and logged in user can create their own review. When they have sent it in Review | Alliance needs to approve it, until it's approved it will not be visible for the public.

<details><summary><b>Create Review</b></summary>

![Create Review](readme/assets/images/create_review.png)
</details><br/>

### **Update Review**
On this page the registered and logged in user can update their own review. When they have updated it in Review | Alliance needs to re-approve it, until it's re-approved it will not be visible for the public.

<details><summary><b>Update Review</b></summary>

![Update Review](readme/assets/images/update_review.png)
</details><br/>

### **Profile Page**
On this page the user can view and update their own profile page.

<details><summary><b>Profile Page - To Be Updated</b></summary>

![Profile Page](To Be Updated)
</details><br/>

### **Admin Area**
On this page the administrator (or other superuser decided by Review | Alliance) can *approve* / *unapprove* / *publish* / *unpublish* and *delete* reviews and comments. General information about *number of users*, *number of comments *number of reviews*, *unapproved comments / reviews* is also being showed on the page.

<details><summary><b>Admin Area - To Be Updated</b></summary>

![Admin Area(To Be Updated)
</details><br/>

### **Sign Up**
If the site visitor has no registered user at Review | Alliance they can sign up on this. They can also add a presentation and upload a featured image that will be used on the users profile page.

<details><summary><b>Sign Up</b></summary>

![Sign Up](readme/assets/images/sign_up.png)
</details><br/>

### **Sign In**
On this page the user can sign in to Review | Alliance

<details><summary><b>Sign In</b></summary>

![Sign In](readme/assets/images/sign_in.png)
</details><br/>

### **Sign Out**
When the user clicks sign out in the menu bar a confirmation page is being showed so that the user don't accidently sign out.

<details><summary><b>Sign Out</b></summary>

![Member Reviews](readme/assets/images/sign_out.png)
</details><br/>

### **Footer**
The footer area includes short information about Review | Alliance, contact information and links to relevant social media.

<details><summary><b>Footer</b></summary>

![Footer](readme/assets/images/footer.png)
</details><br/>

### **Flash Messages and confirmation pages to the user **
The sites incorporates flash messages and confirmation pages when an action has been performed (i.e. delete/update actions). Examples of this in the screenshots below.

<details><summary><b>Confirmation Messages</b></summary>

![Review Created Success](readme/assets/images/review_created_success.png)
![Review Deleted Success](readme/assets/images/review_deleted_success.png)
</details><br/>

### Features Left to Implement

* To be updated

[Back to top](<#table-of-content>)

# Technologies Used

## Languages

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the application.
* [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Provides interactive elements of the website

## Frameworks, Libraries & Software
* [Bootstrap](https://getbootstrap.com/) - A CSS framework that helps building solid, responsive, mobile-first sites
* [Django](https://www.djangoproject.com/) - A model-view-template framework used to create the Review | Alliance site
* [Balsamiq](https://balsamiq.com/) - Used to create the wireframe.
* [Microsoft Excel](https://www.microsoft.com/sv-se/microsoft-365/excel) - Used to create testing scenarios.
* [Github](https://github.com/) - Used to host and edit the website.
* [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Terminal in [Gitpod](https://www.gitpod.io) used to push changes to the GitHub repository.
* [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform that the application is deployed to.
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used to test performance of site.
* [Responsive Design Checker](https://www.responsivedesignchecker.com/) - Used for responsiveness check.
* [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org/) - Used to validate the sites accessibility.
* [Graph Models](https://django-extensions.readthedocs.io/en/latest/graph_models.html) - Used to create a *.dot file of all models in the project.
* [dreampuf](https://dreampuf.github.io/GraphvizOnline/) - Creates visually appealing database diagrams of *.dot files.
* [Favicon](https://favicon.io/) - Used to create the favicon.
* [VSCode](https://code.visualstudio.com/) - Used to create and edit the site.
* [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used to debug and test responsiveness.
* [Trello](https://trello.com/en-GB) - A project management tool to organize the project.
* [Cloudinary](https://cloudinary.com/) - A service that hosts all static files in the project.
* [HTML Validation](https://validator.w3.org/) - Used to validate HTML code
* [CSS Validation](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code
* [PEP8 Validation](http://pep8online.com/) - Used to validate Python code
* [JSHint Validation](https://jshint.com/) - Used to validate JavaScript code

## Libraries

[Back to top](<#table-of-content>)

The libraries uses in this project are located in the requirements.txt file and have been documented below

* [asgiref](https://pypi.org/project/asgiref/) - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI.
* [cloudinary](https://pypi.org/project/cloudinary/) - The Cloudinary Python SDK allows you to quickly and easily integrate your application with Cloudinary. Effortlessly optimize, transform, upload and manage your cloud's assets.
* [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) - Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary by implementing Django Storage API.
* [Django](https://pypi.org/project/Django/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
* [django-allauth](https://pypi.org/project/django-allauth/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
* [django-crispy-forms](https://pypi.org/project/django-crispy-forms/) - Used to integrate Django DRY forms in the project.
* [django-extensions](https://pypi.org/project/django-extensions/) - Django Extensions is a collection of custom extensions for the Django Framework.
* [gunicorn](https://pypi.org/project/gunicorn/) - Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.
* [oauthlib](https://pypi.org/project/oauthlib/) - OAuthLib is a framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
* [psycopg2](https://pypi.org/project/psycopg2/) - Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
* [PyJWT](https://pypi.org/project/PyJWT/) - A Python implementation of RFC 7519.
* [pylint-django-2.5.3](https://pypi.org/project/pylint-django/) - A Pylint plugin for improving code analysis when analysing code using Django.
* [pylint-plugin-utils-0.7](https://pypi.org/project/pylint-plugin-utils/) - This is not a direct Pylint plugin, but rather a set of tools and functions used by other plugins such as pylint-django.
* [python3-openid](https://pypi.org/project/python3-openid/) - OpenID support for modern servers and consumers.
* [pytz](https://pypi.org/project/pytz/) - This is a set of Python packages to support use of the OpenID decentralized identity system in your application, update to Python 3
* [requests-oauhlib](https://pypi.org/project/requests-oauthlib/) - P    rovides first-class OAuth library support for Requests.
* [sqlparse](https://pypi.org/project/sqlparse/) - sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.
* [cryptography-3.3.23](https://pypi.org/project/cryptography/3.3/) - Cryptography is a package which provides cryptographic recipes and primitives to Python developers.

# Testing

## Code Validation
To be updated

### Markup Validation
To be updated

<details><summary><b>HTML Validation Result</b></summary>

![HTML Result Home Page](readme/assets/images/html_validation.png)
</details><br/>

[Back to top](<#table-of-content>)

### CSS Validaton
To be updated

<details><summary><b>CSS Validation Result</b></summary>

![CSS Result](readme/assets/images/css_validation.png)
</details><br/>

[Back to top](<#table-of-content>)

### PEP Validation
To be updated

<details><summary><b>PEP Validation Result</b></summary>

![PEP Validation](readme/assets/images/pep_validation_ok.png)
</details><br/>

[Back to top](<#table-of-content>)

### JavaScript Validation
To be updated

[Back to top](<#table-of-content>)

## Additional Testing

### Manual Testing

In addition to tests stated above I have performed a series of manual tests. Below the list of tests that has been conducted can be found.

| Status | **Main Website - User Logged Out**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Pasting page that needs authentication loads a forbidden page
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and lists all reviews
| &check; | Clicking the All button on the nav bar lists all reviews
| &check; | Clicking the Albums button on the nav bar lists all album reviews
| &check; | Clicking the Concert button on the nav bar lists all concert reviews
| &check; | Clicking the Log In / Sign Up loads the sign up page
| &check; | 6 Reviews are rendered for the user on all / albums / concert page before pagination kicks in
| &check; | Clicking the Read More button on the a review card loads the review detail page
| &check; | In the details view the user cannot create a comment
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the YouTube link in the footer area opens YouTube in a new window
| &check; | Clicking the LinkedInlink in the footer area opens LinkedIN in a new window
| &check; | Clicking the Twitter link in the footer area opens Twitter in a new window

| Status | **Main Website - User Logged In**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Pasting page that needs authentication loads a forbidden page
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and lists all reviews
| &check; | Clicking the All button on the nav bar lists all reviews
| &check; | Clicking the Albums button on the nav bar lists all album reviews
| &check; | Clicking the Concert button on the nav bar lists all concert reviews
| &check; | 6 Reviews are rendered for the user on all / albums / concert page before pagination kicks in
| &check; | Clicking the Read More button on the a review card loads the review detail page
| &check; | In the detail view the logged in user can comment a review
| &check; | In the detail view the logged in user can update/delete the comments written by themselves
| &check; | Clicking the update button loads the update comment page
| &check; | Clicking the delete button loads the delete comment page
| &check; | In the detail view the logged in user can like/unlike reviews
| &check; | In the detail view the logged in user can update/delete the reviews written by themselves
| &check; | Clicking the update button in the detail view loads the update review page
| &check; | Clicking the delete button in the detail view loads the delete review page
| &check; | Clicking the My Reviews button in the logged in user menu lists the logged in users reviews
| &check; | Clicking the update button in the My Reviews view loads the update review page
| &check; | Clicking the delete button in the My Reviews view loads the delete review page
| &check; | In the My Reviews view the information about the review status is correct
| &check; | In the logged in user menu the Admin Area is not visible
| &check; | Clicking the Show Profile Page button in the logged in user menu loads the My Profile page
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the YouTube link in the footer area opens YouTube in a new window
| &check; | Clicking the LinkedInlink in the footer area opens LinkedIN in a new window
| &check; | Clicking the Twitter link in the footer area opens Twitter in a new window

| Status | **Main Website - Admin Logged In**
|:-------:|:--------|
| &check; | Clicking the Admin Area button in the logged in user menu loads the Admin Area Page
| &check; | In the review section. Clicking the approve / unapprove / publish / unpublish toggles the approve and status signs
| &check; | The view button is only visible if a review is published
| &check; | In the comment section. Clicking the approve / unapprove toggles the approve and status signs
| &cross; | When clicking delete / add genre the appropiate page loads.


### Automated Testing

### Responsiveness Test
To be updated

[Back to top](<#table-of-content>)

### Browser Compatibility
* Google Chrome Version (103.0.5060.114)
* Mozilla Firefox (version 102.0.1)
* Min (version 1.25.1)
* Apple Safari (version 15.5)
* Microsoft Edge (version 103.0.1264.62)

[Back to top](<#table-of-content>)

### Lighthouse
To be updated


<details><summary><b>Lighthouse Result Result</b></summary>

![Lighthouse Form Confirmation Page Result](readme/assets/images/lighthouse.png)
</details><br/>

### WAVE
To be updated

<details><summary><b>WAVE Result</b></summary>

![WAVE Result](readme/assets/images/wave_result.png)
</details><br/>

[Back to top](<#table-of-content>)

### Peer Review
To be updated


<details><summary><b>Test Scenarios</b></summary>

![Test Scenarios](readme/assets/images/testing_scenarios.png)
</details><br/>

<details><summary><b>User Stories</b></summary>

![User Stories](readme/assets/images/testing_user_stories.png)
</details><br/>

## Known bugs

### Fixed Bugs

**2022-xx-xx**
* Bug: To be updated

### Unfixed Bugs

**2022-xx-xx**
* Bug: To be updated


[Back to top](<#table-of-content>)

# Deployment

## Deployment To Heroku

The project was deployed to [Heroku](https://www.heroku.com). To deploy, please follow the process below:

1. The first step is to log in to Heroku (or create an account if needed).

<details><summary><b>Heroku Step 1</b></summary>

![Heroku Step 1](readme/assets/images/heroku_step_1.png)
</details><br />

2. In the top right corner there is a button that is labeled 'New'. Click that and then select 'Create new app'.

<details><summary><b>Heroku Step 2</b></summary>

![Heroku Step 2](readme/assets/images/heroku_step_2.png)
</details><br />

3. Now it's time to enter an application name that needs to be unique. When you have chose the name, choose your region and click 'Create app".

<details><summary><b>Heroku Step 3</b></summary>

![Heroku Step 3](readme/assets/images/heroku_step_3.png)
</details><br />

4. On the next page, click the 'Settings' tab and find the "Config Vars" section. When you have found it, click "Reveal Config Vars". Now it's time to add values. In the 'WOM Record Collection' case I needed to add two values. The first one was the credentials (KEY input field = "CREDS", VALUE input field = "your credentials", I have blurred out my credentials for security reasons), click the 'Add' button. Next you need to add another key, enter "PORT" in the KEY input field and "8000" in the VALUE field, click the 'Add' button.

<details><summary><b>Heroku Step 4</b></summary>

![Heroku Step 4](readme/assets/images/heroku_step_4.png)
</details><br />

5. Next step is to add buildpacks to the application which will run when the application is deployed. The reason why this is needed is because all dependencies and configurations will be installed for the application. To do this you scroll down to the buildpacks section on the settings page and click the button 'Add buildpack'.

<details><summary><b>Heroku Step 5</b></summary>

![Heroku Step 5](readme/assets/images/heroku_step_5.png)
</details><br />

6. Add "Python" and node.js". It is important that Python is listed above node.js. If it's not you can sort it by dragging and dropping.

<details><summary><b>Heroku Step 6</b></summary>

![Heroku Step 6](readme/assets/images/heroku_step_6.png)
</details><br />

7. Now it's time for deployment. Scroll to the top of the settings page and click the 'Deploy' tab. For deployment method, select 'Github'. Search for the repository name you want to deploy and then click connect.

<details><summary><b>Heroku Step 7</b></summary>

![Heroku Step 7](readme/assets/images/heroku_step_7.png)
</details><br />

8. Scroll down on the deploy page and choose deployment type. Choose to enable automatic deployments if you want to and then  click 'Deploy Branch'.

<details><summary><b>Heroku Step 8</b></summary>

![Heroku Step 8](readme/assets/images/heroku_step_8.png)
</details><br />

The live link to the 'WOM Record Collection' Github repository can be found [here](https://github.com/worldofmarcus/project-portfolio-3).

[Back to top](<#table-of-content>)

## How To Fork The Repository On GitHub

It is possible to do a copy of a GitHub Repository by forking the GitHub account. The copy can then be viewed and it is also possible to do changes in the copy without affecting the original repository. To fork the repository, take these steps:

1. After logging in to GitHub, locate the repository. On the top right side of the page there is a 'Fork' button. Click on the button to create a copy of the original repository.

<details><summary><b>Github Fork</b></summary>

![Fork](readme/assets/images/github_fork.png)
</details><br />

[Back to top](<#table-of-content>)

## Create A Local Clone of A Project

To create a local clone of your repository, follow these steps:

1. When you are in the repository, find the code tab and click it.
2. To the left of the green GitPod button, press the 'code' menu. There you will find a link to the repository. Click on the clipboard icon to copy the URL.
3. Use an IDE and open Git Bash. Change directory to the location where you want the cloned directory to be made.
4. Type 'git clone', and then paste the URL that you copied from GitHub. Press enter and a local clone will be created.

<details><summary><b>Github Create Local Clone</b></summary>

![Clone](readme/assets/images/github_local_clone.png)
</details><br />

[Back to top](<#table-of-content>)

# Credits

## Content

* All text content written by Marcus Eriksson.

* Template for read.me provided by Code Institute (*with some additional changes that my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/))* suggested.

## Technical

* Inspiration on importing Google Sheet to Rich table was taken from [Stack Overflow](https://stackoverflow.com/questions/71799108/how-do-i-zip-a-list-of-lists-into-a-python-rich-table-with-headers-and-rows)

* Convert to uppercase in list of lists taken (*and slightly modified*) from [Stack Overflow](https://stackoverflow.com/questions/54438770/lowercase-a-list-of-lists)

* Inspiration taken from [Computing Learner](https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/) to create a menu in a console application.

# Acknowledgements
This fictional site was created for Portfolio Project #4 (Full-Stack Tolkin) - Diploma in Full Stack Software Development Diploma at the [Code Institute](https://www.codeinstitute.net). I would like to thank my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for relevant feedback during the project.

*Marcus Eriksson, 2022-xx-xx*

[Back to top](<#table-of-content>)