1. [Validation](#validation) 
   - [html validator](#html)
   - [css validator](#css)
   - [python Pep8 complience](#pep8) 
   - [javaScript jshint complience](#javscript) 
2. [Lighthouse reports](#lighthouse)
3. [Testing user stories](#stories)
   - [Viewing and navigition](#nav) 
   - [Sorting and searching](#search) 
   - [Registration and User Account](#account)
   - [Purchasing and check out](#order)
   - [Contact and booking](#booking)
   - [Adding content](#content)
4. [Manual Testing](#Tesing)
5. [Further testing](#further)
6. [Bugs](#bugs)

# 1. Validation <a id="validation"></a>

I used the W3C Markup and CSS Validator Service to ensure there were no syntax errors throughout my website.

# Html <a id="html"></a> 

| ![index page validation]() |
|:--:|
| <b>Index page validation - Passed  - No errors or warnings</b>|

![Products page validation]() |
|:--:|
| <b>Products page validation - Passed  - No errors or warnings</b>|

![Products details page validation]() |
|:--:|
| <b>Products details page validation - Passed  - No errors or warnings</b>|

![Taproom page validation]() |
|:--:|
| <b>Taproom page validation - Passed  - No errors or warnings</b>|

![Our Story page validation]() |
|:--:|
| <b>Ourstory page validation - Passed  - No errors or warnings</b>|

![Contacts page validation]() |
|:--:|
| <b>Taproom page validation - Passed  - No errors or warnings</b>|

![Events Page validation]() |
|:--:|
| <b>Events page validation - Passed  - No errors or warnings</b>|

## CSS <a id="css"></a>

 ![CSS validation](/assets/screenshots/cssval.png) |
|:--:|
| <b>CSS validation  - Passed  - All errors and warnings are from the Font Awessome and Bootstrap CSS files</b>|

## Python Pep8 complience <a id="pep8"></a>

I used the Pep8 validator to to ensure there were no syntax errors in my python code

### Booking app files 

![models.py file validated]() |
|:--:|
| <b>models.py file validated  - Passed  </b>|

![urls.py file validated]() |
|:--:|
| <b>url.py file validated  - Passed  - </b>|

![viewss.py file validated]() |
|:--:|
| <b>models.py file validated  - Passed  - </b>|

### contact app files 

![models.py file validated]() |
|:--:|
| <b>models.py file validated  - Passed  </b>|

![urls.py file validated]() |
|:--:|
| <b>url.py file validated  - Passed  - </b>|

![viewss.py file validated]() |
|:--:|
| <b>models.py file validated  - Passed  - </b>|

![forms.py file validated]() |
|:--:|
| <b>models.py file validated  - Passed  - </b>|


### events app files 

![models.py file validated]() |
|:--:|
| <b>views.py file validated  - Passed  </b>|

![urls.py file validated]() |
|:--:|
| <b>url.py file validated  - Passed  - </b>|

![viewss.py file validated]() |
|:--:|
| <b>models.py file validated  - Passed  - </b>|

![forms.py file validated]() |
|:--:|
| <b>forms.py file validated  - Passed  - </b>|

### Newsletter app files 

![models.py file validated]() |
|:--:|
| <b>views.py file validated  - Passed  </b>|

![urls.py file validated]() |
|:--:|
| <b>url.py file validated  - Passed  - </b>|

![viewss.py file validated]() |
|:--:|
| <b>models.py file validated  - Passed  - </b>|

![forms.py file validated]() |
|:--:|
| <b>forms.py file validated  - Passed  - </b>|


### Home app files 

![models.py file validated]() |
|:--:|
| <b>views.py file validated  - Passed  </b>|

![urls.py file validated]() |
|:--:|
| <b>url.py file validated  - Passed  - </b>|


## JavaScript jshint complience <a id="javascript"></a>

I used the jShint validator to to ensure there was no syntax errors in my JavaScript code

![stripe_elements.js validated](/assets/screenshots/jshint.png) |
|:--:|
| <b>stripe_elements.js validated  - Passed  - unused variables are on onclick functions</b>|

# 2. Lighthouse Testing <a id="lighthouse"></a>

All my pages have went through google devtools lighthouse analysis which are scored on: 
* Performance 
* Accesibility 
* Best Practices 
* Search Engine Optimization (SEO)

![home page lighthouse scores]() |
|:--:|
| <b>Home page lighthouse scores - All fine  - Best pratices low due to front-end JavaScript libraries with known security vulnerabilities. this is from the Jquery need by libary from bootsrap</b>|

![Products page lighthouse scores]() |
|:--:|
| <b>Products page lighthouse scores - All fine  - Best pratices low due to front-end JavaScript libraries with known security vulnerabilities. this is from the Jquery need by libary from bootsrap</b>|

![Taproom page lighthouse scores]() |
|:--:|
| <b>Taproom page lighthouse scores - All fine  - Best pratices low due to front-end JavaScript libraries with known security vulnerabilities. this is from the Jquery need by libary from bootsrap</b>|

![Our Story page lighthouse scores]() |
|:--:|
| <b>Taproom page lighthouse scores - All fine  - Best pratices low due to front-end JavaScript libraries with known security vulnerabilities. this is from the Jquery need by libary from bootsrap</b>

![Contact page lighthouse scores]() |
|:--:|
| <b>Contact page lighthouse scores - All fine  - Best pratices low due to front-end JavaScript libraries with known security vulnerabilities. this is from the Jquery need by libary from bootsrap</b>|

![Taproom bookinG page lighthouse scores]() |
|:--:|
| <b>Taproom booking page lighthouse scores - All fine  - Best pratices low due to front-end JavaScript libraries with known security vulnerabilities. this is from the Jquery need by libary from bootsrap</b>|

![Brewtour booking page lighthouse scores]() |
|:--:|
| <b>Brewtour booking page lighthouse scores - All fine  - Best pratices low due to front-end JavaScript libraries with known security vulnerabilities. this is from the Jquery need by libary from bootsrap</b>|

# 3. Testing User Stories <a id="stories"></a>

## viewing and navigition <a id="nav"></a>

1. As a first time vistor, I want to be able easily recongise the navigation bar of the website. So that i can easily navigate through the pages 
 * When entering the site users can clearly see the navigation bar and the purpose of the site is very clear.

 ![home page screenshot]() |
|:--:|
| <b>Outline of the home page and a clear navigation bar at the top of the page</b>|


2. As a shopper. I want to easily view a list of products.
 * all products can been seen on the products page. The product page is in the navbar at the top of the screen. Shoppers can also type into the search bar to just view products relevent to their searches.  

 ![Beer page screenshot]() |
|:--:|
| <b>search bar at top of screen and link in navbar</b>|

3. As a shopper. I want to easily view a individual product details. So that i can view the product name, price, description and style.  
 * all products hav a products detail page with more info on each product. 

 ![Product details page screenshot]() |
|:--:|
| <b>all information on each product can be found here</b>|

## Searching and sorting <a id="search"></a>

4. As a shopper. I want to Sort through products. So that i can easily sort through products for the product im looking for.  
 * In the navbar there is a drop down menu so shoppers can select the styles the like. Shoppers can also type into the search bar to just view products relevent to their searches.    

 ![nav bar drop down menu and search bar]() |
|:--:|
| <b>nav bar drop down menu and search bar can be used to sort through products</b>|

5. As a shopper. I want to Sort through products Sort through products by style. So that i can easily sort through products in the style i like .  
 * In the navbar there is a drop down menu so shoppers can select the styles the like.   

 ![drop down menu with the styles highlighted]() |
|:--:|
| <b>When a style is selected the user will only see beers of that style</b>|

6. As a shopper. I want to search for products by name or description. So that i can find a specific product .  
 * Users can search in the search bar this will query the name field and description and only return matches.  
   
 ![search bar and result]() |
|:--:|
| <b>product search using search bar </b>|

## Registration and User Account <a id="account"></a>
7. As a site user. I want to Sign up for an account easily. Create a personal profile.  
 * Users can register for an account by clicking the resgister account button in the navbar and filling out the form.  

 ![regisiter acount link]() |
|:--:|
| <b>Register account link in the navbar</b>|

 ![regisiter form]() |
|:--:|
| <b>Register form user must filling</b>|

8. As a site user. I want to easily login. So that access my personal account.  
 * Users can fimd the login link in the nav bar and fill in the form.  
   
 ![Login link]() |
|:--:|
| <b>Login link in the navbar</b>|

 ![Login form]() |
|:--:|
| <b>Login form user must filling</b>|

9. As a registered user. I want Easily recover my account if i forget my password.  
 * Users can press the Easily recover my password link on the login page and recover there password using there email address.  

  ![recover password form]() |
|:--:|
| <b>recover password form</b>|

10. As a registered user, i want to easily logout my account.
 * A logged in user will see the log out option in the nav bar. 

  ![Logout option in navbar]() |
|:--:|
| <b>log out option in navbar</b>|

11. As a site user, i want recieve an confirmation ater sign up, So that i can Verify my email address.
 * Users will recieve a confirmation email once they register for an acoount. 

![Confirmation email sent ]() |
|:--:|
| <b>confirmation email sent</b>|

## Purchasing and check out <a id="order"></a>

12. As a shopper. I want to easily select and purchase products . So that i Add products to my cart.  
 * Users can add items to their shopping cart on the products details page. This can then be viewed in there shopping cart.  
   
 ![Adding product to he shoppong cart]() |
|:--:|
| <b>adding product to the basket</b>|

 ![products now in the shoppong cart]() |
|:--:|
| <b>added product to he shoppong cart</b>|

13. As a shopper. Easily view the total of my purchases  . So that i dont over spend.  
 * The total of the shopping cart is always displayed in the corner of the screen so users can always keep track of what they are spending.  

  ![Total of shopping cart in the navbar]() |
|:--:|
| <b>Total of shopping cart in the navbar</b>|

14. As a shopper, I want to be able to easily remove items from my shopping cart.
 * Shoppers can remove items from the basket by clicking the remove item link inside the basket 

 ![Remove item link ]()
 |:--:|
 | <br>Remove item link</br>

 15. As a returning user, I want to beable to view my previous purchases.
 * Users can see their order history on their profile page 

![User Profile page]() |
|:--:|
| <b>User Profile page</b>|

## Contacts and booking <a id="booking"></a>

16. As a site user, I want to easily make booking at the brewery. So that i can book a table or a brewery tour. 
* Users can make booking for the taproom and brewery tour by filling out the book now forms. Links to both forms are clearly seen throught the site and in the footer. 

![Brewery tour booking form]() |
|:--:|
| <b>Brewery tour booking form</b>|

![Taproom booking form]() |
|:--:|
| <b>Taproom booking form</b>|

17. As a site user, I want to easily Find social media links. So can follow and interact with thier content
* Social media links in both the navbar and the footer. Also in the contact page 

![Navbar with social media links ]() |
|:--:|
| <b>Navbar with social media links</b>|

![Footer with social media links ]() |
|:--:|
| <b>Footer with social media links</b>|

18. As a site user, I want to easily find contact details. Get in touch if i need too and find opening hour.
*  The contact us page is clearly linked in the navigation bar. On this page it has an enquiry form and all other contact information. The opening times are listed here too.

![Contact Form ]() |
|:--:|
| <b>Contact Form </b>|

### Adding content <a id="content"></a>

19. As a site Site Owner, i want to admin pages that allow me to add content. So i can add products/events to the website 
 * Admin users can add products and Events to the website by going to the management pages and filling out the form.

![Add Product Form ]() |
|:--:|
| <b>Add Product Form</b>|

![Event Product Form ]() |
|:--:|
| <b>Add Product Form</b>|

20. As a site Site Owner, i want to admin pages that allow me to edit content. So i can edit products/events to the website 
 * Admin users can edit products and Events by clicking the edit links under each product/event and filling out the form.

![Edit Product Form ]() |
|:--:|
| <b>Add Product Form</b>|

![Edit Product links ]() |
|:--:|
| <b>Add Product Form</b>|

21. As a site Site Owner, i want to admin pages that allow me to delet content. So i can delete products/events to the website 
 * Admin users can delete products and Events by clicking the delete links under each product/event 

![delete Product links ]() |
|:--:|
| <b>Add Product Form</b>|

![delete Product links ]() |
|:--:|
| <b>delete Product Form</b>|

# 4. Manual Texting <a id="testing"></a>

## Navigation links (logged out)

| Test number | Page |Test Description|Expected Outcome|ScreenShot| Pass/Fail| Comment |
|:-----------:|:----:|:--------------:|:--------------:|:--------:|:--------:|:-------:|
|1|Navigation links|Home button clicked|Opens home page|![home page]()|Pass|Works as expected|
|2|Navigation links|Beer button clicked|Opens beer page|![beer page]()|Pass|Works as expected|
|3|Navigation links|Taproom button clicked|Opens Taproom page|![taproom page]()|Pass|Works as expected|
|4|Navigation links|Our story button clicked|Opens Our Story page|![Our Story page]()|Pass|Works as expected|
|5|Navigation links|Our Contact button clicked|Opens Contact page|![Contact page]()|Pass|Works as expected|
|7|Navigation links|Login button clicked|Opens login page|![Login page]()|Pass|Works as expected|
|8|Navigation links|Sign up button clicked|Opens login page|![Sign up]()|Pass|Works as expected|
|9|Navigation links|Shopping cart buttonclicked|Opens shopping cart page|![Opens shopping cart page]()|Pass|Works as expected|
|10|Navigation links|facebook link clicked|Opens Facebook in new tab![Opens Facebook page]()|Pass|Works as expected|
|11|Navigation links|twitter link clicked|Opens Twitter in new tab|![Opens Twitter]()|Pass|Works as expected|
|12|Navigation links|youtube link clicked|Opens Youtube in new tab|![Opens Youtube]()|Pass|Works as expected|
|13|Navigation links|phone number link clicked|Opens Call pop up|![Opens Call pop up]()|Pass|Works as expected|
|13|Navigation links|Logo clicked|Opens Homepage| ![Home Page]()|Pass|Works as expected|


## Navigation links (logged in)

| Test number | Page |Test Description|Expected Outcome|ScreenShot| Pass/Fail| Comment |
|:-----------:|:----:|:--------------:|:--------------:|:--------:|:--------:|:-------:|
|14|Navigation links|Profile link clicked|Opens Profile page|![Pofile page]()|Pass|Works as expected|

## Navigation links (Admin Logged in)

| Test number | Page |Test Description|Expected Outcome|ScreenShot| Pass/Fail| Comment |
|:-----------:|:----:|:--------------:|:--------------:|:--------:|:--------:|:-------:|
|15|Navigation links|Product Management link clicked|Opens Product management page|![Product management page|]()|Pass|Works as expected|
|16|Navigation links|Create Newsletter  link clicked|Opens Create Newsletter page|![Create Newsletter page|]()|Pass|Works as expected|
|17|Navigation links|Create Newsletter sign up link clicked|Opens Newsletter sign page|![Newsletter sign up page|]()|Pass|Works as expected|
|18|Navigation links|Product Management link clicked|Opens Events management page|![Events management page|]()|Pass|Works as expected|
|19|Navigation links|Product Management link clicked|Opens Bookings page|![Bookings page|]()|Pass|Works as expected|
|20|Navigation links|Contact Management link clicked|Opens Contact management page|![Manage messages|]()|Pass|Works as expected|

## Footer links 

| Test number | Page |Test Description|Expected Outcome|ScreenShot| Pass/Fail| Comment |
|:-----------:|:----:|:--------------:|:--------------:|:--------:|:--------:|:-------:|
|21|Footer links|logo link clicked|Opens Home page|![Home page|]()|Pass|Works as expected|
|22|Footer links|Terms and conditions link clicked|Opens Terms and conditions |![HTerms and conditions]()|Pass|Works as expected|
|23|Footer links|Privacylink clicked|Opens Terms and conditions |![privacy |]()|Pass|Works as expected|
|24|Footer links|Contact clicked|Opens contact page |![contact page |]()|Pass|Works as expected|
|25|Footer links|Book taproomclicked|Opens book taproom page |![taproom booking page |]()|Pass|Works as expected|
|26|Footer links|Book brewery tour clicked|Opens book brewery tour page |![conatct page |]()|Pass|Works as expected|
|27|Footer links|facebook link clicked|Opens Facebook in new tab![Opens Facebook page]()|Pass|Works as expected|
|28|Footer links|twitter link clicked|Opens Twitter in new tab|![Opens Twitter]()|Pass|Works as expected|
|29|Footer links|youtube link clicked|Opens Youtube in new tab|![Opens Youtube]()|Pass|Works as expected|
|30|Footer links|phone number link clicked|Opens Call pop up|![Opens Call pop up]()|Pass|Works as expected|

## Home Page Button 

| Test number | Page |Test Description|Expected Outcome|ScreenShot| Pass/Fail| Comment |
|:-----------:|:----:|:--------------:|:--------------:|:--------:|:--------:|:-------:|
|31|Home page |Shop now button clicked|Opens products page|![Beer page|]()|Pass|Works as expected|
|32|Home page |Book now button clicked|Opens taproom booking page|![Taproom button page|]()|Pass|Works as expected|
|33|Home page |Events button clicked|Opens Events page|![Events button page|]()|Pass|Works as expected|

### Products Page Buttons and links

| Test number | Page |Test Description|Expected Outcome|ScreenShot| Pass/Fail| Comment |
|:-----------:|:----:|:--------------:|:--------------:|:--------:|:--------:|:-------:|
|34|Product page |Buy now button clicked|Opens products details page|![product Details page|]()|Pass|Works as expected|
|35|Product page |Image clicked|Opens taproom booking details page|![Product Details page|]()|Pass|Works as expected|
|36|Product page |Book now button clicked|Opens taproom booking page|![Taproom button page|]()|Pass|Works as expected|

### Taproom page Buttons and links

| Test number | Page |Test Description|Expected Outcome|ScreenShot| Pass/Fail| Comment |
|:-----------:|:----:|:--------------:|:--------------:|:--------:|:--------:|:-------:|
|37|Taproom page |Book now button clicked|Opens Taproom booking page|![Taproom booking page|]()|Pass|Works as expected|
|38|Taproom page |Shop now clicked|Opens Product page|![Product page|]()|Pass|Works as expected|

### Our Story Buttons

| Test number | Page |Test Description|Expected Outcome|ScreenShot| Pass/Fail| Comment |
|:-----------:|:----:|:--------------:|:--------------:|:--------:|:--------:|:-------:|
|37|Our Storypage |Book now button clicked|Opens Taproom booking page|![Brewery tour booking page|]()|Pass|Works as expected|

### Events Links
|37|Events |Ticket link clicked|Opens ticket link page in new tape|![Eventbrite|]()|Pass|Works as expected|

### Contact Links
|38|Contact links|facebook link clicked|Opens Facebook in new tab![Opens Facebook page]()|Pass|Works as expected|
|39|Contact links|twitter link clicked|Opens Twitter in new tab|![Opens Twitter]()|Pass|Works as expected|
|40|Contact links|youtube link clicked|Opens Youtube in new tab|![Opens Youtube]()|Pass|Works as expected|
|41|Contact links|phone number link clicked|Opens Call pop up|![Opens Call pop up]()|Pass|Works as expected|
|42|Contact links|email link clicked|Opens Email pop up|![Opens email pop up]()|Pass|Works as expected|



# 5. Bugs 


# Known bugs 

- Subscription email form not validating.
- Newsletter send email error.
- product page spills over the container on small screens
- contact submit does not clear on submit
- matching icons 
- toasts now showing up