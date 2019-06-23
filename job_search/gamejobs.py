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
    job_link = []
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
                job_link.append(fetch_job_link(job_key))
        start_page += 1
    search_result = pd.DataFrame()
    search_result['Job title'] = job_title
    search_result['Company\'s link'] = job_link

    search_result.to_excel(f'{file_name}.xlsx')


def fetch_job_link(key):
    # Fetch web page
    page = requests.get(f'https://gamejobs.co{key}').content
    # parse webpage
    page = BeautifulSoup(page, 'html.parser')
    # look for job link
    for offer in page.find_all('a'):
        if offer.text == 'Apply on Company Site':
            link = offer.get('href')
    return link


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
