import os
from functools import reduce
import tweepy
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
def save_jobs(tweet, query=None):
    connect = initDB()
    query = query or "INSERT INTO jobs (status text, date text) VALUES (?, ?)"

   
    if len(tweet) > 1:       
        connect.cursor().executemany(query, jobs)
    else:
        connect.cursor().execute(query, tweet)
    connect.commit()
       
def query_jenkin(url):
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    jenkins_server = jenkins_connection(
        url,
        settings.USERNAME,
        settings.PASSWORD
    )
        
    jobs = [jenkins_server.get_job_info(job.name) for job in jenkins_server.get_jobs()]
    
    
    def reducer(accumulator, currentvalue):
        accumulator = accumulator if accumulator else []
        accumulator.append((currentvalue.result, currentvalue.timestamp))
        return accumulator
        
    return reduce(reducer, jobs, [])
   
   
      

 