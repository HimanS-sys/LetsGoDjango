# LetsGoDjango
A demo repository to learn Django Framework.

## UserApp
A basic page that: 
* creates user (type: `GET`, path: `'name/'`, creates user object named profile and redirects)

![Screenshot 2024-02-24 000353](https://github.com/HimanS-sys/LetsGoDjango/assets/68765011/8382f415-224b-4c8c-8770-1100cae85b57)

* displays all users info (type: `POST`, path: `'name/'`, displays all the users information as a rendered template)
  
![Screenshot 2024-02-24 000621](https://github.com/HimanS-sys/LetsGoDjango/assets/68765011/269bf013-176b-441a-96af-d5ffc62c4e33)

* displays single user info (type: `GET`, path: `'profile/{name}/'`, returns a json response)
  
![Screenshot 2024-02-24 001312](https://github.com/HimanS-sys/LetsGoDjango/assets/68765011/261475fe-9388-4ae4-9e29-5124469f4e24)

* updates email (type: `POST`, path: `'profile/{name}/email/'`, returns with message of success/failure)
  
![Screenshot 2024-02-24 103158](https://github.com/HimanS-sys/LetsGoDjango/assets/68765011/92d9da80-8551-4c47-a346-21ceb653b1fe)


