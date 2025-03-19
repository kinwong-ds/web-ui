
# my_default_prompt="""navigate to the website from the additional information. Create a account from the using email address "kinwong.ds@gmail.com" and password of "G1ttingOffers1nWA!". Task is completed after account is created"""

my_default_prompt="""Go to ‘https://docs.google.com/forms/d/1bYhFsbF2hcpep1E7-oxYDdZbopToQYoaQnIuofy-RbA/edit’ and assist me in completing the form while following these guidelines:
	- Enter the week ending date as per the provided information, then click Next.
	- Navigate to the first job application link and begin answering the questions one by one by getting information from the list of job application link.
	- For the contact date, select a date 1 to 5 days before the week ending date.
	- Utilize a search engine by opening a new tab to research the Employer or business contact information, Address, City&State, Website, and Phone number.
	- After completing one job application entry, click Next on the form to proceed to the second job application from the provided list.
  - Repeat the same process until 3 jobs is filled. Click Submit form when done.
	- If a job application link is unavailable, skip it and move on to the next one.
  - Finish one job application before moving onto the next link.
  - Do not sign in to Google.
	- Do not use the same job link for multiple entries.
	- Do not click “Clear Form.”
  - Do not search on the same tab as the Google Form.
	- If a question is unclear or you are unable to find an answer, enter “NA” and move on.
  - Don't fill in the actual job application. Just fill in the Google Form.
	- Once all sections are completed, click Submit and stop all actions.
"""

with open('src/utils/job_apps_links.yaml', 'r') as f:
    lines = f.readlines()
job_apps_links = 'list of job application links: ' + '\n '.join([str(i+1) + ". " + line.strip() for i, line in enumerate(lines)])

my_add_infos=f"""
Week ending: March 14, 2025

{job_apps_links}

"""
