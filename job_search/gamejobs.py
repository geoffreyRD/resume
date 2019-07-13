# !/usr/bin/env python3
import argparse
import pandas as pd
import re
import requests

from bs4 import BeautifulSoup


def gamejobs_search(job: str, pages_to_search: int, file_name: str = None):
    # lower all case to avoid false negative
    job = job.lower()
    if file_name is None:
        file_name = f'{job}_search_results'
    job_title = []
    job_application_link = []
    job_city = []
    job_company = []
    job_location = []
    start_page = 1
    while pages_to_search >= start_page:
        # Fetch web page
        page = requests.get(f'https://gamejobs.co/?p={start_page}').content
        # parse webpage
        page = BeautifulSoup(page, 'html.parser')
        # seach job in the list of offerts.
        for offer in page.find_all('a'):
            if job in offer.text.lower():
                job_title.append(offer.text)
                # get the key for the job offer page
                job_key = offer.get('href')
                # get description and link to the company's website offer
                job_application_link.append(job_link(job_key))
                # get city and compagny from the job offerts
                job_info = job_details(job_key)
                job_company.append(job_info[0])
                job_location.append(job_info[1])
        start_page += 1
    search_result = pd.DataFrame()
    search_result['Job title'] = job_title
    search_result['Location'] = job_location
    search_result['Company'] = job_company
    search_result['Company\'s link'] = job_application_link
    # Print results in excel
    search_result.to_excel(f'{file_name}.xlsx')


def job_link(key):
    # Fetch web page
    page = requests.get(f'https://gamejobs.co{key}').content
    # parse webpage
    page = BeautifulSoup(page, 'html.parser')
    # look for job link
    for offer in page.find_all('a'):
        if offer.text == 'Apply on Company Site':
            link = offer.get('href')
    return link


def job_details(key):
    # Fetch web page
    page = requests.get(f'https://gamejobs.co{key}').content
    # parse webpage
    page = BeautifulSoup(page, 'html.parser')
    # look for job link
    position = 0
    for content in page.find_all('div'):
        if position == 1:
            company = content.string
        if position == 2:
            city = content.string
        position += 1
    return company, city


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--job', type=str, help='The job you\'re looking for.', required=True)
    parser.add_argument('--pages', type=int, help='Number of pages to scrap.', required=True)
    parser.add_argument('--file', type=str, help='Name of the output excel file',
                        required=False, default=None)
    args = parser.parse_args()

    gamejobs_search(
        job=args.job,
        pages_to_search=args.pages,
        file_name=args.file
    )

    print('Done!')
