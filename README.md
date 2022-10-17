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

<details><summary><b>Trello & Github Board</b></summary>

![Trello Image](readme/assets/images/trello.png)

![User Stories](readme/assets/images/user_stories.png)
</details><br/>

[Back to top](<#table-of-content>)

### Database Schema
I have used a modelling tool called [Graph Models](https://django-extensions.readthedocs.io/en/latest/graph_models.html) to create the database schema. In short it shows the relationships between the different models in the database connected to the application. Graph Models exports a *.dot file which easily can be converted to a more 'easy to read' design with the help of the application [dreampuf](https://dreampuf.github.io/GraphvizOnline/).

Models used (besides standard user model) in this project are:

* **Category** - Handles categories. I made a specific model to be able to add more dynamics (create / remove categories going forward in the admin backend instead of 'hard code' it in the code).
* **Genre** - Handles genre. I made a specific model to be able to add more dynamics (create / remove genres going forward in the admin backend instead of 'hard code' it in the code).
* **Post** - Handles all the reviews
* **Comment** - Handles all the comments
* **UserProfile** - Handles the user profile information (first name, last name, presentation and featured image for the specific user/reviewer). There is a one-to-one relation to the user model to connect it to the standard user model.

<details><summary><b>Database Schema</b></summary>

![Database Schema](readme/assets/images/database_schema.png)
</details><br/>

# **User Experience (UX)**

## Wireframes
The wireframes for the site were created in the software [Balsamiq](https://balsamiq.com). The wireframes have been created for desktop, tablet and mobile devices. The text content wasn't finalized during the wireframe process. It's worth mentioning that there are visual differences compared to the wireframes, the reason being design choices that was made during the creation process.

<details><summary><b>Wireframes</b></summary>

![Wireframes](readme/assets/images/balsamiq.png)
</details><br/>

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
| As a Site User | I can create a profile page so that other reviewers can read about who I am | &check; |
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

The Review | Alliance site is split up in two parts: **when the user is logged out** and **when the user is logged in**. Depending on login status different pages is available for the user. When the user is logged out the pages: *about*, *all*, *albums*, *concerts* are avaliable. When the user is logged in *about*, *all*, *albums*, *concerts*, *create review*, *view my reviews* and *show profile page* are available. If you are logged in as an administratorThe site has an minimalistic, clean and intuitive design that makes the site easy to navigate for the user.

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
In the about section the user can read about both who Review | Alliance are but also about all reviewers that are registered on the site.

<details><summary><b>About Section</b></summary>

![About](readme/assets/images/about.png)
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
The Member Review Page lists the reviews that the logged in user has written. The user can update and delete their review on this page and also gets information about the status of the review. There are 4 different statuses:

* *Your review is awaiting approval* - Review has been submitted with the status 'published' and awaits approval
* *Your review is in draft status but is approved* - The review is in draft status but has been approved
* *Your review is published and approved* - The review is published and approved
* *Your review is in draft status* - The review has been submitted with the status 'draft'

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
On this page the user can view and update their own profile page. The profile is visible in the about section.

<details><summary><b>Profile Page</b></summary>

![Profile Page](readme/assets/images/update_profile.png)
</details><br/>

### **Admin Area**
On this page the administrator (or other superuser decided by Review | Alliance) can *approve* / *unapprove* / *publish* / *unpublish* and *delete* reviews and comments. General information about *number of users*, *number of comments*, *number of reviews*, *unapproved comments / reviews* is also being showed on the page.

<details><summary><b>Admin Area</b></summary>

![Admin Area](readme/assets/images/admin_area.png)
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

### **Flash Messages and confirmation pages to the user**
The sites incorporates flash messages and confirmation pages when an action has been performed (i.e. delete/update actions). Examples of this in the screenshots below.

<details><summary><b>Confirmation Messages</b></summary>

![Review Created Success](readme/assets/images/review_created_success.png)
![Review Deleted Success](readme/assets/images/review_deleted_success.png)
</details><br/>

### Features Left to Implement

* Add more automated testing
* Add 'current page is active' in navbar
* Search reviews functionality from the navbar
* Information in the about section how many reviews each reviewer has made
* Add / remove genre and category in admin section
* Add image resize functionality
* Remove admin approval of comments

[Back to top](<#table-of-content>)

# Technologies Used

## Languages

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the application.
* [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Provides interactive elements of the website

## Frameworks & Software
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
* [a11y Color Contrast Accessibility Validator](https://color.a11y.com/Contrast/) - Used to test color contrast on the site
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

The libraries used in this project are located in the requirements.txt file and have been documented below

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

## Testing User Stories

* As a Site User | I can view a list of the music reviews so that I can select one to read
    * At the top of the site there is a navigation bar with a link that lists all reviews when the user clicks on it.

* As a Site User | I can view a list of the concert reviews so that I can select one to read
   * At the top of the site there is a navigation bar with a link that lists all concert reviews when the user clicks on it.

* As a Site User | I can click on a specific review so that I can read it in detail
   * At the top of the site there is a navigation bar with a link that lists all album reviews when the user clicks on it.

* As a Site User | I can like and unlike a review so that it is possible for me to interact with the review
    * When the user is logged it is possible to click on a heart on the review detail page to like / unlike a review.

* As a Site User | I can view the number of likes on each review so that I can see how popular a specific review is
    * On the review detail page the user can see how many likes the specific review has.

* As a Site User | I can contact Review Alliance in an easy way so that I can interact with them if I have a need for it
    * In the footer there is clear information about how to contact Review | Alliance.

* As a Site User | I can navigate easy on the site through paginated list of posts so that I feel comfortable using the site
    * On the review pages the pagination is activated when there are more than 6 reviews on a page.

* As a Site User | I can view comments on a specific review so that I can read the conversations between different users on the site
    * When the user clicks on a specific review the comment section can, in an easily way, be viewed.

* As a Site User | I can sign up an account so that I can like and comment on reviews, create a profile page, create own reviews and edit / remove my reviews
    * In the navigation bar the user can click the Login / Sign up link to either login or sign up for a new account. When this is done the user can interact on the page as stated in the user story).

* As a Site User | I can create a profile page so that other reviewers can read about who I am
    * If a user is registered and logged in there is a 'Show Profile'-page in the navigation menu where the user can fill in profile details. The profile is shown for the site users in the about section.

* As a Site User | I can comment on a review so that I can be involved in the conversation
    * When the user is logged in they can write a comment on a specific review on the review detail page.

* As a Site User | I can edit my comment so that I can change the content if needed
    * When the user is logged in an edit button appears on the all comments that the specific user has written. When the user clicks the edit button they can change the content in the comment.

* As a Site User | I can remove my review so that I have full control of my reviews
    * When the user is logged in a delete button appears on the all comments that the specific user has written. When the user clicks the delete button they get the option to delete the comment.

* As a Site User | I can choose to see my own reviews so that I can find them easily
    * When a user is logged in they can choose to view their own reviews through the link 'My Reviews'.

* As a Site User | I can create a new review so that I can contribute to with new content to Review Alliance
    * When a user is logged in they can create a new review through the 'Create New Review'-link in the navigation bar.

* As a Site User | I can log out from the site so that I can feel safe that nobody can access my information
    * When the user is logged in it is possible to choose the 'Log Out'-option in the navigation menu.

* As a Site User | I can create draft reviews so that I can finish writing the content later
    * When a logged in user creates a review they have the possibility to set the status on the review either on published or draft.

* As a Site User | I can get visual feedback when interacting with the content so that I can be sure how I have interacted with the page
    * When the user sign in, sign out, create / update / deletes reviews and comments they always get a confirmation message to secure visual feedback.

* As a Site Admin | I can log out from the site so that I can feel safe that nobody can access my information
   * When the admin is logged in it is possible to choose the 'Log Out'-option in the navigation menu.

* As a Site Admin | I can create, read, update and delete reviews so that I can manage my review content
    * When the user is logged in as an administrator / superuser a new item show up in the navigation menu called 'Admin Area'. In this area the user can read, update and delete reviews. Creation of reviews can be made the same way as any logged in user. Updating reviews can only be made if the administrator has written the original review.

* As a Site Admin | I can approve reviews so that I can secure high quality of the content
    * When the user is logged in as an administrator / superuser a new item show up in the navigation menu called 'Admin Area'. In this area the user can approve / unapprove / publish / unpublish reviews.

* As a Site Admin | I can approve and disapprove comments so that I can secure a safe environment for the Site Users
    * When the user is logged in as an administrator / superuser a new item show up in the navigation menu called 'Admin Area'. In this area the user can approve / unapprove comments.

* As a Site Admin | I can create draft reviews so that I can finish writing the content later
    * When a user is logged in as an administrator they have the possibility to create a review they and set the status to published or draft.

* As a Site Admin | I can access an admin area so that I can get a general understanding of logged in users, number of likes and number of posts
    * In the admin area there is an summary area in the top with general information about the site (i.e. number of users, number of reviews / comments that need approval)

* As a Site Admin | I can get visual feedback when interacting with the content so that I can be sure how I have interacted with the page
    * When the admin signs in, signs out, create / update / deletes reviews and comments they always get a confirmation message to secure visual feedback.

## Code Validation
The code on the 'Review | Alliance' site has been tested through W3C Markup Validatiaon Service, W3C CSS Validatiaaon Service and JSHint. Errors were at first found on the site in the W3C Markup Validation Service but could quite easily be fixed (see bugs section). One error appeared as well in the W3C CSS Validation but that was connected to Font Awesome and not to the site code itself (see bugs section).

### Markup Validation
After fixing the inital errors that W3C Markup Validaton Service reported, no errors were returned.

<details><summary><b>HTML Validation Result</b></summary>

![HTML Result Home Page](readme/assets/images/html_validation_no_error.png)
</details><br/>

[Back to top](<#table-of-content>)

### CSS Validaton
When validating my own code the W3C CSS Validator reports no errors.

<details><summary><b>CSS Validation Result</b></summary>

![CSS Result](readme/assets/images/css_validation_no_error.png)
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
| &check; | When user submits a comment a message with approval information is being showed on the page
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
| &cross; | When clicking delete / add genre the appropiate page loads and shows success page after submit
| &check; | Total Users shows correct number of total users
| &check; | Total Reviews shows the correct number of total reviews
| &check; | Total Comments shows the correct number of total comments
| &check; | Reviews that need approval shows the correct numer of reviews that need approval
| &check; | Comments that need approval shows the correct numer of comments that need approval

 Status | **Create A Review - User Logged In**
|:-------:|:--------|
| &check; | Title field is required
| &check; | Title field does not accept empty field
| &check; | Title field does not accept just spaces
| &check; | Artist field is required
| &check; | Artist field does not accept empty field
| &check; | Artist field does not accept just spaces
| &check; | Featured Image is not required
| &check; | Fragment field is required
| &check; | Fragment field does not accept empty field
| &check; | Body field is required
| &check; | Body field does not accept empty field
| &check; | Category field defaults to Uncategorized
| &check; | Fragment field is required
| &check; | Fragment field does not accept empty field
| &check; | Record Label is not required
| &check; | Venue is not required
| &check; | Genre field defaults to Uncategorized
| &check; | Rating field defaults to 3
| &check; | Status field defaults to Draft
| &check; | Posting as shows name of logged in user
| &check; | Review Success Page is displayed when the user submits the review and the form validation is ok.

Status | **Create A New User - User Logged Out**
|:-------:|:--------|
| &check; | Username field is required
| &check; | Username field does not accept empty field
| &check; | Email field does not accept just spaces
| &check; | Email field is optional
| &check; | Password field does not accept empty field
| &check; | Success flash message is displayed when the user submits the create a new user form
| &check; | Default biography is visible in about page (with i.e default featured image)

Status | **Create A Profile Page - User Logged In**
|:-------:|:--------|
| &check; | Default featured image is visible the first time a user opens the 'my profile' page
| &check; | First Name field is required
| &check; | First Name field does not accept empty field
| &check; | First Name field does not accept just spaces
| &check; | Last Name field is required
| &check; | Last Name field does not accept empty field
| &check; | Last Name field does not accept just spaces
| &check; | Update profile success Page is displayed when the user submits the profile form

### Automated Testing
Some automated testing has been done during this project. I currently have X number of tests which provide XX% coverage. See screenshot below. Automated tests can be run by typing the command - *python3 manage.py test*

<details><summary><b>Automated Testing - To Be Updated</b></summary>

![Automated Testing](To Be Updated)
</details><br/>

### Responsiveness Test
The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).

| Desktop    | Display <1280px       | Display >1280px    |
|------------|-----------------------|--------------------|
| Render     | pass                  | pass               |
| Images     | pass                  | pass               |
| Links      | pass                  | pass               |

| Tablet     | Samsung Galaxy Tab 10 | Amazon Kindle Fire | iPad Mini | iPad Pro |
|------------|-----------------------|--------------------|-----------|----------|
| Render     | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

| Phone      | Galaxy S5/S6/S7       | iPhone 6/7/8       | iPhone 12pro         |
|------------|-----------------------|--------------------|----------------------|
| Render     | pass                  | pass               | pass      | pass     |
| Images.    | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

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
Additional testing of the application was conducted by people outside of the software development field. Some smaller spelling and grammar errors were found and corrected. No issues connected to design or handling of the site.

## Known bugs
No known bugs besides those in the unfixed bugs section.

### Fixed Bugs
**2022-10-10**
When updating a review or comment the approved variable did not get updated to 'False'. This is is now handled and fixed.

**2022-10-11**
When updating a review the slug did not change. I chose to fix this bug so that the slug updates when a review is updated but one 'school' within this area says that a slug never should be changed (due to problems with urls / linking in the future). This functionality is an easy fix to remove if necessary but I chose to keep it for now.

**2022-10-14**
* Bug: When the Markup Validation was done there was initially quite a lot of errors. The debugging process was very straight forward and the errors could easily be fixed.

<details><summary><b>HTML Validation</b></summary>

![HTML Validation](readme/assets/images/html_validation_error.png)
</details><br />

**2022-10-17**
* Bug: When the CSS Validation an error apperars that is connected to Font Awesome. When I validate my own CSS code there are no errors at all. So this might be a Font Awesome bug that is out of my control. But I thought it would be proper to highlight the error here in the bugs section.

<details><summary><b>CSS Validation</b></summary>

![HTML Validation](readme/assets/images/css_validation_error.png)
</details><br />

### Unfixed Bugs

**2022-10-14**
* Bug: Summernote is not working 100% properly. I have debugged and sweeped the Internet for solutions. The issue is that when a user creates a review it's not possible to overide the choices the user makes when writing the review (i.e. font-size, font). I tried to handle this by setting rules of what tools to show in the Summernote editor without success. One workaround could of course be to remove the Summernote functionality but I did not want to do that in this project at least. this bug is still unfixed and I haven't found a solution to it yet.


[Back to top](<#table-of-content>)

# Deployment

## Deployment To Heroku

The project was deployed to [Heroku](https://www.heroku.com). To deploy, please follow the process below:

1. To begin with we need to create a GitHub repository from the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) by following the link and then click 'Use this template'.

<details><summary><b>Heroku Deployment - Step 1</b></summary>

![Heroku Deployment Step 1](readme/assets/images/heroku_01.png)
</details><br />

2. Fill in the needed details as stated in the screenshot below and then click 'Create Repository From Template'.

<details><summary><b>Heroku Deployment - Step 2</b></summary>

![Heroku Deployment Step 2](readme/assets/images/heroku_02.png)
</details><br />

3. When the repository creation is done click 'Gitpod' as stated in the screenshot below.

<details><summary><b>Heroku Deployment - Step 3</b></summary>

![Heroku Deployment Step 3](readme/assets/images/heroku_03.png)
</details><br />

4. Now it's time to install Django and the supporting libraries that are needed. Type the commands below to do this.

* ```pip3 install 'django<4' gunicorn```
* ```pip3 install 'dj_database_url psycopg2```
* ```pip3 install 'dj3-cloudinary-storage```

<details><summary><b>Heroku Deployment - Step 3</b></summary>

![Heroku Deployment Step 4](readme/assets/images/heroku_04.png)
</details><br />

5. When Django and the libraries are installed we need to create a requirements file.

* ```pip3 freeze --local > requirements.txt``` - This will create and add required libraries to requirements.txt

<details><summary><b>Heroku Deployment - Step 3</b></summary>

![Heroku Deployment Step 5](readme/assets/images/heroku_05.png)
</details><br />

6. Now it's time to create the project.

* ```django-admin startproject YOUR_PROJECT_NAME .``` - This will create your project

<details><summary><b>Heroku Deployment - Step 6</b></summary>

![Heroku Deployment Step 6](readme/assets/images/heroku_06.png)
</details><br />

7. When the project is created we can now create the application.

* ```python3 manage.py startapp APP_NAME``` - This will create your application

<details><summary><b>Heroku Deployment - Step 7</b></summary>

![Heroku Deployment Step 7](readme/assets/images/heroku_07.png)
</details><br />

8. We now need to add the application to settings.py

<details><summary><b>Heroku Deployment - Step 8</b></summary>

![Heroku Deployment Step 8](readme/assets/images/heroku_08.png)
</details><br />

8. Now it is time to do our first migration and run the server to test that everything works as expected. This is done by writing the commands below.

* ```python3 manage.py migrate``` - This will migrate the changes
* ```python3 manage.py runserver``` - This runs the server. To test it, click the open browser button that will be visible after the command is run.

9. Now it is time to create our application on Heroku, attach a database, prepare our environment and settings.py file and setup the Cloudinary storage for our static and media files.

* Head on to [Heroku](https://www.heroku.com/) and sign in (or create an account if needed).

10. In the top right corner there is a button that is labeled 'New'. Click that and then select 'Create new app'.

<details><summary><b>Heroku Step 09</b></summary>

![Heroku Step 9](readme/assets/images/heroku_09.png)
</details><br />

10. Now it's time to enter an application name that needs to be unique. When you have chosen the name, choose your region and click 'Create app".

<details><summary><b>Heroku Step 10</b></summary>

![Heroku Step 10](readme/assets/images/heroku_10.png)
</details><br />

11. To add a database to the app you need to go to the resources tab ->> add-ons, search for 'Heroku Postgres' and add it.

<details><summary><b>Heroku Step 11</b></summary>

![Heroku Step 11](readme/assets/images/heroku_11.png)
</details><br />

12. Go to the settings tab and click on the reveal Config Vars button. Copy the text from DATABASE_URL (because we are going to need it in the next step).

<details><summary><b>Heroku Step 12</b></summary>

![Heroku Step 12](readme/assets/images/heroku_12.png)
</details><br />

13. Go back to GitPod and create a new env.py in the top level directory. Then add these rows.

* ```import os``` - This imports the os library
* ```os.environ["DATABASE_URL_FROM HEROKU"]``` - This sets the environment variables.
* ```os.environ["SECRET_KEY"]``` - Here you can choose whatever secret key you want.

<details><summary><b>Heroku Step 13</b></summary>

![Heroku Step 13](readme/assets/images/heroku_13.png)
</details><br />

14. Now we are going to head back to Heroku to add our secret key to config vars. See screenshot below.

<details><summary><b>Heroku Step 14</b></summary>

![Heroku Step 14](readme/assets/images/heroku_14.png)
</details><br />

15. Now we have some preparations to do connected to our environment and settings.py file. In the settings.py, add the following code:

```import os```

```import dj_database_url```

```if os.path.isfile("env.py"):```

```import env```

<details><summary><b>Heroku Step 15</b></summary>

![Heroku Step 15](readme/assets/images/heroku_15.png)
</details><br />

16. In the settings file, remove the insecure secret key and replace it with:
```SECRET_KEY = os.environ.get('SECRET_KEY')```

<details><summary><b>Heroku Step 16</b></summary>

![Heroku Step 16](readme/assets/images/heroku_16.png)
</details><br />

17. Now we need to comment out the old database setting in the settings.py file (this is because we are going to use the postgres database instead of the sqlite3 database).

<details><summary><b>Heroku Step 17 1/2</b></summary>

![Heroku Step 17](readme/assets/images/heroku_17_1.png)
</details><br />

Now, add the link to the DATABASE_URL that we added to the environment file earlier.

<details><summary><b>Heroku Step 17 2/2</b></summary>

![Heroku Step 17](readme/assets/images/heroku_17_2.png)
</details><br />

18. Save all your fields and migrate the changes.

```python3 manage.py migrate```

19. Now we are going to get our connection to Cloudinary connection working (this is were we will store our static files). First you need to create a Cloudinary account and from the Cloudinary dashboard copy the API Environment Variable.

20. Go back to the env.py file in Gitpod and add the Cloudinary url (it's very important that the url is correct):

```os.environ["CLOUDINARY_URL"] = "cloudinary://************************"```

21. Let's head back to Heroku and add the Cloudinary url in Config Vars. We also need to add a disable collectstatic variable to get our first deployment to Heroku to work.

<details><summary><b>Heroku Step 21</b></summary>

![Heroku Step 21](readme/assets/images/heroku_21.png)
</details><br />

22. Let's head back to our settings.py file on Gitpod. We now need to add our Cloudinary Libraries we installed earlier to the installed apps. Here it is important to get the order correct.

<details><summary><b>Heroku Step 22</b></summary>

![Heroku Step 22](readme/assets/images/heroku_22.png)
</details><br />

23. For Django to be able to understand how to use and where to store static files we need to add some extra rows to the settings.py file.

<details><summary><b>Heroku Step 23</b></summary>

![Heroku Step 23](readme/assets/images/heroku_23.png)
</details><br />

24. Hang in there, we have just a couple of steps left. Now it's time to link the file to the Heroku templates directory.

<details><summary><b>Heroku Step 24</b></summary>

![Heroku Step 24](readme/assets/images/heroku_24.png)
</details><br />

25. Let's change the templates directory to TEMPLATES_DIR in the teamplates array.

<details><summary><b>Heroku Step 25</b></summary>

![Heroku Step 25](readme/assets/images/heroku_25.png)
</details><br />

26. To be able to get the application to work through Heroku we also need to add our Heroku app and localhost to which hosts that are allowed.

<details><summary><b>Heroku Step 26</b></summary>

![Heroku Step 26](readme/assets/images/heroku_26.png)
</details><br />

27. Now we just need to add some files to Gitpod.

* Create 3 folders in the top level directory: **media**, **static**, **templates**
* Create a file called **Procfile* and add the line ```web: gunicorn PROJ_NAME.wsgi?``` to it.d

28. Now you can save all the files and prepare for the first commit and push to Github by writing the lines below.

* ```git add .```
* ```git commit -m "Deployment Commit```
* ```git push```

29. Before moving on to the Heroku deployment we just need to add one more thing in the config vars. We need to add "PORT" in the KEY input field and "8000" in the VALUE field. If we don't add this there might be problems with the deployment.

30. Now it's time for deployment. Scroll to the top of the settings page in Heroku and click the 'Deploy' tab. For deployment method, select 'Github'. Search for the repository name you want to deploy and then click connect.

31. Scroll down to the manual deployment section and click 'Deploy Branch'. Hopefully the deployment is successful!

<details><summary><b>Heroku Step 31</b></summary>

![Heroku Step 31](readme/assets/images/heroku_step_31.png)
</details><br />

The live link to the 'Review | Alliance' site on Heroku an be found [here](https://project-portfolio-4.herokuapp.com/). And the Github repository can be found [here](https://github.com/worldofmarcus/project-portfolio-4).

[Back to top](<#table-of-content>)

## How To Fork The Repository On GitHub

It is possible to do a independent copy of a GitHub Repository by forking the GitHub account. The copy can then be viewed and it is also possible to do changes in the copy without affecting the original repository. To fork the repository, take these steps:

1. After logging in to GitHub, locate the repository. On the top right side of the page there is a 'Fork' button. Click on the button to create a copy of the original repository.

<details><summary><b>Github Fork</b></summary>

![Fork](readme/assets/images/github_fork.png)
</details><br />

[Back to top](<#table-of-content>)

## Cloning And Setting Up This Project

To clone and set up this project you need to follow the steps below.

1. When you are in the repository, find the code tab and click it.
2. To the left of the green GitPod button, press the 'code' menu. There you will find a link to the repository. Click on the clipboard icon to copy the URL.
3. Use an IDE and open Git Bash. Change directory to the location where you want the cloned directory to be made.
4. Type 'git clone', and then paste the URL that you copied from GitHub. Press enter and a local clone will be created.

<details><summary><b>Github Create Local Clone</b></summary>

![Clone](readme/assets/images/github_clone_01.png)
</details><br />

5. To be able to get the project to work you need to install the requirements. This can be done by using the command below:

* ```pip3 install -r requirements.txt``` - This command downloads and install all required dependencies that is stated in the requirements file.

6. The next step is to set up the environment file so that the project knows what variables that needs to be used for it to work. Environment variables are usually hidden due to sensitive information. It's very important that you don't push the env.py file to Github (this can be secured by adding env.py to the .gitignore-file). The variables that are declared in the env.py file needs to be added to the Heroku config vars. Don't forget to do necessary migrations before trying to run the server.

* ```python3 manage.py migrate``` - This will do the necessary migrations.
* ```python3 manage.py runserver``` - If everything i setup correctly the project is now live locally.

<details><summary><b>Setup env.py</b></summary>

![Clone](readme/assets/images/github_clone_02.png)
</details><br />

[Back to top](<#table-of-content>)

# Credits

## Content

* All text content written by Marcus Eriksson.

* Test concert images on review cards taken from [Shutterstock](https://www.shutterstock.com/sv)

* Test album images on review cards taken from [Kollektiv Fem](https://www.kollektivfem.se) which is owned by Marcus Eriksson.

* Featured default review image taken from [FAVPNG](https://favpng.com/png_view/download-clip-art-png/hHNmGh4R)

* Template for read.me provided by Code Institute (*with some additional changes that my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/))* suggested.

## Technical

* Inspiration regarding UpdateView taken from [Learn Django Class Based Views](https://www.youtube.com/watch?v=EUUjJdw3EBM)

* Formatting date format [Formatting Date, Time, and Numbers in Django Templating](https://collinshillary1.medium.com/formatting-date-time-and-numbers-in-django-templating-f53fea027a06)

* Inspiration regarding CSS code to add circle around text [How to Add a Circle Around a Number in CSS](https://www.w3docs.com/snippets/css/how-to-add-a-circle-around-a-number-in-css.html)

* Inspiration regarding adding extra forms in Django Allauth form [How to add more custom fields on signup form?](https://stackoverflow.com/questions/68591755/django-allauth-how-to-add-more-custom-fields-on-signup-form)

# Acknowledgements
This fictional site was created for Portfolio Project #4 (Full-Stack Tolkin) - Diploma in Full Stack Software Development Diploma at the [Code Institute](https://www.codeinstitute.net). I would like to thank my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for relevant feedback during the project.

*Marcus Eriksson, 2022-10-18*

[Back to top](<#table-of-content>)