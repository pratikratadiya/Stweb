************Documentation for Payment Statistics Module****************

# Table of Contents

1. Installation
2. Using the software
3. Features
4. Tables structure 
5. Scope for improvement 

***************************************************************

// 1. INSTALLATION AND REQUIREMENTS //

-> Requirements:
	1. Python 3.0+
    2. Linux OS(not compulsory)* (*-refer end of file)

-> Installation procedure:

1. Go to the directory where you have cloned the repo and activate virtual environment 
    `source myvenv/bin/activate`

2. Upgrade pip and install Django version 2.0
    `pip install --upgrade pip`
    `pip install django~=2.0`

3. Install mysql client using the following commands:
    `sudo apt-get install python3-dev`
    `sudo apt-get install python3-dev libmysqlclient-dev`

    and then
       `pip install mysqlclient`
       
4. Install mysql server in your PC using the command 
    `sudo apt-get install mysql-server`
        You will be prompted to enter a password, enter a password 
    MySQL is now installed which you can check by running the command `systemctl status mysql.service` which will show active status.
    
5. Login into mysql server using `mysql -u root -p` and enter password. A mysql shell will be started. Create database for our project using 
    `CREATE DATABASE project_data;`
    
6. Update the database settings in the settings.py file located at `st_app/settings.py` and set the values of NAME, USER, PASSWORD  to the database name, user name and password respectively.
    Restart the server to update the database schema:
        `systemctl daemon-reload`
        `systemctl restart mysql`

7. Perform migrations into the database using the following commands             
    `python manage.py makemigrations`
    `python manage.py sqlmigrate st_web 0001_initial`
    `python manage.py migrate`

This completes the installation process and you are ready to use the product!

***************************************************************

// 2. USING THE SOFTWARE // 

- Go into the directory where you have cloned the repository: `cd directory`
- Activate virtual environment: `source myvenv/bin/activate`
- Go into st_app directory and type the command `python manage.py runserver`
	
	Server will be initialised at `http://127.0.0.1:8000`. Access this URL through your browser and get the app running!
	
 Note: To access the admin panel, enter the URL `http://127.0.0.1:8000/admin` You will be asked to enter credentials doing which you will get access to the admin panel
 
****************************************************************

// 3. FEATURES //

- Login and signup facility for existing and new contributors 
- Admin login facility on the front end side 
- Facility for admin to assign tutorial as well as foss(for new contributor) on the front end
- Facility for contributor to upload the tutorial assigned to them 
- List displaying tutorials contributed with expected and actual date 
- List displaying contributions done by a user
- List displaying total amount payable per contributor 
- SPAM filtering to allow only valid media extension files to be accepted as a tutorial file.

****************************************************************

// 4. TABLES STRUCTURE //

- There are four tables used - User, Foss, Tutorial_detail, Payment 
- User table is extended from the django user model as abstract user with extra fields `name` and `contributions` which store total contributions of a user 
- Foss table has two fields- contributor which is has One-to-One relationship with User, and foss_name which stores the name of the FOSS
- Tutorial_detail table has following fields: parent_foss which is a foreign key from the foss table; tutorial_name which has the name of the tutorial; tutorial which stores the file of the assigned tutorial; expected_date and actual_date which store the expected dates and actual date of submission for the tutorial object 
- Payment table has two fields- user, which is a foreign key from the user table and amount which stores the amount payable for the respective user

****************************************************************

// 5. SCOPE FOR IMPROVEMENT //

- Giving user the liberty to chose the month for which they wish to see the concerned lists
- Improving front end styling of forms and profile pages
- Payment gateway for admin to pay pending amounts to contributors and subsequent changes in the amount payable 

****************************************************************

* REMARKS

If you face problems while installation on system other than Linux(Ubuntu,Fedora etc.) like Windows, MacOS
feel free to refer the following link:
	https://tutorial.djangogirls.org/en/django_installation/
	
Documentation By: Pratik Rajendra Ratadiya
Contact me at: prratadiya@gmail.com
Github profile link: https://www.github.com/prratadiya
