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

- 

### **User Stories**

- 

### **Site Aims**

- 

### **Database Schema**

### **Wireframes**

<details>
<summary>Home Page</summary>
<br>
<img alt="" src="">
</details>
<br>

### **Color Scheme**

Actual HEX values

The [WCAG Color Contrast Checker](https://accessibleweb.com/color-contrast-checker/) was used to ensure ..., all results passed except the small text in the AAA test, however after a discussion with my mentor we agreed this was OK as the criteria for the AAA testing is incredibly high and almost never passes.

![Color contrast]()

## **Typography**



## **Features**

**Features common to all pages**



**Home Page**



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

## **Credits**

The following people, websites and learning materials aided me with the creation of this project.

### **Honourable mentions**

Special thanks to my mentor Richard Wells for his excellent advice and support throughout this project.

### **Content**



### **Media**

