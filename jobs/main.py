from .utility import query_jobs, save_jobs
import settings


if __name__ == '__main__':

    jobs = query_jobs(settings.url)
    save_jobs(jobs)
    print('job data save completed')
               
    
  
