## **In Home**

[View the deployed project here](https://in-home-9aea5ddaebd0.herokuapp.com/)

![Application shown on multiple devices]()

## **Site Overview**

In Home is an online e-commerce store selling all different types of homeware. Users are able to browse and purchase homeware directly through the website, make an account to keep track of their order history, leave reviews for products they have purchased and contact the company via a contact form.

## **Table of contents**

- [**In Home**](#in-home)
- [**Site Overview**](#site-overview)
- [**Table of contents**](#table-of-contents)
- [**Planning stage**](#planning-stage)
  - [**Target Audiences**](#target-audiences)
  - [**User Stories**](#user-stories)
  - [**Site Aims**](#site-aims)
  - [**Database Schema**](#database-schema)
  - [**Wireframes**](#wireframes)
  - [**Color Scheme**](#color-scheme)
- [**Typography**](#typography)
- [**Features**](#features)
- [**Future Enhancements**](#future-enhancements)
- [**Testing Phase**](#testing-phase)
  - [**Responsiveness**](#responsiveness)
  - [**Functionality**](#functionality)
  - [**Validators**](#validators)
  - [**Lighthouse**](#lighthouse)
  - [**Testing user stories**](#testing-user-stories)
- [**Bugs**](#bugs)
- [**Deployment**](#deployment)
- [**Tech**](#tech)
- [**Credits**](#credits)
  - [**Honourable mentions**](#honourable-mentions)
  - [**Content**](#content)
  - [**Media**](#media)

## **Planning stage**

### **Target Audiences**

- Users in need of homeware for their new home
- Users in need of homeware to refurbish their home
- Users in need of homeware as a gift for a friend or relative
- Users in need of homeware for an office or workplace (kitchen appliances etc)

### **User Stories**

As a new user, I want to:

- Immediately understand the site's purpose
- Easily navigate the website
- Browse all available products
- Filter products to quickly find what I need
- Search for products
- Contact the company for help or advice
- Purchase products without registering for an account
- Browse reviews left by other users
- Stay informed on actions I take throughout the website
- Receive confirmation of my order
- Access the site on any device
- Create and log into an account

As a registered user, I want to:

- View my profile page
- View my previous order history
- View and update my personal information
- Create reviews for products I've purchased
- View reviews for products I've purchased
- Update reviews for products I've purchased
- Delete reviews for products I've purchased
- Change my password
- Make purchases without filling in my personal information each time
- Logout of my account

As an admin, I want to:

- Add new products to the store
- Update existing products
- Delete existing products
- Delete existing reviews
- Easily access admin controls

### **Site Aims**

- Offer a simple and responsive e-commerce store where users can purchase homeware items quickly and easily.
- Offer the ability to register an account, allowing the user to see their previous order history, manage personal information and leave reviews for products they have purchased.
- To keep the user informed as they nagivate the store, providing confirmation of successful actions taking and warning them when something hasn't worked the way they would expect.
- To allow the user the ability to message the store via a contact form if they need help or advice.

### **Database Schema**

-

### **Wireframes**

The original wireframes for the main pages of the store can be found below. During development, a few decisions were made to change the original structure.

- Home Page: The welcome heading and text was moved into the main image underneath the navigation to give this area more substance and make it one of the first things the user can see upon entering the store.
- Product Detail Page: Instead of using Bootstrap cards to display existing review, I opted to use the Bootstrap accordion instead as the cards would be quite big, and also I could incorporate the stores color theme into the accordion in a more aesthetic way than a card. I felt the overall flow of the page was better as a result.
- Contact Page: A few minor label changes for the input fields, plus the addition of the company contact details should the user wish to contact them by phone, email or visit directly. These details are already in the footer, however as one of the essential pieces of information if a user needs help or advice, I felt it was a good idea to include it on the contact page as well.

<br>

<details>
<summary>Home Page</summary>
<br>
<img alt="Home Page Wireframe" src="docs/wireframes/home-wf.png">
</details>
<br>

<details>
<summary>Profile Page</summary>
<br>
<img alt="Profile Page Wireframe" src="docs/wireframes/user-profile-wf.png">
</details>
<br>

<details>
<summary>Contact Page</summary>
<br>
<img alt="Contact Page Wireframe" src="docs/wireframes/contact-us-wf.png">
</details>
<br>

<details>
<summary>Products Page</summary>
<br>
<img alt="Products Page Wireframe" src="docs/wireframes/products-wf.png">
</details>
<br>

<details>
<summary>Product Detail Page</summary>
<br>
<img alt="Product Detail Page Wireframe" src="docs/wireframes/product-details-wf.png">
</details>
<br>

<details>
<summary>Shopping Bag</summary>
<br>
<img alt="Shopping Bag Wireframe" src="docs/wireframes/shopping-cart-wf.png">
</details>
<br>

<details>
<summary>Checkout Page</summary>
<br>
<img alt="Checkout Page Wireframe" src="docs/wireframes/checkout-wf.png">
</details>
<br>

<details>
<summary>Order Confirmation Page</summary>
<br>
<img alt="Order Confirmation Page Wireframe" src="docs/wireframes/order-conf-wf.png">
</details>

### **Color Scheme**

Navy: #0D1B2A
Blue: #415A77

The [WCAG Color Contrast Checker](https://accessibleweb.com/color-contrast-checker/) was used to ensure ..., all results passed except the small text in the AAA test, however after a discussion with my mentor we agreed this was OK as the criteria for the AAA testing is incredibly high and almost never passes.

![Color contrast]()

## **Typography**



## **Features**

**Features common to all pages**




## **Future Enhancements**



## **Testing Phase**

### **Responsiveness**

Responsiveness was checked and worked as intended with the following browsers and screen sizes:

- Extra Large (27" Mac Desktop):

  - Chrome (Version 123.0.6312.106 Official Build x86_64)
  - Safari (Version 17.4.1 19618.1.15.11.14)
  - Firefox (Version 123.0 64-bit)

- Large (15" MacBook Pro Laptop):

  - Chrome (Version 123.0.6312.107 Official Build x86_64)
  - Firefox (Version 124.0.1 64-bit)
  - Safari (Version 17.4.1 17618.1.15.111.8, 17618)

- Medium (10.9" iPad):

  - Chrome
  - Safari
  - Firefox

- Small (6" iPhone 13):

  - Chrome (Version 123.0.6312.52)
  - Safari
  - Firefox (Version 124.3 40336)

DevTools was also used to check the responsiveness at various screen sizes and devices from the list of devices available. All were fully responsive and caused no issues. 

### **Functionality**

Manual testing as a logged **OUT** user

Feature/Test                                                                       | Expected Outcome.                                                                                                                                                  | Result |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
|                                                                     |                                                                                                                |   |


Manual testing as a logged **IN** user

Feature/Test                                                                       | Expected Outcome.                                                                                                               | Result |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------ |
|                                            |                                                                       |   |


### **Validators**

**HTML Validators**

<details>
<summary>Home Page</summary>
<br>
<img alt="Home page HTML validator" src="documentation/html-validators/homepagehtmlvalidator.png">
</details>
<br>

**CSS Validator**

style.css result

![style.css validator result](documentation/css-validator/cssvalidator.png)

**JS Hint**

script.js result

![script.js validator result](documentation/js-validator/jsvalidator.png)

**CI Python Linter**

app.py result

![app.py linter result](documentation/python-validator/pythonlinter.png)

### **Lighthouse**

<details>
<summary>Home Page Desktop</summary>
<br>
<img alt="Home page desktop lighthouse results" src="documentation/lighthouse/homedesktoplighthouse.png">
</details>
<br>

### **Testing user stories**

**User story 1**: As a user, I want the site to be easy to use.

**Achieved?**: Yes. The application includes features and instructions which are clear to the user as they progress through the website.

## **Bugs**

I found the following bugs during the development process:

- Subject
  - Problem: 
  - Cause: 
  - Solution: 

filtering issue when trying to add icons to specific categories. Was missing the .name from the if statement so the conditions couldn't be met

Toasts bug where the jquery was causing the toast not to load as it didn't recognise the toast() function. Replaced it with vanilla javascript which worked with the bootstrap version I was using.

Emails issue after deploying, when setting up contact form getting SMTP.starttls() error and form not submitting correctly

---

## **Deployment**



## **Tech**

Languages used:

- HTML
- CSS
- JavaScript
- Python

Framework used:

- Django

Tools used:

- Bootstrap
- Fontawesome
- Google Fonts
- Stripe
- Amazon Web Services
- CI Database

Deployment:

- Heroku

Version Control:

- Git & Github

## **Credits**

The following people, websites and learning materials aided me with the creation of this project.

### **Honourable mentions**

Special thanks to my mentor Richard Wells for his excellent advice and support throughout this project.

### **Content**



### **Media**

