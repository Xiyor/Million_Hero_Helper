import webbrowser
import requests
import html2text
import lxml.etree as etree

def start_search(content):
    #driver = webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s')
    process_url = 'https://www.bing.com/search?q={}'.format(content)
    print(process_url)
    #driver.open_new_tab(process_url)
    res = requests.get(process_url).text
    decompose(res)


def decompose(html):
    tree = etree.HTML(html)
    property_list_reg = '//ol[@id="b_results"]//div[@class="b_caption"]'
    property_lst = tree.xpath(property_list_reg)
    print("property: {}".format(property_lst))
    for e in property_lst:
        print(e.xpath('string(.)'))
    print(len(property_lst))


