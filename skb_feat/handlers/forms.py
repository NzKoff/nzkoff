from wtforms import Form, StringField, DateField, SelectMultipleField, PasswordField, validators, RadioField


class RegForm(Form):
    login = StringField('Имя пользователя', [validators.Length(min=3, max=25), validators.required()])
    password = PasswordField('Пароль', [
        validators.Length(min=6, max=30),
        validators.required(),
        validators.EqualTo('confirm_password', message='Пароли должны совпадать')]
    )
    confirm_password = PasswordField('Повторите пароль', validators=[
        validators.Length(min=6, max=30),
        validators.required()
    ])
    firstname = StringField('Имя', [validators.Length(min=2, max=30), validators.required()])
    secondname = StringField('Фамилия', [validators.Length(min=2, max=30), validators.required()])
    bday = DateField('Дата рождения', format='%d.%m.%Y')
    sex = RadioField('Пол', choices=[
        (0, 'Мужской'),
        (1, 'Женский')
    ])

    hobbys = SelectMultipleField('Хобби', choices=[
        (0, 'Музыка'),
        (1, 'Театр'),
        (2, 'Кино'),
        (3, 'Цирк'),
        (4, 'Музей'),
        (5, 'Выставка'),
        (6, 'Другое')
    ])
    social_link = StringField('Социальная сеть', validators=[validators.required(), validators.url()])


class LoginForm(Form):
    login = StringField('Имя пользователя', [validators.Length(min=3, max=25), validators.required()])
    password = PasswordField('Пароль', [validators.Length(min=6, max=30),validators.required()])