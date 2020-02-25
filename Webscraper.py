import requests
import os
from bs4 import BeautifulSoup
import csv



def view_random_company():
    '''
    Task 1
    view the random company website, print to the console
    '''

    url = "http://18.207.92.139:8000/random_company"
    response = requests.request("GET", url)
    print('================ Task 1 ========================')
    print(response.text)

def parse_name_purpose(html):
    '''
    Task 2
    parse the html and get name and purpose
    :param html:
    :return: name, purpose
    '''
    soup = BeautifulSoup(html, 'html.parser')
    soups = soup.find_all('li')
    for soup in soups:
        if 'Name' in soup.text:
            name = soup.text[soup.text.find('Name') + 6:]
        elif 'Purpose' in soup.text:
            purpose = soup.text[soup.text.find('Purpose') + 9:]
    return name, purpose


def download_html_extract():
    '''
    Task 2
    download html files into 'data' file
    extract name and purpose
    :return: a list of [name, purpose]
    '''
    lst = []
    print('================ Task 2 ========================')
    isExists = os.path.exists('data')
    if not isExists:
        os.makedirs('data')
    # loop 50 times
    for i in range(50):
        # download
        url = "http://18.207.92.139:8000/random_company"
        response = requests.request("GET", url)
        txt = str(response.text)
        print('downloading into data/%d.html' % i)
        open('data/%d.html' % i, 'w').write(txt)
        # extract name and purpose
        name, purpose = parse_name_purpose(txt)
        lst.append([name, purpose])
    return lst


def save_names_and_purposes(lst):
    '''
    Task 3
    use the [name, purpose] list and write them into csv file
    :param lst
    '''
    print('================ Task 3 ========================')
    f = open('result.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(f)

    csv_writer.writerow(['name', 'purpose'])
    for name, purpose in lst:
        csv_writer.writerow([name, purpose])
    f.close()

if __name__ == '__main__':
    view_random_company()
    lst = download_html_extract()
    save_names_and_purposes(lst)

