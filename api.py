from abc import ABC, abstractmethod
import requests
import os

API_KEY = os.getenv("API_KEY_SUPERJOB")


class Api(ABC):
    """
    Класс для работы с API сайтов с вакансиями
    """

    @abstractmethod
    def get_vacs(self, vacancy):
        pass


class ApiHH(Api):

    def get_vacs(self, vacancy):
        hh_dict = {}
        page = 0
        pages = 1
        while page < pages:
            params = {
                "text": vacancy,
                "per_page": 100,
                "page": page,
            }
            try:
                resp = requests.get("https://api.hh.ru/vacancies", params=params).json()
                hh_dict.update(resp)
                pages = resp['pages']
                page += 1
            except Exception as e:
                print(f'Ошибка при запросе к API HeadHunter: {e}')
                break
        return hh_dict


class ApiSJ(Api):

    def get_vacs(self, vacancy):
        sj_dict = {}
        more = True
        next_url = None
        while more:
            params = {
                "keyword": vacancy,
                "count": 100
            }
            headers = {
                'X-Api-App-Id': API_KEY

            }
            try:
                if next_url is None:
                    resp = requests.get("https://api.superjob.ru/2.0/vacancies", params=params, headers=headers).json()
                else:
                    resp = requests.get(next_url, headers=headers).json()
                sj_dict.update(resp)
                more = resp['more']
                next_url = resp['next_url']
            except Exception as e:
                print(f'Ошибка при запросе к API SuperJob: {e}')
                break
        return sj_dict
