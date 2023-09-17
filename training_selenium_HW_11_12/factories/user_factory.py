from faker import Faker

fake = Faker()


def generate_user_data(**kwargs):
    password = fake.password()
    data = dict(
        name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        password=password,
        repeat_password=password
    )
    data.update(**kwargs)
    return data
