from faker import Factory
f = Factory.create()


def get_age(pro):
    return 2016 - int(pro['birthdate'][:4])

r = []
for _ in range(10000):
    profile = f.simple_profile()

    data = (profile['name'], profile['birthdate'], str(get_age(profile)), f.state())
    r.append(data)

with open('./data.csv', 'w') as f:
    for d in r:
        f.write(','.join(d) + "\n")
