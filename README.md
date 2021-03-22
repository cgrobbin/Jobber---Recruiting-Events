# Jobber---Recruiting-Events

Jobber is a site for finding recruitment events available around the country. Users can sign up and login to a personal profile that they can update as needed while viewing others public profiles. While anyone can view the upcoming events on the site, a user must be logged in to register and unregister for an event. This allows users to have access to the event and to view it on their profile.

## Heroku Link

[Jobber]()

## Technologies Used

- Django
- Python
- Materialize
- HTML/CSS
- Imgur
- Excalidraw

## Installation Instructions

- Fork and clone this repo
- Create your virtual environment using `python3 -m venv .env`
- Activate your virtual environment `source .env/bin/activate`
- Install all modules `pip3 install requirements.txt`
- Start your server `python3 manage.py runserver`

## Screenshots

![Home](https://i.imgur.com/7Vag09ul.png) ![About](https://i.imgur.com/LYEE7w7l.png)
![Register](https://i.imgur.com/hsgjeQgl.png) ![Login](https://i.imgur.com/4DvZwFMl.png)
![Profile](https://i.imgur.com/lMu82ZRl.png) ![Search](https://i.imgur.com/SJFtBrCl.png)
![Event](https://i.imgur.com/edht4F3l.png) ![Add Event](https://i.imgur.com/dIM6VZvl.png)

## ERD Model

![ERD Model](https://i.imgur.com/wKtQHYJl.png)

There are 3 main models in this application: `User`, `Profile`, and `Events`. While `User` and `Profile` have a 1:1 relationship, `User` and `Events` share a M:M relationship in which one Event can have many Users registered and one User can register for many Events.

## User Stories

- As a user, I want to sign up and be able to continuously use those login credentials.
- As a user, I want to have a profile associated with my login that I can update easily.
- As a user, I want to be able to register/unregister for any available event and when registered, see it on my profile.
- As a user, I want to view other users public profiles and the events that they are registered for.
- As a user, I want a mobile friendly site that is easily accessible on a smart phone.

## Admin Stories

- As an admin, I want to add, update, and delete events on the front end of the application.
- As an admin, I want to be able to add or remove users registration for any event.
- As an admin, I want to view the total number of users registered on the event details page.

## Major Hurdles

We were rather fortunate to not run into any major hurdles that were unsolvable during this application. A few issues we did run into are as follows:

- Toggling between register and unregister based on whether the user is registered for the event or not. This was solved with a boolean passed to the template after some time interacting with the database.
- Proper messages for sign up validation. We solved this with a lot of work together on error messaging and special tags for pop up errors.