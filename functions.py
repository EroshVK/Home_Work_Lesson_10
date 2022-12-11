import json


def load_candidates():
    '''
     Загружает данные из файла
    '''
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_all():
    '''
     Показывает всех кандидатов
    '''
    return load_candidates()

def get_by_pk(pk):
    '''
     Возвращает кандидата по pk
    '''
    for item in get_all():
        if pk == item['pk']:
            return item

def get_by_skill(skill_name):
    '''
     Возвращает кандидата по навыку
    '''
    candidates_for_skill = []
    for item in get_all():
        if skill_name.lower() in item['skills'].lower():
            candidates_for_skill.append(item)
    return candidates_for_skill
