# Quote your thought
People have thoughts. You have it, I have it why not let them through writing and posting. You can write short stories, poems, lyrics of our own, opinion on something or just a thought. 

Website link : http://milestone-project-iii.herokuapp.com/

### UX
For this project I wanted to have minimal things like uses of color and font to be simple.  
This section provide a list of User Stories, with the following below:
* As a user type, when I comes to site, it should make me calm but with a lots of thoughts.
* As a user type, I need good navigation and its simple enough that I can read the site make use of it.
* As a user type, I need right color to know what it does, like buttons.
* As a user type, I need to read posts or thoughts.
* As a user type, I need to write or post a thought.
* As a user type, I need to edit a post or thought.
* As a user type, I need to delete a post or thought.
In wireframes folder, you can find wireframes/mock up images. The original plan to have a lots features  but to make it simple, I decided to have only few of them. 

### Features
The project is to have CRUD functionality which means C for create, R for read, U for update or edit and D for delete. The site is simple to understand where you can see a simple title, navigation bar and posts/thoughts. In home page,  you can see/read post or thoughts. In posts, you can see edit and delete button where you can edit or delete a post. In navigation bar, add a thought brings you to create or write a new post. And about bar is about the site and link to developer social sites. More feature detail below.

#### Existing Features
* Click to title and thoughts brings to home page.
* Click to add a thought brings to create or write a new post. 
* Click to edit button brings to update or edit pervious posts.
* Click to delete button deletes a post.
* All Input fields to need to be filled when posting a thought, it will not allow user to post.

I wanted to have many more features like sharing your thought in different social sites, adding comments, user having own account and manage his/her thoughts/posts, a chat room to discuss about your thoughts.

#### Features Left to Implement
* account page where user manage settings
* chat room to discuss  opinion or thoughts
* sharing thoughts to other site
* user can add or invite friends to chat or discuss  their thoughts

### Technologies Used
* HTML  is use for structure.
* CSS  is use for style / decorate.
* Bootstrap is use for responsive for desktop and mobile view. 
* Python is programming language and use for functionality of website features.
* Flask is library for python and use for to help python implement the features.
* MongoDB is non-relational database and use for to store data and manage data structure.
* Gitpod is online code editor and use for write and store the codes and manage codes.

### Testing
* All the links and buttons works fine like title and thoughts is home page.
* All the links about page leads to respective sites.
* Add a thought link leads to posting page where you can add a post.
* All the input field must be fill before submitting.
* The website is responsive and works fine in desktops and mobiles view.
When I was checking all the links and buttons, I found out there was a problem with add a thought link and it was wrong route. It was suppose to be add_thought route but I put get_thought route which was change into index to be recognize as landing page by hosting platform. 

### Deployment
I used Heroku platform to host the website. Before I used to host in github but I am using python and github do not support python apps. Heroku deployment was little bit confusing because of many programming language apps it supports. This is my process for deployment in heroku:
* create/ setup configs var which is IP and PORT address for your website.
* go to code editor and connect to heroku.
* create requirements.txt which is the requirements file and libraries for the app.
* create Procfile which a file to recognize heroku that app is using certain programming language in which my is python.
* after completion  push it to heroku command git push heroku master

I had problem during my deployment. When I try to push heroku using "git push heroku master", heroku did not recognize for some reason. After some research I found out that I have change master folder to main and then push it. It did worked but I have to merge main to master in github.
I used MongoDB database which store data and you can manage data and data types. I have to make database and its collection and I had to setup IP and PORT address to connect from database to my app. My collection or database structure is like this:

title : "Thoughts"

content : "A new idea is an old idea but with a different perspective"

name : " A-man"

To deploy my app locally you need code editor, heroku hosting platform  and MongoDB.  Make sure you have heroku and MongoDB account and database structure which is above. 

### Acknowledgements
•	I was inspired by twitter - https://en.wikipedia.org/wiki/Twitter

