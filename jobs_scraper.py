import requests
from bs4 import BeautifulSoup
import time

print('Enter the skills that you have')
MySkills = input('>')
print(f'Filtering out {MySkills}')
def find_jobs():
    req = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Science&txtLocation=')
    soup = BeautifulSoup(req.content, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_dates = job.find('span', class_='sim-posted').span.text
        if 'few' in published_dates:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_='srp-skills').text.replace(' ','')
            # experience = job.find('i', class_='material-icons').text
            link = job.header.h2.a['href']
            if MySkills in skills:
                with open(f'job_posts/{index}.txt','w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"Direct Link: {link}")
                print(f'File Saved {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait =10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
