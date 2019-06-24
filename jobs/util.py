import os
import json
import sqlite3
import settings

def jenkins_connection(url, username, password):
    server = jenkins.Jenkins(url, username=username, password=password)
    try:
        server.get_whoami()
        return server
    except jenkins.JenkinsException as err:
        print "There was an error in authentication!
        raise err

def initDB():
    if not os.path.exists("{}".format(settings.DB_NAME)):
        connect = sqlite3.connect("{}".format(settings.DB_NAME))
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE jobs
                    (status text, date text)"""
        )
        connect.commit()
        connect.close()
    connect = sqlite3.connect("{}".format(settings.DB_NAME))
    return connect


# Class for defining a Tweet
def save_jobs(jobs, query=None):
    connect = initDB()
    query = query or "INSERT INTO jobs (status text, date text) VALUES (?, ?)"

   
    if len(jobs) > 1:       
        connect.cursor().executemany(query, jobs)
    else:
        connect.cursor().execute(query, jobs)
    connect.commit()
       
def query_jenkin(url):
    jenkins_server = jenkins_connection(
        url,
        settings.USERNAME,
        settings.PASSWORD
    )
        
    jobs = [jenkins_server.get_job_info(job.name) for job in jenkins_server.get_jobs()]
        
    return [(job.result, job.timestamp) for job in jobs]
   
   
      

 
