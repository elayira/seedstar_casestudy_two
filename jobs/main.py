from .utility import query_jobs, save_jobs


if __name__ == '__main__':

    jobs = query_jobs()
    save_jobs(jobs)
    print('job data save completed')
               
    
  