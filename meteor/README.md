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
