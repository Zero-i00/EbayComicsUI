import requests
from bs4 import BeautifulSoup


def get_values_and_grades(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    soup = soup.find('div', class_='container mt-2').find('div', class_='col-12 col-md-6').find('div', class_='tab-pane active')
    containers = soup.find('ul', class_='list-group mb-1').find_all('li', class_='list-group-item')[1:]
    values_and_grades = []
    for container in containers:
        try:
            container = container.find('div', class_='row')
            grade = container.find('div', class_='col-3 col-xl-2').text.strip()
            value = container.find('div', class_='col-5 col-xl-6 pr-xl-0 text-right').find('div', class_='col-12 col-xl-7')
            if value is None:
                value = container.find('div', class_='col-5 col-xl-6 pr-xl-0 text-right').find('div', class_='col-12 col-xl-7 text-muted')
            value = value.text.strip().rstrip('*')
            values_and_grades.append((grade, value))
        except Exception:
            pass
    print(values_and_grades)
    return values_and_grades


if __name__ == "__main__":
    test_url = 'https://comics.gocollect.com/guide/view/124346'
    get_values_and_grades(test_url)