# appChat 

So this is the simple application I am going to be building . Now all these data you're seeing here with the date and time with the message and the name are going to be saved in our database .You will see getting back all these messagesin real time. 


# Features



## Database Model
![appModel4](https://github.com/julielk/appChat/assets/118198069/e079aab9-f00a-49ae-a8a4-52eca4441806)


I am  going to set up two models, using the ERD desing above first one is called room,
and the second called  the messages. In side the room model a model called name with a character field  
Inside the messages models a  value with characterfield for example  if the user wants to send  a message, 
let's give it a date.date time field. So the next thing we want to have is the user, charater field in this project.
And then the last term I want to add is the room. So we want to know which room is this projects been in this message


# App Chat

![frorm](static/images/form.png)




The front-end of the app before enterning room or sending a message

![form](static/images/form2.png)
Now. Let's enter room name as *Backend Developer*.  Now you see that it loads all the *messages* of this
room. Now, let me say *chat app with backend development* automatically, you see, it shows you and 
it shows in my own side also. So it's *real time*. So if someone is in another part of the 
world,it's gonna work. in different places, once a user sends a message here is going to show
right here in my own platform a real time  feature,



# Database

![databse](static/images/database.png)
In te django adminstration database the messaage sent  at the front-end  is stored at the backend.
if we click on messages the message object. Shows the value *chat app with backend development*,
date  2020.03.21,  time 15.16, user *joe blogs* room *8*



# Validator Testing
## HTML
No errors were returned when passing through the official W3C validator
## CSS
No errors were found when passing through the official (Jigsaw) validator
## Javascript
No errors were returned JavaScript code passed through a linter (e.g. jslint.com) with no major issues
## pthon 
Python code  conforms to the PEP8 style guide (style guide, such as Google's)
Unfixed Bugs


## Testing App Chat form

So let's make sure we got no errors. And in this -test . So let's just
go to the home page. An So now let me create a new room. So let me
say, let me just say, *development*, let me just name it *developmenr*. And now let
 you can see now that there are no messages,  I can put something like, if there are 
 no messages, I should say, no messages in the room. We don't need that for now. 
 So *deelopmenr*.And then let's enter another another name, *Joe*, we need to enter.
 So now we have these two blank rooms, who's online, it's automatically shows here 
 without any delay. 





# Github Repository

  https://github.com/julielk/appChat

# Credits
**Snippet Tool**  used for the screenshot of images in project
**Luncid Chart**  used for designing database  models.
**Django Framework**  design for chat App



# Content

Instructions on how to implement form validation taken from code
Insitute Tutorial The images us were taken from the unsplash websitee site
