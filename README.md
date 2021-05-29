# CAMPER HAMPERS

## Code Institute - Milestone Project 4

NEED TO ADD
![Camper Hampers responsive website mockup]( https://github.com/chloelewisdev/milestone-project-3/blob/master/static/images/Responsive-web-mockup.png)

This was the last of four Milestone Projects that made up the Full Stack Web Development Program at The Code Institute. The main requirements were to build a full-stack website with the use of HTML, CSS, JavaScript, Python, Django and a relational database. Accommodating payment services was another requirement for this project and this was achieved through the use of Stripe.

The idea for this website was based on my own experiences of camping and going away in a campervan – I have always thought how amazing it would be to have a hamper of food or drinks prepared for you before you depart so that all hassle is removed on the first night and morning and you can just enjoy the adventure! The result is a website providing savoury, sweet and campfire hampers, which users can order to be delivered on their departure. Users can create their own profile where they can store their personal information such as their delivery address, pay securely to purchase a hamper, leave testimonials and view their order history, as well as the owner’s blog. 


This was the third of four Milestone Projects that made up the Full Stack Web Development Program at The Code Institute. The main requirements were to build site a site using HTML, CSS, JavaScript, Python + Flask and MongoDB. 

Click [here](http:// https://camperhampers.herokuapp.com/) to view the website live. 

**For testing purposes, please use the following credit card details:**

`Card number:` 4242 4242 4242 4242
`Exp:` any date in the future using MM/YY format
`CSV:` any 3 numbers, ie 424


## Table of Contents:

* [User Experience](#User-Experience)
    * [User Stories](#User-Stories)
    * [Strategy Plane](#Strategy-Plane)
    * [Scope Plane](#Scope-Plane)
    * [Structure Plane](#Structure-Plane)
    * [Skeleton Plane](#Skeleton-Plane)
    * [Surface Plane](#Surface-Plane)

* [Existing Features](#Existing-Features)
    * [Features to consider implementing in the future](#Features-to-consider-implementing-in-the-future)

* [Technologies Used](#Technologies-Used)

* [Testing](#Testing)

* [Deployment](#Deployment)

* [Credits](#Credits)
    * [Content](#Content)
    * [Images](#Images)

* [Acknowledgements](#Acknowledgements)

## **User Experience**
This section provides insight into the UX process, focusing on Camper Hamper’s target audience, the main aims of the project and how the website can help users meet their needs.  

### User Stories

**New users:** 
* As a new user, I want to be able to register on the site. 
* I want to be able to log on and off the site after I have registered.
* I want to be able to receive confirmation emails when I register, and if I purchase any products.
* I would like to have a profile that stores my delivery information, as well as my order history.
* I want to be able to view all the hampers available, and also view by category and price. 
* I want to be able to click on a hamper and view more details about what is included. 
* I want to be able to easily navigate to my bag and see which products I have added to purchase. I also want to see how much the total is of the bag, and be able to add and remove items in the bag before I checkout. 
* I want to be able to search the site using key words.
* I want the site to be easy to navigate and intuitive.
* New user case story - I am going camping for the first time this year. We are hiring a campervan, and I have a lot of things to pack and organise. I really want to have some drinks and nibbles sorted for the first night so that we don’t have to worry about the hassle of where to go for food when we arrive at our destination. 
* New user case story - I am going away on a camping trip with some friends, and really want to have some drinks sorted for our first campfire as a treat for everyone. I am looking for a place to provide a selection of drinks we can all enjoy that can easily be transported from my tent over to the campfire. 
* New user case story - I am going away with small children. I am wondering about buying some treats for myself and my husband and also for the children. My friend recommended this website so I am interested in having a look to see what the company can offer.

**Returning user:**
* I have made a purchase and would like to go back into my account, log in  and easily look at my order history rather than going through my emails. 
* I previously purchased a hamper and was delighted with it, and would like to leave a testimonial on the website to help the company do well as I love supporting small independents.  


**Business Owner:**

* I am the creator of this app and want to see it succeed. I want the app to add value to the users and their camping experiences. I want to create a website that encourages users to make a purchase, and also to encourage users to easily return and purchase more hampers easily. Therefore I want the app to be fully responsive, fresh and modern in design, friendly and also intuitive to use. 
* As the business owner, I want to be able to add new hamper products easily, edit hamper products and delete hamper products that are no longer available or that I no longer want to sell.
* As the business owner, I want to users to leave real feedback via testimonials on the site. However, I also want to be able to manage these, therefore I want to have the ability to edit and delete these testimonials too.

### Strategy plane: 

I started the UX process by creating the User Stories above which helped me work out who the project was aimed at and what I would need to include in the website to satisfy the needs of the users. 

The website should be professional and user-friendly, providing an easy navigation journey to reach different sections with ease. 

**Project goals:**
* To provide the user with an online e-commerce store for purchasing savoury, sweet and campfire hampers tailored towards camping holidays. 
* To enable new users to be able to register for an account with Camper Hampers.
* For users who have already signed up previously, to be able to log in with ease
* For users that are logged in, to be able to easily view their own profile, where they can see their delivery information, and order history with ease. 
* For users that are logged in, to be able to easily share a testimonial about their experience on the website if they so wish. 
* For users that are logged in, to easily be able to log out.
* To provide direction to social media links, in order to expand followers and increase brand awareness
* To make Camper Hampers seem a reputable company in order to encourage users to sign up, by creating a professional website, whilst maintaining a friendly appeal. 

**Customer goals:**
* App designed with mobile-first approach
* User friendly navbar
* Enable users to easily scroll back to the top on longer pages
* Relevant social media icons provided in the footer
* Log in and register forms so the customer can sign up to have a Camper Hamper account.
* Customer profile page which enables the user to manage their own information easily and view order history easily.
* App is visually appealing, and fully responsive on all devices and screen sizes

### Scope plane:

The key features of the website were developed based on the main aims of the website and user needs, as well as my current skill-set of HTML, CSS, JavaScript, Python, Django and Heroku. Users should be able to do the following on the website:

* View a clear path on the homepage to view all hampers, or choose to filter the hamper products by category and price. On the homepage the user should be able to navigate to the Camper Hamper blog, and also view customer testimonials.  The user should easily be able to register for an account, or sign in, as well as viewing the total price of any products in their shopping bag.
* Visit the ‘Blog’ page, where the user can view the Camper Hampers blog created by the owners. 
* Visit the ‘Testimonials’ page where the user can view testimonials left by happy customers. 
* Users can choose to view all hampers, or they can easily view hampers by category by clicking on a category option in the nav bar. 
* Across the site, user should be able to search for a keyword, to then be shown results containing any hamper products that match their search. The user should then be able to reset the search to start another search if they wish. 
* Users that do not choose to create an account can still add a product to their bag, and complete checkout successfully. 
* Users who wish to create an account can complete a sign-up form by providing a username and password, which enables them to have a Camper Hamper account and profile on the website. 
* A user that has previously signed-up and is revisiting the site, should be able to easily log in by providing a username and password in the log in form. When on the log in page, if a new user has arrived here by accident, and they want to sign up instead, they should easily be able to navigate to the  ‘Register’ page instead. 
* Once they have signed up they can then start adding, editing and deleting their personal information on their profile, including their delivery address which will be stored for deliveries on future purchases. On their profile page they should also be able to access their order history, and leave a testimonial on the website too. 
* Once logged in, the user can click a button on their profile page which will take them to a page where they can fill out a form to add a testimonial to the Testimonials page on the website. They can click ‘Cancel’ if they change their mind, and return back to their Profile page, or once they click a button to submit the form, they are taken to the Testimonials page where they can see their added testimonial displayed. 
* When logged in, the user should be able to easily log out by clicking on the ‘Log Out’ option on the nav bar. When the user clicks to log out, they should be then taken to a page which asks them to confirm that they want to log out, and when they confirm this the user I taken to the homepage and is no longer logged in (and can no longer view their profile information). 

Therefore the user should be able to create their own account, successfully checkout and if they wish to add information to their Profile they can choose to do this (by clicking a tick button on the checkout page to save their details). They can then manage their own information by using the four CRUD functions, and easily navigate their way around the site. 

Additionally, the website needs to be set up for the business owner too so that they can manage certain parts of information. In particular, the business owner needs to have admin access to do the following:

* Add a product, delete a product, and edit a product. 
* Add a testimonial, delete a testimonial and edit a testimonial. 
* Add a blog post, edit a blog post and delete a blog post. 

The above mentioned features must not be accessible to non-admin users. 

### Structure plane:

Once I had worked out which features I'd like to include, I began to think about the information architecture and the different interactions that could take place across the site, and the order they should be in. 

The website is largely based on the Code Institute’s Boutiqe Ado project, therefore I knew I wanted to include many of the same features. Additionally I needed to develop the testimonials app, blog app and ensure that the business owners were able to access different parts of the site that other users could not. 
There needed to be two different presentable versions of the website, one that was accessible and an enjoyable experience for users visiting the website with open access and no account with Camper Hampers, and then a different experience for users that have created an account and logged in. Therefore I wanted to ensure that certain pages would be visible to everyone, and others would only be visible to those with an account and logged in. The ‘My Account’ option in the nav bar would therefore need to change when a user logged in, displaying certain pages only available to those with an account, and removing the ‘Sign Up’ option which would create a confusing user experience if logged in. 

As well as the sign up and log in forms, points of contact for users would also be provided in the links to social media in the footer. 

### Skeleton plane:

At this stage I was ready to put together wireframes. I used Figma for these, creating wireframes for the website on desktop, tablet and mobile all showing the five main sections. 

I wanted to make sure it would be easy for users to navigate between the pages, and therefore I decided it would be essential to create a fixed nav, as well as a nav that worked well on mobile. This would be similar to the Boutique Ado project. 

I wanted to ensure there would be a sticky footer as I knew on many pages there wouldn’t be a lot of content and I wanted this to still be a positive user experience. I also wanted the Blog and Testimonials to always be available to view on the footer. 

I decided that a 'Back To Top' button on the site would be useful on longer pages, such as the All Products page, the Testimonials page and the Blog page (which could grow to be much longer in the future). 

I decided a clean white background with a box layout would be a good way to present information in the different sections, allowing enough space between text, images and any key features. 

The wireframes can be viewed on [Figma](https://www.figma.com/file/giUuD5vECYMz4Z99Vt3HHw/Milestone-3?node-id=0%3A1)

### Surface plane:

I next moved on to the design work. 

* **Colours & Logo:** 
Colours were an important choice – I wanted the website to be modern, with colours based around camping to create a natural feel, for example a light green for nature, and pinks and dark purples similar to fire. I experimented with orange but this felt too bold. The images I chose from Pexels and Unsplash enabled me to choose the colour palette for the website, including the logo. I decided the logo would show the name of the company ‘CAMPER HAMPERS’. 

* **Typography:** I used Google Fonts to select the fonts for my project and decided on the font ‘Josefin Sans’for the logo and headings – I thought this worked well in uppercase and the design of the the ‘M’, ‘A’ reminded me of tents and yurts, therefore I thought this would be a good fitting. The font ‘Roboto’ complimented this for the body text. 

* **Images:**  The images used on the website are all from Pexel and Unsplash. I chose images of hampers, relevant food and drinks, as well as camping/campervan pictures for the blog and images of people smiling in the outdoors for the testimonials.

* **Layout:** I decided to keep the background clean, spacious and fresh by using a white background for the pages which enabled the images of products to stand out and meant the user was not distracted by busy pages. The testimonials and blog pages use Bootstrap cards to highlight the different content, with simple design to fit in with the rest of the site. 

**Database Structure**

Throughout the development stage of the project, SQLite3 was used as this is the default database included with Django. On deployment, you are given the option to utilise PostgreSQL as this is included with Heroku and this is what I chose to do.

I also relied on Django’s default user model for authorization, allowing me to meet one of the project requirements of separating features by anonymous users, users in session and superusers. Further information about this feature can be found here: [django.contrib.auth.models] (https://docs.djangoproject.com/en/3.0/ref/contrib/auth/).


Code Institute - Boutique Ado was used as a template for the majority of this project with the **Testimonials** and **Blog** models being added in to supplement the project.

### OwnerBlog Model

| Name          | Database Key  | Field Type | Type Validation |
| ------------- | ------------- | ---------- | --------------- |
| Blog Title         | blog_title | CharField  | max_length=254  |
| Blog Content | blog_content | TextField  | max_length=254  |


### Category Model

| Name          | Database Key  | Field Type | Type Validation |
| ------------- | ------------- | ---------- | --------------- |
| Name          | name          | CharField  | max_length=254  |
| Friendly Name | friendly_name | CharField  | max_length=254  |


### Product Model

| Name        | Database Key | Field Type    | Type Validation                                              |
| ----------- | ------------ | ------------- | ------------------------------------------------------------ |
| Category    | category     | ForeignKey    | "Category", null=True, blank=True, on_delete=models.SET_NULL |
| SKU         | sku          | CharField     | max_length=254, null=True, blank=True                        |
| Name        | name         | CharField     | max_length=254                                               |
| Description | description  | TextField     |                                                              |
| Price       | price        | DecimalField  | max_digits=6, decimal_places=2                               |
| Image_URL   | imge_url     | URLField      | max_length=1024, null=True, blank=True                       |
| Image       | image        | ImageField    | null=True, blank=True                                        |

### **Profiles** App

### UserProfile Model

| Name                    | Database Key            | Field Type    | Type Validation                              |
| ----------------------- | ----------------------- | ------------- | -------------------------------------------- |
| User                    | user                    | OneToOneField | User, on_delete=models.CASCADE               |
| Default Phone Number    | default_phone_number    | CharField     | max_length=20, null=True, blank=True         |
| Default Street Address1 | default_street_address1 | CharField     | max_length=80, null=True, blank=True         |
| Default Street Address2 | default_street_address2 | CharField     | max_length=80, null=True, blank=True         |
| Default Town or City    | default_town_or_city    | CharField     | max_length=40, null=True, blank=True         |
| Default County          | default_county          | CharField     | max_length=80, null=True, blank=True         |
| Default Country         | default_country         | CountryField  | blank_label="Country", null=True, blank=True |
| Default Postcode        | default_postcode        | CharField     | max_length=20, null=True, blank=True         |


### **Checkout** App

### Order Model

| Name            | Database Key    | Field Type                      | Type Validation                                                                      |
| --------------- | --------------- | ------------------------------- | ------------------------------------------------------------------------------------ |
| Order Number    | order_number    | CharField                       | max_length=32, null=False, editable=False                                            |
| User Profile    | user_profile    | ForeignKey                      | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' |
| Full Name       | full_name       | CharField                       | max_length=50, null=False, blank=False                                               |
| Email           | email           | EmailField                      | max_length=254, null=False, blank=False                                              |
| Phone Number    | phone_number    | CharField                       | max_length=20, null=False, blank=False                                               |
| Country         | country         | CountryField                    | blank_label='Country\*', null=False, blank=False                                     |
| Postcode        | postcode        | CharField                       | max_length=20, null=True, blank=True                                                 |
| Town or City    | town_or_city    | CharField                       | max_length=40, null=False, blank=False                                               |
| Street Address1 | street_address1 | CharField                       | max_length=80, null=False, blank=False                                               |
| Street Address2 | street_address2 | CharField                       | max_length=80, null=False, blank=False                                               |
| County          | county          | CharField                       | max_length=80, null=True, blank=True                                                 |
| Date            | date            | DateTimeField auto_now_add=True |                                                                                      |
| Delivery Cost   | delivery_cost   | DecimalField                    | max_digits=6, decimal_places=2, null=False, default=0                                |
| Order Total     | order_total     | DecimalField                    | max_digits=6, decimal_places=2, null=False, default=0                                |
| Grand Total     | grand_total     | DecimalField                    | max_digits=6, decimal_places=2, null=False, default=0                                |

### OrderLine Model

| Name           | Database Key   | Field Type   | Type Validation                                                                    |
| -------------- | -------------- | ------------ | ---------------------------------------------------------------------------------- |
| Order          | order          | ForeignKey   | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| Product        | product        | ForeignKey   | Product, null=False, blank=False, on_delete=models.CASCADE                         |
| Product Size   | product_size   | CharField    | max_length=2, null=True, blank=True                                                |
| Quantity       | quantity       | IntegerField | null=False, blank=False, default=0                                                 |
| Lineitem Total | lineitem_total | DecimalField | max_digits=6, decmial_places=2, null=False, blank=False, editable=False            |




[Back to Contents](#contents)

 

**Existing Features** 

* **Fixed navigation** - allows the user to easily navigate to different sections of the website and in particular search for products, view products, view total of items added to bag, click on their bag which can take the user through to checkout, and view their profile – these features are available to the user on the nav bar across all pages. 
* **'Back to top' button** - enables users to quickly move back to the top of the page rather than scrolling back up on longer pages or pages which may have longer content in the future (blog page for example).
* **Colour palette** used logically across the site, for example the colour of the Testimonials section on the homepage takes the user to the Testimonials page which shows cards with the same background colour displaying the testimonials. The colour used for the Blog on the homepage is also similar to the colour used on the Blog page (however the shade is slightly lighter to enable easier reading). 
* **Bootstrap Toasts** used for all flashed messages after user has completed an action.
* **Search bar** on the abovementioned navbar sits at the top of the screen and is linked to keyword searches. 
* **Home** - The user sees an image and introductory title explaining the purpose of the website. The user contains a CTA which links to the products page. When scrolling down, the user is then presented an option to click on a button to view the Camper Hampers blog, and further down the user can also click to view a page containing Customer Testimonials. 

* **Log In page** - This feature contains a log in form where an existing user can input their username and password to log in. Once details have been entered, the user can click on ‘Submit’ and this queries the DB to see if the user already exists. If they enter the wrong password and/or username, they are shown a message telling the username that the details are incorrect and to try again. Users on this page that don’t yet have an account are prompted to sign up with a message and sign up button underneath the log in form.  Once users successfully log in, they are taken to the home page.

* **All Products page**

- Bootstrap cards with Basic product information: Image, Product Name, Price and Category.
- Clicking the image takes the user to the specific product detail page.
- Clicking the Category name will filter, and display, all the products for that Category (categories include Savoury, Sweet and CampFire).
- Sort dropdown allows the user to manipulate the display by Name, Category, and Price - this also reversed.
- Back to Top button at the bottom right of the screen.
- If the user is a SuperUser, they ‘Edit’ and ‘Delete’ links are displayed to allow easy management of products. 

 

* **Product Detail page**
- The user will see a larger product image along with the Product Name, Product Description, Price and Category of the product. 
- The user can edit the quantity of the product displayed, by using the increase and decrease quantity icons which are placed either side of Number Input Field. This field can also be updated by using the up/down arrows that appear.
- The user can choose to click a button to add the product(s) to their bag or they can click a button to keep shopping – these options are available below the quantity input field.
- ‘Keep Shopping’ button returns the user to the All Products page and ‘Add to Bag’ button adds items to the bag which then displays a Bootsrap Toast confirming success of the action. The bag then keeps a running bag total and display of the contents as the user adds or removes items to the bag whilst on the site. 


* **Bag page**

- The user is shown a summary of the items in their bag, including product image, description, price and quantity. 
- The user will be able to adjust the quantity of the items in the bag using the increase/decrease icons and clicking the update link or remove the whole line by clicking the remove link.
- The buttons at the bottom allow the user to confirm that they wish to proceed to secure checkout, which if clicked takes the user to the checkout page or to the user can choose to return to the All Products page.
- There is a back to top button added on this page, in case the user adds several items and in particular is viewing on a smaller screen – the back to top button should enable easy navigation for the user rather than scrolling back up should they wish to return to the top of the page. 



* **Checkout page**
- The user can view several sections of information on this page, including user details and delivery details, as well as an order summary. 
- The user is required to complete the checkout form before being able to continue the checkout process. This includes completing required fields (the user is shown a message if they try to submit the form and haven’t completed them, asking then to complete the required fields in order to continue, otherwise the user cannot submit the form). 
- If the user has created an account, they can choose to save their details on this form to their profile. 
- `STRIPE` provides credit card validation to the credit card field on the form. 
- The right hand column displays the user bag information so they are able to double check what they are purchasing.
- Once the user submits the payment information an opaque spinning overlay appears to show that the payment is being processed.


* **Checkout success page**
- The user is presented with a summary of their purchase, including order number and contact details and a Thank You message.
- A Bootstrap Toast also displays to say that the order has been processed and that a confirmation has been sent to the user’s email.
- A button under the summary enables to user to return to the All Products page. 

* **My Profile page**

-	The user is presented with a question asking if they have been happy with their hampers, and if so they can click on a button to ‘Leave a Testimonial’ which takes the user through to a page where they can add a testimonial. 
-	Under this the user can view their default delivery information, which is stored in their profile for delivery on future orders.
-	The user can also view their Order History, including an Order Number, the Date the order was made, the items purchased and the total cost of the order. 

*  **Testimonials page**

-	The user can see an image of people smiling along with an introductory title and text
-	Underneath the user can see a list of different testimonials displayed simply in cards with a border for easy reading. The testimonials include a title, testimonial text, and the name of the author. 
-	If the user is a superuser, they can click on ‘Edit’ on each card which takes them to a page with a prefilled Edit form, where they can edit the testimonial. 
-	Similarly, if the user is a superuser, they can click on ‘Delete’ on each card which removes the testimonial from the page (and the database). 
-	Bootstrap Toasts display messages to the superuser if they edit or delete a testimonial to confirm their actions. 
-	If the site admin wishes to add a testimonial to the page, they can easily click on the ‘My Account’ dropdown and click on ‘Admin Add Testimonial’, which takes them through to the page containing a form to add a testimonial. 
-	At the bottom of the page the user can choose to return to the Home page or choose to View Hampers.

*  **Blog page**

-	The user can see an image of a tent in the woods, along with an introductory title and text
-	Underneath the user can see an introductory blog article from the author, which includes blog title, blog text and the date posted. 
-	 If the user is a superuser, they can click on ‘Edit’ on each blog post which takes them to a page with a prefilled Edit form, where they can edit the blog post. 
-	Similarly, if the user is a superuser, they can click on ‘Delete’ on each blog post which removes the blog post from the page (and the database). 
-	At the bottom of the page the user can choose to return to the Home page or choose to View Hampers.
-	

* **Sign Up** 

- This feature contains a form where the user can input a username and password in order to create an account. If they enter a username that already exists, they are shown a message explaining this and asking them to try again. Once the user clicks on ‘Sign Up’, the user is sent an email which contains a link they have to click on in order to confirm registration. The link in the email takes the user to a page on the site where they can confirm their registration. Once confirmed, the user is taken to the Products page.  


* **Log Out** 

- This feature appears in the nav bar under My Account when a user is logged in.
- This page can only be accessed by users that are not authenticated.
- The page includes a prompt that confirms that a user really does want to leave the site, with a 'Log Out' button to do so.
- Once signed out, users are redirected back to the Home page and they can no longer view their My Profile page. 


* **Footer** - the footer contains social media icons with links to social media pages that open up in a new page. The Footer also contains an e-mail link in case users want to make contact by email. Also in the Footer there are links to view the ‘Testimonials’ page and the ‘Blog’ page. These were placed here rather than the main nav bar so as not to distract the user from browsing products, but also to make sure the user has access to these pages wherever they are on the site. 

#### Error pages: 404 and 500 pages

- Built with the same structure as the auth pages, these two pages have a large hero image with a textbox notifying the user of the issue they have come across.
- As well as the error message, they also feature buttons to take users back to the home page and include the hotel's email address if users want to get in touch.


### Features to consider implementing in the future:

* A future feature to add would be a Contact Us page along with a contact form.
* Additionally it would be good if there was a blog sign-up form, so that the company could collect data for future marketing. The user would then be emailed when a new blog post was published, and also this would be a way of communicating any further marketing information at the same time. The company could also use these details for asking customers to leave a testimonial if they hadn’t already done so. 
* The blog could be developed much further. For example, as more blog posts are published, it would be good if there was a category option added to the model, so that the admin could choose to select from a range of options such as ‘hampers’, ‘camping’, ‘general’ and ‘news’. A search bar to enable the user to then search the content of the blog page would also be brilliant. And it would be useful if the user could filter the blog by category. 
* It would be great if users could select an image to upload when leaving a testimonial too, in addition to their text. 


## Technologies Used 

### Languages, libraries, databases, frameworks, editors, version control and deployment

- [HTML5](https://www.w3schools.com/html/)
    * The language used to create the content to the website and add structure.
- [CSS3](https://www.w3schools.com/css/)
    * The language used to add styling to the site.
- [JavaScript](https://www.w3schools.com/js/DEFAULT.asp)
    * The language used to make the site interactive.
- [jQuery](https://jquery.com/)
    * I used the jQuery library to help write the JavaScript code used in this project.
- [Python](https://www.python.org/)
    * The programming language used to create the back-end function and the logic of the site.
- [Django](https://www.djangoproject.com/)
    * The web framework used to allow a modular site to be created.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    * Django Crispy Forms were used to style the Django forms used throughout the site.
- [SQLite](https://docs.djangoproject.com/en/3.2/ref/databases/#sqlite-notes)
    * I used Django's built-in SQLite3 database during production and added data through Django's admin panel when authorised as a superuser.
- [PostgresSQL](https://www.heroku.com/postgres)
    * For deployment, I used a Postgres database offered by Heroku. I then added the same data again through Django's admin panel, with the same process that I had followed during production on the SQLite 3 database.
- [Gunicorn](https://gunicorn.org/)
    * The Python WSGI (Web Server Gateway Interface) HTTP Server used in deployment to Heroku.
- [Psycopg2](https://pypi.org/project/psycopg2/)
    * Psycopg2 was used to adapt Python to the PostgreSQL database.
- [Bootstrap framework](https://getbootstrap.com/) 
    * Used for responsive grid framework, toasts, cards, navbar and to ensure a ‘mobile first approach’. 
- [Visual Studio Code](https://code.visualstudio.com/) - IDE used for code editing.
- [Git Version Control](https://git-scm.com/)
    * I used Git for Version Control to track and record changes to my code and refer back when needed.
- [GitHub](https://github.com/)
    * I used GitHub as my remote repository, to push to and store the commited changes to my app from Git.
- [Heroku](https://www.heroku.com/)
    * I used Heroku as a hosting platform to deploy the live version of my website. 

### Additional tools used
- [Stripe](https://stripe.com/en-se)
    * Stripe was used to add the secure payment feature to the site.
- [AWS S3 Bucket](https://aws.amazon.com/s3/)
    * - used the S3 and IAM modules for storage and user access.
- [Gmail](https://www.google.com/intl/sv/gmail/about/#)
    * Google's free email service used to send confirmation emails to users who have made reservations.
- [Figma](https://www.figma.com/) 
    * Figma helped me design my project, by creating wireframes for desktop, tablet and mobile devices. 
- [FontAwesome](https://fontawesome.com/) 
    * icons were taken from this site for the forms, header, footer and buttons, as well as to add some styling to the blog and testimonial pages. 
- [Google Fonts](https://fonts.google.com/)
I used two complementary fonts from Google for my project: Josefin Sans and Open Sans. 
- [Favicon](https://favicon.io/)
    * I used this website to create the favicon for the website 
- [W3C Markup Validation Service](https://validator.w3.org/) 
    * I used this tool to check whether there were any errors in my HTML and CSS code (as discussed in more detail in the Testing section).
- [JSHint](https://jshint.com/) 
    * This tool helped me test my JavaScript and jQuery code (explained in more detail in the Testing section). 
- [PEP8 online](http://pep8online.com/)
    * I used PEP8 to check that my Python code complied with formatting standards. 


**Resources**

* [Code Institute Course Content Boutique Ado](https://courses.codeinstitute.net/) – This website was possibly mostly thanks to the Code Institute’s Boutiqe Ado project, and the main structure and model was taken from this. 
part of the course 
* Code Institute **SLACK Community** - General resource
* [Stack Overflow](https://stackoverflow.com/) – General resource
* [W3C Schools](https://www.w3schools.com/) 
* [CSS-Tricks](https://css-tricks.com/) - General resource
* [Am I Responsive](http://ami.responsivedesign.is/) - Responsive website mockup image generator.


## Testing:

Testing documentation can be found on a separate document [here](https://github.com/chloelewisdev/milestone-project-4/blob/master/testing.md)

As mentioned above the following were used to test the code on the site:

- [W3C Markup Validation Service](https://validator.w3.org/) 
    * This was a great tool throughout the project to check whether there were any errors in my HTML and CSS code (as discussed in more detail in the Testing section).
 - [JSHint](https://jshint.com/) 
    * This tool helped me test my JavaScript and jQuery code (explained in more detail in the Testing section). 
- [PEP 8 online](http://pep8online.com/)
    * I used PEP 8 to check that my Python code complied with formatting standards. 


## **DEPLOYMENT**

### Hosting

The site is hosted on [Heroku](https://www.heroku.com/home).

Deployment of the site was achieved by following the steps below:

- Created a new repository within GitHub.
- Opened repository in my IDE of choice – in my case Visual Studio Code - by cloning the repo from GitHub.
- Created a requirements.txt file by typing `pip3 freeze > requirements.txt` in the terminal which tells Heroku what dependencies are required.
- Created a Procfile and added `web: gunicorn deli_sw.wsgi:application` to the file.
- Checked the Procfile to make sure there is no extra line after the first line as this can confuse Heroku.
- Push the requirements.txt and Procfile to GitHub.
- Logged in to Heroku and selected "Create New App".
- Selected the input field "App Name" and gave app a unique name.
- Selected the region closest to my location
- Clicked "Create App".
- Clicked "Resources" and typed in Postgres in the Add-ons search bar.
- Selected Heroku Postgres and provisioned a free Hobby Dev database.
- Retrieved the Database URL from the hidden Config Vars in "Settings".
- Pasted the Database URL in the database path in settings.py and removed the local settings.
- Run migrations to build the database in Postgres.
- Created a superuser with `python manage.py createsuperuser` and followed the instructions in the terminal.
- Removed the Postgres Database URL so it doesn't end up in version control.
- Typed `heroku config:set DISABLE_COLLECTSTATIC=1` in the terminal to stop Heroku collecting the static files.
- Pushed all changes to GitHub.
- Typed `git push heroku master` to push everything to Heroku.
- Selected "Deploy" from the Heroku App menu.
- Selected "GitHub" from the "Deployment Method" part of the page.
- Ensured my GitHub profile name was showing in the "Connect to GitHub" section and inserted my GitHub repo name in the input field and clicked "Search".
- Once Heroku had found my repo, I clicked "Connect" to complete the process.
- Selected "Settings" from the Heroku App menu.
- Selected "Reveal Config Vars" and added the relevant key/value information for the following:

| Config Var            | Key                                                                               |
| --------------------- | --------------------------------------------------------------------------------- |
| AWS_SECRET_KEY_ID     | obtained when you set up AWS                                                      |
| AWS_SECRET_ACCESS_KEY | obtained when you set up AWS                                                      |
| DATABASE_URL          | created when you provisioned Postgres                                             |
| EMAIL_HOST_PASS       | obtained from email provider                                                 |
| EMAIL_HOST_USER       | email address                                                                |
| SECRET_KEY            | obtained from [miniwebtool](https://miniwebtool.com/django-secret-key-generator/) |
| STRIPE_PUBIC_KEY      | obtained from STRIPE                                                              |
| STRIPE_SECRET_KEY     | obtained from STRIPE                                                              |
| STRIPE_WH_SECRET      | obtained from STRIPE                                                              |
| USE_AWS               | True                                                                              |

- Selected "Deploy" from the Heroku App menu.
- Scrolled down the page and selected "Enable Automatic Deployment".
- Selected Master Branch under "Branch Selected".
- Clicked "Deploy Branch" 
- Once site was deployed, clicked "View" to launch the app and be able to view it within the browser.
- Heroku now updates automatically every time you push to GitHub.

[Back to Contents](#contents)

### AWS

In order for the static css, js and media files to be stored and useable with Heroku, it was necessary to set up an AWS account.

- Go to [AWS](aws.amazon.com) and either log in or create an account.
- Search for S3.
- Create a new bucket and ensure that the `Block All Public Access` tickbox is unchecked and click 'Create Bucket`.
- Click on the Properties tab and enable `Static Website Hosting`. This will allow AWS to host our static files.
- Input `index.html` and `error.html` in the appropriate fields and hit save.
- Click on the Properties tab and click CORS configuration and add the below before hitting save:

  ```
  [
  {
  "AllowedHeaders": [
  "Authorization"
  ],
  "AllowedMethods": [
  "GET"
  ],
  "AllowedOrigins": [
  "*"
  ],
  "ExposeHeaders": []
  }
  ]
  ```

- Click the Policy Tab and select Policy Generator which creates a security policy for the bucket.
- The policy type is S3 Bucket Policy and the Action will be `get object`.
- Copy the ARN (Amazon Resource Name) from the bucket and paste it in the ARN field.
- Click `Add Statement` and then `Generate Policy`.
- Copy the generated policy into the Bucket Policy Editor.
- Add `/*` at the end of the resource key as this will allow access to all resources in the bucket.
- Click Save.
- Click the Access Control tab and set the list object permission to everyone under the Public Access section.
- Open IAM from the service menu.
- Create a group for your user to belong to.
- Create an access policy for you the group which gives access to the S3 bucket.
- Click the JSON tab and select import managed policy, search for S3 and select S3 Full Access Policy.
- Create a user, give them programmatic access and attach it to the group.
- Download the CSV file that is generated as this contains the keys required to use AWS.
- Install boto3 and django-storages using `pip3 install`.
- Add the keys to the Config Vars in Django.
- Create a custom_storage file.
- Run `python manage.py collectstatic` and transfer the static info to AWS.

- [Back to Contents](#contents)

###  LOCAL HOSTING

If you wish to clone a copy of my project, feel free. You will need to:

- Navigate to my GitHub [repository]( https://github.com/chloelewisdev/milestone-project-4).
- Click the `Code` button next to the Green Gitpod button.
- Either, download the zip file or clone the repo using `gh repo clone chloelewisdev/milestone-project-4` in the terminal.
- Install the modules listed in the requirements.txt file using `python -m pip -r requirements.txt` in the terminal.
- Install the JSON files using `python manage.py loaddata categories`,  and `python manage.py loaddata products` in this order as "products" relies on the previous two.
- Create a SuperUser by using `python manage.py createsuperuser` and following the onscreen instructions.
- Run migrations to create your database by using `python manage.py migrate`
- Create an env.py file in your application folder and add the following:

  ```
  import os

  os.environ.setdefault(
  "SECRET_KEY", "ADD YOUR SECRET KEY HERE"
  )
  os.environ.setdefault(
  "STRIPE_PUBLIC_KEY",
  "ADD YOUR STRIPE PUBLIC KEY HERE,
  )
  os.environ.setdefault(
  "STRIPE_SECRET_KEY",
  "ADD YOUR STRIPE SECRET KEY HERE",
  )
  os.environ.setdefault("STRIPE_WH_SECRET", "ADD YOUR STRIPE WEBHOOK SECRET HERE")

  os.environ.setdefault("EMAIL_HOST_PASS", "ADD YOUR EMAIL HOST PASSWORD HERE")

  os.environ.setdefault("EMAIL_HOST_USER", "ADD YOUR EMAIL HOST USERNAME HERE")

  ```

- The app can now be run locally by typing python manage.py in the terminal and will be available in your browser using the address `http://127.0.0.1:8000`.

[Back to Contents](#contents)

## Credits

### Content

The content of this website is entirely fictional and written by myself.

### Images

- The images are all from [Pexels](https://www.pexels.com/) and [Unsplash] (www.unsplash.com), which is an open source library of photos, images and videos.

### Acknowledgements

A big thank you to the brilliant support from the *Code Institute* tutors, who were very helpful at pointing me in the right direction when trying to debug code.


Thanks to the Code Institute Slack Community.


Thanks also to my family and friends for taking the time to look over the website, test the features and for providing feedback.


