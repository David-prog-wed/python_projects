DATA = [
    {
        'name': 'ernesto',
        'age': 72,
        'organization': 'silicon',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'silicon',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'silicon',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'silicon',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

#High order funcions  filter, map and reduce  / merge list + con diccionarios |

def run():
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
#    all_silicon_workers = [worker['name'] for worker in DATA if worker['organization'] == 'silicon']
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    all_silicon_workers = list(filter(lambda worker: worker['organization'] == 'silicon', DATA))
    all_silicon_workers = list(map(lambda worker: worker['name'], all_silicon_workers))

    #all_silicon_workers = list(filter(lambda worker: worker['organization'] == 'silicon', DATA))
    #all_silicon_workers = list(map(lambda worker: worker['name'], all_silicon_workers))

    
    for worker in all_silicon_workers:
        print(worker)


if __name__ == '__main__':
    run()
  


  # Nuevo Reto

  #Con list comprehensions
# adults = [worker ['name'] for worker in DATA if worker ['age'] > 18]
# old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]

# #Con high order functions
# all_python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))
# all_python_devs = list(map(lambda worker: worker['name'], all_python_devs))

# all_silicon_workers = list(filter(lambda worker: worker['organization'] == 'silicon', DATA))
# all_silicon_workers = list(map(lambda worker: worker['name'], all_silicon_workers))