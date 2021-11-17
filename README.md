# Liquidity Task

The task is to calculate the liquidity ratio, which allows us to understand much better whether
the ads are popular among seekers.
Based on this, I prepared a complete analysis using the available data.

I have chosen to divide this task into two parts:

<br/>

**Technical part**
1. SQL queries that allow liquidity calculation - I have developed a sql script, which is inserted in a python file, through which it will be possible to access a database created within the scope of this task in postgresql.
The execution steps of this task are defined below

2. Preparation also in Python for calculating liquidity for all users, i.e. I want to get a
list with information about exactly how much liquidity is for each user

**Analytical part**
1. Please prepare a complete analysis of the data that was sent, along with the answers to
the following questions:    

        a. What differences do you see between the segments in terms of the data you have available (including liquidity)?


        b. What I think may affect the higher or lower liquidity level?

Form:
1. Jupyter and Markdown preferred for analysis
2. The scripts can be in separate files or as part of the notebook depending on the methods
chosen
3. Please present the final results and the most important conclusions in the form of a
presentation (e.g. Google slides)

<br/>

**How to calculate the liquidity**
Liquidity is understood as the % of ads that received at least 1 response (by phone or e-mail)
within 7 days.

Example:
```
On April 1, the user added 10 ads to the website

From 1 to 7 April, he received responses to 6 ads.

On April 2, another 5 ads were added and he received replies to all of them within 7 days of
their appearance on the site

The liquidity is (6 + 5) / (10 + 5) = 73%
```

<br/>

## Dataset
The data we have at our disposal:
1. Data_ads (`date, user_id, ad_id, category_id, params`) - here you can find information about ads
2. Data_replies (`date, user_id, ad_id, mails, phones`) - information about replies to the ads on a given day
3. Data_categories (`category_id, category_name`) - mapping to a category tree
4. Data_segments (`user_id, segment`) - mapping to segmentation for each user

<br/>

## Analysis (ppt)

<br/>

**Scope**
**Objective**

WIP

**Data**

WIP

<br/>

**Briefing and Model**

WIP

<br/>

**Top 5 Insights**

WIP

<br/>

## Project repository structure
The following folders and files are contained in the project repository:

```
.liquidity
|
│   README.md                          # Project description and documentation
│   .gitignore                         # Files and extension ignored in commited
│   docker-compose.yml                 # Container for postgres and pgadmin
│   requirements.txt        
│
└───data                               # Locally data source (csv files)
│   └───raw
│   │   │   data_ads.csv
│   │   │   data_replies.csv
│   │   │   data_segments.csv
│   │   │   data_categories.csv
│   │
│   └───processed
│       │   ...
│   
└───resources                          # Project resources (images, others...)    
│     │   database-pgadmin.png
│   
└───notebooks                          # Jupyter notebooks
│   │   data-analysis.ipynb
│   │   etl.ipynb
│   │   data_exploration.ipynb
└───src                                # Source code - Python code
│    |   create_tables.py
│    |   etl.py 
│    |   sql_queries.py
```

<br/>

The main files:

* `etl.ipynb` reads and processes a single file from data and loads the data into final tables. This notebook contains detailed instructions on the ETL process for each of the tables.

* `data_exploration.ipynb` notebooks which make it possible to explore the data and present some statistical data on them. I present some graphs.

* `sql_queries.py` contains all sql queries, and it's used (imported) in other files or scripts.

* `create_tables.py` drops and creates your tables. This file should always be executed before running the ETL scripts. The db should be cleaned.

* `etl.py` reads and processes files from data and loads them into final tables.

<br/>

## Requirements

The following tools and packages are necessary to run the scripts locally:

* Git
* Python3
    * jupyter notebooks
* Requirements
* Docker
* Docker-Compose
    * _PostgresSQL_
    * _PgAdmin_

<br/>

## How to use the Repository (for running locally in your machine)

<br/>

**Clone repository**

``` bash
git clone https://github.com/dacosta-github/liquidity.git 
```

<br/>

**Change directory to local repository**

```bash
cd liquidity
```

<br/>

**Start postgres and pgadmin docker container**

_Run this command in new terminal window or tab_

```bash
docker-compose up
```

_check containers_
```bash
docker ps # run in new terminal
```

<br/>

**Create and active python virtual environment**

_Run these following commands in new terminal window or tab_
```bash
python3 -m venv python-venv            
source python-venv/bin/activate 
```

<br/>
   
**Install requirements**

```bash
pip install -r requirements.txt  
```

<br/>

**Run the DDL and ETL scripts**

```bash
cd src
python -m create_tables  # create database schema DDL
```

_Log obtained after execution:_
```bash
(python-venv) user@user src % python -m create_tables
Creating database: 2021-04-27 11:24:01.092774
Process executed with success. Database created: 2021-04-27 11:24:01.241855
```

<br/>

```bash
python -m etl            # load one file per commit ETL
```

_Log obtained after execution:_
```bash
(python-venv) user@user src % python -m etl
ETL Step - Creating Postgresql Connection: 2021-04-27 11:36:58.247971
ETL Step - Postgresql Connection Created: 2021-04-27 11:36:58.257116
ETL Step - Cleaning all final tables: 2021-04-27 11:36:58.257150
ETL Step - All final tables cleaned: 2021-04-27 11:36:58.282344
ETL Step - Loading Data Processing to ads: 2021-04-27 11:36:58.282388
ETL Step - Load Data Processing to ads table completed: 2021-04-27 11:37:20.115963
ETL Step - Loading Data Processing to categories: 2021-04-27 11:37:20.116006
ETL Step - Load Data Processing to categories table completed: 2021-04-27 11:37:20.180858
ETL Step - Loading Data Processing to segments: 2021-04-27 11:37:20.180910
ETL Step - Load Data Processing to segments table completed: 2021-04-27 11:37:21.741640
ETL Step - Loading Data Processing to replies: 2021-04-27 11:37:21.741681
ETL Step - Load Data Processing to replies table completed: 2021-04-27 12:29:30.367915
...
```
<br/>


**Check results**

_This command launches the **Jupyter Notebook** application and opens an installation in the browser automatically. Afterwards, you should navigate to the notebook folder and open the `data-analysis.ipynb`. notebook later is able to run the code._

```bash
cd notebooks
jupyter notebook     # http://127.0.0.1:8888/?token=XXXXXXXXXXXXXXX
```
<br/>

**Exploring the database**
_You should open the following link in your web browser:_

```bash
http://localhost:5555/browser/     # Email: student@pgadmin.org | Password: student
```
<br/>


**Cleaning virtual environment**

After all validations you can delete the created environments (python and docker). To do this, use the following commands:

On the same terminal as the python env, execute:

```bash
ctrl+c # to close Jupyter Notebook instance, use Ctrl+C in the terminal
```

```bash
cd ..
cd liquidity
deactivate
rm -r python-venv
```

On the same terminal as the docker, execute:

```bash
ctrl+c  # to close Docker Containers, use Ctrl+C in the terminal
```

```bash
docker ps
docker kill
docker system prune -a  # select y
```

```bash
docker volume ls
docker volume prune # select y
```

```bash
docker network ls
docker network prune  # select y
```

### Kill database sessions

```sql
SELECT pg_terminate_backend(pid) 
FROM  pg_stat_activity 
WHERE 
    -- don't kill my own connection!
    pid <> pg_backend_pid()
    -- don't kill the connections to other databases
    AND datname = '"liquidity_db"'
    ;
```