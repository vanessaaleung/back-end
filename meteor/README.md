# Meteor
- [Setup](#setup)
- [Database](#database)
- [Router](#router)
- [Authentication](#authentication)
- [Blog](#blog)
- [Deployment](#deployment)
- [Add Packages](#add-packages)
- [Testing](#testing)

## Setup
### Installation
```shell
curl https://install.meteor.com/ | sh
```

### Create A Project
```shell
meteor create --react simple-todos-react
```
- Run the app
```shell
meteor run
```

## Directory Structure

### imports/api
A place to store API-related code, like publications and methods

## Responsive Design
- Adding these lines to your client/main.html file, inside the head tag, after the title
```html
<meta charset="utf-8"/>
<meta http-equiv="x-ua-compatible" content="ie=edge"/>
<meta
    name="viewport"
    content="width=device-width, height=device-height, viewport-fit=cover, initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no"
/>
<meta name="mobile-web-app-capable" content="yes"/>
<meta name="apple-mobile-web-app-capable" content="yes"/>
```

## Database
### Create a Collection in MongoDB
```jsx
import { Mongo } from 'meteor/mongo';
 
export const TasksCollection = new Mongo.Collection('tasks');
```
### Initialize a Collection
```jsx
import { TasksCollection } from '/imports/api/TasksCollection';

const insertTask = taskText =>
  TasksCollection.insert({ text: taskText });

Meteor.startup(() => {
  // If the Tasks collection is empty, add some data.
  if (TasksCollection.find().count() === 0) {
    [
      'First Task',
      'Second Task'
    ].forEach(insertTask)
  }
});
```
### Render a Collection
```jsx
import { useTracker } from 'meteor/react-meteor-data';
import { TasksCollection } from '/imports/api/TasksCollection';

const tasks = useTracker(() => TasksCollection.find({}).fetch());
```

### Connect to MongoDB
```shell
meteor mongo
```

## Add Packages
```shell
meteor add react-meteor-data
```

## Authentication
- Enable username and password authentication
```shell
meteor add accounts-password

meteor npm install --save bcrypt
```
- Should always use `meteor npm` instead of only `npm`, help avoid problems ude to different versions of npm installing different modules

- Create a default user
```jsx
Meteor.startup(() => {
  // Create a default user 
  if (!Accounts.findUserByUsername(SEED_USERNAME))  {
    Accounts.createUser({
      username: SEED_USERNAME,
      password: SEED_PASSWORD,
    })
  }
```

## Router
_Route between site URLs and HTML content on both the client and the server_
```shell
meteor add iron:router
```
- Create a route
```js
Router.route('/', function () {
  this.render('Home'); // render the template called Home
});
```
- Server side route
```js
Router.route('/item', function () {
  var req = this.request;
  var res = this.response;
  res.end('hello from the server\n');
}, {where: 'server'});   // tells the Router thihs is a server side route
```

- Create a html file as a template

```html
<template name="news">
  ...
</template>
```

- Add the page link in the navbar
```html
<a href="news">News</a>
```

## Blog
```shell
meteor add ryw:blog
````

## Publications
- `Meteor.publish`: allows data to be published from server to client
- `Meteor.subscribe`: allows client code to ask for data to client

## Testing
```shell
meteor add meteortesting:mocha
meteor npm install --save-dev chai
```

```shell
TEST_WATCH=1 meteor test --driver-package meteortesting:mocha
```

<img src="test.png" height="100px">


## Deploy
1. Create account on Galaxy: www.meteor.com/sign-up
2. Set up MongoDB on https://www.mongodb.com/cloud/atlas
3. Create the database and collections and et up network access
4. Copy the MongoDB Atlas URL like this `mongodb+srv://youruser:youserpassword@yourname.sdge2.mongodb.net/yourdb`
5. Create a folder called `private` in root directory and create a file called `settings.json` inside
```json
{
  "galaxy.meteor.com": {
    "env": {
      "MONGO_URL": "Your MongoDB URL"
    }
  }
}
```
6. Run `meteor npm install` to make sure all dependencies are installed
7. Deploy
```shell
meteor deploy YOUR_SUB_DOMAIN.meteorapp.com --settings private/settings.json
```
