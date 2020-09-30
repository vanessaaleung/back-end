# Meteor

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
