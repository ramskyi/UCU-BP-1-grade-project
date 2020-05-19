from selenium import webdriver
import time
import re
from pathlib import Path


base_url = 'https://www.metal-archives.com/lists/'
letters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z NBR ~'.split()


def chunks_count(page_source):
    """
    Takes source code and returns count of chunks of band entries
    considering there no more than 500 entries per chunk.
    """
    # Example: "Showing 1 to 500 of 11,839 entries"
    pattern = re.compile('Showing .* entries')
    matches = re.findall(pattern, page_source)
    matches = matches[0].split()
    entries_count = int(''.join(matches[5].split(',')))
    return (entries_count // 500) + int(entries_count % 500 > 0)


def band_urls_list(page_source):
    """
    Forms and returns a list of urls of bands, taking a page source.
    """
    pattern = re.compile(
        '<a href="https://www\.metal-archives\.com/bands/[^<>]*>')
    matches = re.findall(pattern, page_source)
    for i in range(len(matches)):
        matches[i] = matches[i].split('"')[1]
    return matches


def scrape_band_list():
    """
    Scrapes all bands urls from www.metal-archives.com and writes them
    out in polygon/band_url_list.txt
    :return:
    """
    out_file = open(Path('..') / 'polygon' / 'band_url_list.txt', 'w')
    driver = webdriver.Firefox()
    for letter in letters:
        driver.get(base_url + letter)
        time.sleep(5)
        count = chunks_count(driver.page_source)
        for i in range(count):
            lst = band_urls_list(driver.page_source)
            print(len(lst))
            for url in band_urls_list(driver.page_source):
                out_file.write(url + '\n')
            if i != count - 1:
                btn = '//a[@class="next paginate_button"]'
                next_button = driver.find_element_by_xpath(btn)
                next_button.click()
                time.sleep(3)

    out_file.close()
