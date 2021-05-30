## Testing

- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-testing)
  - [Code Validation](#code-validation)
  - [Browser Validation](#browser-validation)
  - [Responsive Testing] (#responsive-testing)
- [User Testing](#user-testing)
  - [Peer Testing](#peer-testing)
  - [User Testing](#user-testing)

To return to the previous document, click [here]( https://github.com/chloelewisdev/milestone-project-4/blob/master/README.md).


### **Manual Testing**

- Chrome Developer Tools were used to test responsiveness of all pages on all screen sizes.
- Physical testing was carried throughout the whole process on Desktop, Tablet(iPad) and iPhone.
- All links were tested manually to ensure they worked on all devices.
- All buttons were tested manually to ensure they worked on all devices.
- NavBar was tested to ensure it worked on all devices.
- All CRUD functions were tested to ensure they worked on all devices.

#### Issues found from manual testing:
I realised that when physically viewing the dropdown items on mobile, the menu items were difficult to select as they were too close to each other, meaning the user could click on the wrong link and a frustrating user experience. I therefore added extra padding here to allow for more space between the items and to improve the user experience. 


### Automated Testing

#### Code Validation

**HTML**

I validated the HTML pages with the [W3C Markup Validation Service](https://validator.w3.org/)

Whilst doing this a few errors were brought up throughout the project relating to using Django templates. These included:
- An issue in using '{}' brackets as part of the source for elements. However, this syntax is necessary to access static files and urls and was therefore ignored.
- All html templates led to errors that the doctype and language were not declared. As the templates were based on the base.html template where these were addressed, this issue was also ignored.
- It showed that a ``<li>`` existed for the mobile nav without a ``<ul>`` tag, therefore I updated the code for this in the mobile_top_header.html file and the error was resolved. 
- blog.html : Duplicate ‘class=’ on line 25 – removed this. Also there was a stray end div tag on line 76 which I removed. 
- edit_blog.html – unclosed div element on line 18, which I resolved. 
- new_blog.html – also an unclosed div element on line 14 which I resolved. 
- testimonials.html – also an unclosed div element on line 73 which was removed. 

**CSS**

I validated the CSS files with the [W3 CSS Validation Service](https://jigsaw.w3.org/css-validator/)

No errors were presented. 


**JavaScript**

I used [JSHint](https://jshint.com/) to check my JavaScript files.
- *script.js* - no errors were shown for this file

**Python**

I used [Pep8online](http://pep8online.com) check my Python app.py file

This returned indentation errors and warnings that some lines that were too long within a few files. There were also a few files where two lines had not been added before a class was defined. These errors were all corrected. 


### Browser Validation

I manually tested the website on the following browsers:
* Chrome
* Safari
* Mozilla Firefox

### Responsive Testing

* I manually tested the website by using Google Developer Tools to check each individual section and the website as a whole worked on different devices and different screen sizes, including: Moto G4, Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 5 SE, iPhone 6/7/8, iPhone 6/7/8 Plus, iPhone X, iPad, iPad Pro, Surface Duo and Galaxy Fold. I also manually tested the site on my MacBook Air, iPad, and iPhone 11.
* By using Google Developer Tools I checked that all of the form were displayed correctly, as well as the flash messages, search results, and tips.  
* I asked family to visit the website on their devices including a variety of mobiles and tablets, interact with the page and sign up. 

### **User Testing**

### Peer Testing
* I asked members of the May2020 group on the Code Institute's Slack community to test the site. One point that was raised was to ensure that the social links in the footer opened up new pages, which I then changed in the code. 

### User Testing

#### New users

* ***As a new user, I want to be able to register on the site.*** This user can click on the dropdown link under 'My Account' on the nav bar and choose to 'Register' where they are taken to a page to complete registration.
* ***I want to be able to log on and off the site after I have registered.*** The user can choose to 'Login' from the link under My Account in the nav bar at any time, and once logged in, the user is given an option under 'My Account' to Logout. 
* ***I want to be able to receive confirmation emails when I register, and if I purchase any products.*** When the user registers, they are sent a confirmation email which contains a link they need to click on to complete registration. If a user makese a purchase, they are sent a confirmation email of their order. 
* ***I would like to have a profile that stores my delivery information, as well as my order history.*** A user that has signed up for an account can view their 'My Profile' page, which contains their stored address information for default delivery, and also shows their order history. 
* ***I want to be able to view all the hampers available, and also view by category and price.*** The user can select at any time on the account from the nav menu to view 'All Hampers', or to select by category, or to filter by category and price. 
* ***I want to be able to click on a hamper and view more details about what is included.*** The user can click on a product, which then takes them to a product detail page where they can read a more detailed description about the product.  
* ***I want to be able to easily navigate to my bag and see which products I have added to purchase. I also want to see how much the total is of the bag, and be able to add and remove items in the bag before I checkout.*** The user can click on the 'bag' icon at the top of the screen at any time whilst on the site. If they have added items a running total is always displayed. If they click on the icon, the user is then taken to a page which shows them the details of the items in their shopping bag. Here the user can add more of a product or remove the product from their bag. If they wish to checkout they can click on a button on this page to checkout, or they can return to the Products page to keep shopping. 
* ***I want to be able to search the site using key words.** A search bar is made available to the user in the nav menu at the top which means they can access this at any time on the site. The search bar shows 'Search Hampers' so that the user knows this tool is specifically for searching hampers.
* ***I want the site to be easy to navigate and intuitive.*** The site is responsive on all screen sizes and browsers, ensuring a good user experience. Additionally, the buttons are clear with consistent styling and help to guide the user through their journey on the site. 
* ***New user case story - I am going camping for the first time this year. We are hiring a campervan, and I have a lot of things to pack and organise. I really want to have some drinks and nibbles sorted for the first night so that we don’t have to worry about the hassle of where to go for food when we arrive at our destination.*** This user can come to the site, and can use the search bar to find products that match their needs - for example typing in 'drinks' or 'nibbles' to see if there are any hampers that match. Additionally this user can filter the hampers by category if they wish. 
* ***New user case story - I am going away on a camping trip with some friends, and really want to have some drinks sorted for our first campfire as a treat for everyone. I am looking for a place to provide a selection of drinks we can all enjoy that can easily be transported from my tent over to the campfire.*** This user can type 'drinks' in the navbar search feature to see the hampers offering drinks.  
* ***New user case story - I am going away with small children. I am wondering about buying some treats for myself and my husband and also for the children. My friend recommended this website so I am interested in having a look to see what the company can offer.*** This user can use the categories filter to help with their search, additionally the user could use the 'search' function to see if there are any hampers with 'treats'.

**Returning user:**
* ***I have made a purchase and would like to go back into my account, log in  and easily look at my order history rather than going through my emails.*** This user can log in by clicking on the link under 'My Account', once they have logged in they can view the 'My Profile' page which will show all of their past orders.  
* ***I previously purchased a hamper and was delighted with it, and would like to leave a testimonial on the website to help the company do well as I love supporting small independents.*** If this user is logged in, they can click on the link in their 'My Profile' page which says 'Leave a Testimonial'. Here they are taken to a page where they can complete a short form to add a testimonial, then they can click on 'Add Testimonial' and it will be published on the website's 'Testimonials' page.  


**Business Owner:**

* ***I am the creator of this app and want to see it succeed. I want the app to add value to the users and their camping experiences. I want to create a website that encourages users to make a purchase, and also to encourage users to easily return and purchase more hampers easily. Therefore I want the app to be fully responsive, fresh and modern in design, friendly and also intuitive to use.*** The creator should be happy as the site is responsive, intuitive and allows for a positive user experience. Additionally the website is professional yet maintains a natural feel to keep with the aesthetics of the brand. 
* ***As the business owner, I want to be able to add new hamper products easily, edit hamper products and delete hamper products that are no longer available or that I no longer want to sell.*** Once logged in, the business owner has special permissions which enables them to access certain pages and features that regular users cannot. Under the 'My Account' option in the navbar, the business owner can choose the option 'Admin Add Product' which takes them to a page where they can add new hamper products, along with category, SKU, price, description and image. The business owner, the 'superuser' can also click on 'edit' on any product on the All Products page or Product Details page, which takes them to a page with a form pre-filled with the current information. Here they can edit the details and then click save, or cancel if they wish. The superuser can also click on 'delete' which appears under any product on the All Products page or the Product Detail page, which will remove the product from the site. The superuser is provided with flash toast messages after any action has been completed. 
* ***As the business owner, I want to enable users to leave real feedback via testimonials on the site. However, I also want to be able to manage these, therefore I want to have the ability to edit and delete these testimonials too.*** The superuser is provided with an 'edit' or 'delete' option under each testimonial once logged in. If they click edit, they are taken to a page containing the current testimonial, which they can edit and then save, with the new information being shown on the Testimonials page. If the superuser decides to click on 'delete', then the tesitmonial is removed. The superuser is provided with flash toast messages after any action has been completed.  Additionally the superuser can choose to 'Admin Add Testimonial' from the dropdown link under 'My Account', should they wish to add a testimonial they have received themselves.

* ***As the business owner, I want to be able to easily add blog posts, and edit or delete these at a future date if needed.*** The superuser can click on 'Admin Add Blog Post' from under the 'My Account' option in the nav bar. Here they are taken to a page where they can complete a form to add their new blog article. Once they save it it is shown on the website's 'Blog' page. On the blog page, the superuser is given the chance to 'edit' or 'delete' the blog posts if they wish. If they click edit then they are taken to a page where they can edit a pre-filled form containing the current blog post. 

To return to the previous document, click [here]( https://github.com/chloelewisdev/milestone-project-4/blob/master/README.md)
