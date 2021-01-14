# Asylum | Human Rights First

![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Framework](https://img.shields.io/badge/Framework-FastAPI-red)
![Webdriver](https://img.shields.io/badge/Webdriver-Selenium-green)
![NLP-Library](https://img.shields.io/badge/NLP_Library-Spacy-cyan)
![Database](https://img.shields.io/badge/Database-AWS_S3-peach)
![Database](https://img.shields.io/badge/Database-AWS_RDS_PostgreSQL-yellow)
![Paas](https://img.shields.io/badge/Paas-AWS_Elastic_Beanstalk-orange)

I was part of a cross functional team consisting of 3 Data Scientists, 2 Front-end and 1 Back-end developer. We collaborated remotely to work on a greenfield project from a non-profit organization, Human Rights First.

## About the Non-profit Organization and its Asylum Representation Program

Human Rights First is an independent advocacy and action organization that challenges America to live up to its ideals. They believe American leadership is essential in the global struggle for human rights, so they press the U.S. government and private companies to respect human rights and the rule of law. When they fail, they step in to demand reform, accountability, and justice. Around the world, they work where they can best harness American influence to secure core freedoms.

The asylum representation program helps people who have fled dangerous situations in their home countries to obtain asylum in the United States. Asylum is a legal status that the U.S. government can grant to people who are at risk of harm in their home countries because of who they are — because of their religion, political opinion, sexual orientation, or ethnicity, for example — if the governments in their home countries will not protect them.

The process for seeking asylum in the U.S. is complicated and an asylum-seeker is more likely to be granted this form of protection if he or she is represented by a good lawyer who understands the system. Our pro bono legal representation program matches good lawyers with asylum-seekers who need help and would not otherwise be able to afford high-quality legal representation.

## Product Vision

We worked on designing a web tool backed by data science to aggregate data on asylum cases, allowing users to explore data, make predictions, and visualize how a judge might rule on a specific asylum case considering the elements of that case.

Using this tool the attorneys will be able to prepare their case better which will significantly increase the chances of winning the case for the refugees, and getting them asylum in the United States.

## My Contributions

Since we were working on a greenfield project, the first and foremost challenge that we faced was not having any data to start off with. The main task was downloading the pdfs and then parsing data from the PDF for each individual case. The list of PDF having no uniformity made data parsing even trickier.

### Parsing data from PDFs

I was involved in making a web crawler using Selenium that would download the list of PDFs from the website that we were given. After we had our PDFs downloaded, our next challenge was to parse the useful information from the document. The idea behind the process was to somehow convert the PDF into plain text and then use Natural Language Processing to extract the relevant information.

Documents being the searchable PDFs it made it easy to use one of the third-party libraries that will convert the PDF into plain text. Had it been an image PDF the process of converting it into text would have been a lot more complex using OCR (Optical Character Recognition).

After extracting the plain text, I had an option to use one of the two well known Natural Language Processing libraries; NLTK and Spacy. Spacy is a newer library that is more accurate and a lot faster I went with Spacy. Using Spacy’s named entity recognition I was able to extract the names from the document.

![123](https://user-images.githubusercontent.com/67918990/104557048-938db280-560e-11eb-9499-858a8439fb53.png)

The challenge that I faced extracting the names was that the names in the PDF were in the format of Last name, First name. Spacy was outputting one full name as two separate names. I came across a Class, Matcher in Spacy where we are able to match sequences of tokens, based on custom pattern rules. Using matcher along with named entities Class I was able to extract the full names.

### Built REST API using FAST API

I also took the charge of making a REST API to feed data to our front-end team. I used FastAPI as it’s a relatively new web framework for Python claiming to be one of the fastest Python frameworks available.

![124](https://user-images.githubusercontent.com/67918990/104557055-95f00c80-560e-11eb-9858-63e3c4025f29.png)

Inside the app folder, I had made separate files that were performing individual tasks rather than throwing everything in the main file. This made things more organized and it’s easier to debug. The database connection using SQLAlchemy was handled in the database.py file, and the SQLAlechmy models were all put in the models.py file. The endpoints were all put in the routes file, and the main.py file was where all the modular components were put together.

### Amazon RDS for PostgreSQL

I took the responsibility of managing and hosting the Postgres database on AWS RDS.

### Deployed Using Amazon Elastic Beanstalk

I was also involved in helping my teammate to containerize the application using Docker, and then deploying it on AWS Beanstalk.
