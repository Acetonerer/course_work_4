from abc import ABC, abstractmethod
import json


class JSONAbc(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(JSONAbc):

    def add_vacancy(self, vacancies):
        data = []
        for vacancy in vacancies:
            vacancy_in_dict = {
                "название": vacancy.title,
                "ссылка": vacancy.url,
                "зарплата": vacancy.salary,
                "требования": vacancy.requirements,
            }
            data.append(vacancy_in_dict)
        with open("../src/vacancy.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def delete_vacancy(self, vacancy):
        with open("../src/vacancy.json", "r", encoding="utf-8") as file:
            vacancies = json.load(file)
            new_vacancies = [vac for vac in vacancies if vacancy not in vac.values()]
        with open("../src/vacancy.json", "w", encoding="utf-8") as file:
            json.dump(new_vacancies, file, ensure_ascii=False, indent=2)