https://user-images.githubusercontent.com/89501363/144725439-5d9191f8-df13-4814-aa15-99cd752ab0cc.mp4

[![GitHub license](https://img.shields.io/github/license/Cynamide/application-tracking-system)](https://github.com/chaithanyaMarripati/application-tracking-system/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10211922.svg)](https://doi.org/10.5281/zenodo.10211922)
[![codecov](https://codecov.io/gh/chaithanyaMarripati/application-tracking-system/branch/main/graph/badge.svg)](https://codecov.io/gh/Cynamide/application-tracking-system)
![GitHub issues](https://img.shields.io/github/issues/chaithanyaMarripati/application-tracking-system)
![GitHub closed issues](https://img.shields.io/github/issues-closed/chaithanyaMarripati/application-tracking-system)
![GitHub top language](https://img.shields.io/github/languages/top/Cynamide/application-tracking-system)
[![Super Linter](https://github.com/chaithanyaMarripati/application-tracking-system/actions/workflows/super-linter.yml/badge.svg)](https://github.com/Cynamide/application-tracking-system/actions/workflows/super-linter.yml)

# J-Tracker - Your Job Tracking Assistant

https://user-images.githubusercontent.com/43064854/135554150-c06afd4e-d223-47e3-b123-b45f9cd1b87a.mp4

The process of applying for jobs and internships is not a cakewalk. Managing job applications is a time-consuming process. Due to the referrals and deadlines, the entire procedure can be stressful. Our application allows you to track and manage your job application process, as well as regulate it, without the use of cumbersome Excel spreadsheets.

Our application keeps track of the jobs you've added to your wish list. It also keeps track of the companies you've already applied to and keeps a list of any rejections. Rather than having the user browse each company's site for potential prospects, our application allows the applicant to search for them directly using basic keywords. Any prospective work offers can then be added to the applicant's wishlist.

## Table of contents

- [J-Tracker - Your Job Tracking Assistant](#j-tracker---your-job-tracking-assistant)
  - [Table of contents](#table-of-contents)
  - [Basic Design:](#basic-design)
  - [Samples:](#samples)
    - [Login Page / Signup Page](#login-page--signup-page)
    - [HomeScreen](#homescreen)
    - [SearchPage](#searchpage)
    - [SearchPage with Salary filter](#searchpage-with-salary-filter)
    - [ResumePage](#resumepage)
    - [Recommendations Page](#recommendations-page)
    - [Whats New](#whats-new)
      - [Version 1.1](#version-11)
      - [Version 1.0.3](#version-103)
      - [Version 1.1.1](#version-111)
  - [Roadmap:](#roadmap)
  - [Future Scope:](#future-scope)
  - [Explanation:](#explanation)
  - [Technologies Used:](#technologies-used)
  - [Installation:](#installation)
    - [Requirements:](#requirements)
    - [Strongly Recommended:](#strongly-recommended)
  - [Getting Started:](#getting-started)
    - [Boot:](#boot)
    - [Shutdown:](#shutdown)
  - [Hosting the Database:](#hosting-the-database)
    - [Local MongoDB:](#local-mongodb)
    - [Hosted database with MongoDB Atlas:](#hosted-database-with-mongodb-atlas)
  - [License](#license)
  - [How to Contribute?](#how-to-contribute)
  - [Team Members (Group 16)](#team-members-group-16)

## Basic Design:

![Basic Design](https://github.com/prithvish-doshi-17/application-tracking-system/blob/main/resources/Overall%20Design.PNG)

## Samples:

### Login Page / Signup Page

The introductory visual interface displayed from which a user is able to register and log into the application.

<p align="center"><img width="700" src="./resources/login.png"></p>

### HomeScreen

The introductory visual interface displayed from which a user is able to access different cards - Waitlisted applications, Waiting for Refereals, Applied Jobs, Application Status.The user can also add cards through this screen.

<p align="center"><img width="700" src="./resources/home_screen.png"></p>

### SearchPage

The interface through which a user is able to search for specific jobs and add them to Waitlisted Applications.

1. Navigate to Job search page, search for particular Job.
2. Click on Add button. Fill in the Details.
3. Click on Create buttop.
4. The application will then be saved as per the selected category.

<p align="center"><img width="700" src="./resources/search.png"></p>
<p align="center"><img width="700" src="./resources/newjobdetails1.PNG"></p>

### Share with friends 

Share the applications status with friends via email 

1. click on share with friends button
2. select the column you want to share with friends
3. enter the email address
4. click on send button to be able to share the details

<p align="center"><img width="700" src="./resources/share.png"></p>


### SearchPage with Salary filter

The interface through which a user is able to search for specific jobs based on the salary range selected.

1. Navigate to Job search page, search for particular Job and select the salary range from the dropdown.
2. Click on Search button.

<p align="center"><img width="700" src="./resources/salaryfilter1.png"></p>

### ResumePage

1. Navigate to resume Section
2. Upload any resume file with .PDF extension by selecting the file from local storage. Click Upload.
3. Click on download button to Download the uploaded file.

<p align="center"><img width="700" src="./resources/resume.png"></p>

### Recommendations Page

1. Assuming that you have uploaded your resume on the resume page
2. Click on the get recommendations button
3. View the recommended companies returned by ChatGPT API

<p align="center"><img width="700" src="./resources/recommendations.png"></p>

### Whats New

#### Version 1.1

- Add headless feature for selenium
- Fix shutdown.sh
- Login frontend
- Add resume storage for users
- Updated reloading issues
- Fix linting issues

#### Version 1.0.3

- Updated badges for repository
- Users database implementation
- Add logout endpoint and update middleware
- Implementing search based on salary functionality
- Login frontend for login and signup functionality
- Search custom date

#### Version 1.1.1

- Added intelligent job recommendations based on OpenAI ChatGPT's API response
- Used the OpenAI API to analyze resume uploaded by user and intelligently recommend companies to apply to
- Updated badges for repository
- Updated GitHub workflows files

#### Version 1.2.0
- Added deadline reminder using google calendar
- Deadline notifications on the main dashboard
- Fuzzy search implemented on the main page, search for jobTitle, companyName, date and jobLink
- share with friends, to be able to share the applications status with friends via email

**Job Recommendations Video (Added in Version 1.1.1)**
Watch: https://github.com/Cynamide/application-tracking-system/blob/ff0691c919330a2c8cf80854fe969e31214671b4/resources/JobRecommendationsDemo.mp4

## Roadmap:

![Roadmap](https://github.com/prithvish-doshi-17/application-tracking-system/blob/main/resources/Roadmap%20-%202.PNG)

## Future Scope:

- Include deadline reminders for the application and interview.
- Include a direct link to the company's application site when the wishlist item is clicked.
- Include a link to the university’s career fair page.
- Direct connection to LinkedIn, allowing for the addition of job opportunities to the wishlist.
- Improve keyword search to improve specifications such as pay range, employment location, and so on.
- An option to maintain separate profiles for job tracking.

## Explanation:

Currently, we have four fundamental steps in our project:

1. The position for which you have applied
2. The job you want to apply for, without a referral
3. The job at which you have faced rejection, and
4. The job you're waiting for a referral.

Any details in any table can be modified at any time during the process.

## Technologies Used:

- Python
- Node.js
- Flask
- MongoDB

## Installation:

### Requirements:

- [Python](https://www.python.org/downloads/) (recommended >= 3.8)
- [pip](https://pip.pypa.io/en/stable/installation/) (Latest version 21.3 used as of 11/3)
- [npm](https://nodejs.org/en/) (Latest version 6.14.4 used as of 11/3)

## Getting Started:

docker and docker compose are used to start and run the application 
make sure you download the latest version of docker desktop from [Link](https://www.docker.com/products/docker-desktop/)

Run the following command in your terminal

```
docker compose up
```

## Hosting the Database:

### Local MongoDB:

1. Download [MongoDB Community Server](https://docs.mongodb.com/manual/administration/install-community/)
2. Follow the [Installion Guide](https://docs.mongodb.com/guides/server/install/)
3. In `app.py` set `'host'` string to `'localhost'`
4. Run the local database:

```
mongod
```

- Recommended: Use a GUI such as [Studio 3T](https://studio3t.com/download/) to more easily interact with the database

### Hosted database with MongoDB Atlas:

1. [Create account](https://account.mongodb.com/account/register) for MongoDB

\*\* **_If current MongoDB Atlas owner adds your username/password to the cluster, skip to step 4_** \*\*

2. Follow MongoDB Atlas [Setup Guide](https://docs.atlas.mongodb.com/getting-started/) to create a database collection for hosting applications
3. In `app.py` set `'host'` string to your MongoDB Atlas connection string
4. Create an `application.yml` file in the /backend directory with the specifications:

```
username: <MongoDB Atlas cluster username>
password: <MongoDB Atlas cluster password>
```

5. For testing through CI to function as expected, repository secrets will need to be added through the settings. Create individual secrets with the following keys/values:

```
MONGO_USER: <MongoDB Atlas cluster username>
MONGO_PASS: <MongoDB Atlas cluster password>
```

## License

The project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.

## How to Contribute?

Please see our CONTRIBUTING.md for instructions on how to contribute to the repository and assist us in improving the project.

## Team Members (Group 18)

- [Krishna Chaitanya Marripati](https://github.com/chaithanyaMarripati)
- [Sai Vikas Reddy Yeddulamala](https://github.com/saivikasreddy717)
- [Sai Subhang Boorlagadda](https://github.com/subhang51011)
- [Basaveswara Mukesh Suryadevara](https://github.com/S-B-Mukesh)
