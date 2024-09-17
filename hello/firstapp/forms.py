from django import forms

# class UserForm(forms.Form):
#     file = forms.ImageField(label="Изображение")
# class UserForm(forms.Form):
#     date = forms.DateField(label="Введите дату")
# class UserForm(forms.Form):
#     time = forms.DateField(label="Введите время")
# class UserForm(forms.Form):
#     date_time = forms.DateTimeField(label="Введите дату и время")
# class UserForm(forms.Form):
#     time_delta = forms.DurationField(label="Введите промежуток времени")
# class UserForm(forms.Form):
#     date_time = forms.SplitDateTimeField(label="Введите дату и время")
# class UserForm(forms.Form):
#     num = forms.IntegerField(label="Введите целое число")
# class UserForm(forms.Form):
#     num = forms.DecimalField(label="Введите десятичное число")
# class UserForm(forms.Form):
#     num = forms.DecimalField(label="Введите десятичное число", decimal_places=2)
# class UserForm(forms.Form):
#     num = forms.FloatField(label="Введите число")
# class UserForm(forms.Form):
#     ling = forms.ChoiceField(label="Выберите язык",
#         choices=((1, "Английский"),
#         (2, "Немецкий"),
#         (3, "Французский")))
# class UserForm(forms.Form):
#     city = forms.TypedChoiceField(label="Выберите город",
#         empty_value=None,
#         choices=((1, "Москва"),
#             (2, "Воронеж"),
#             (3, "Курск")))
# class UserForm(forms.Form):
#     country = forms.MultipleChoiceField(label="Выберите страны",
#         choices=((1, "Англия"),
#             (2, "Германия"),
#             (3, "Испания"),
#             (4, "Россия")))

# class UserForm(forms.Form):
#     city = forms.TypedMultipleChoiceField(label="Выберите город",
#         empty_value=None,
#             choices=((1, "Москва"),
#                 (2, "Воронеж"),
#                 (3, "Курск"),
#                 (4, "Томск")))

# class UserForm(forms.Form):
#    name = forms.CharField(label="Имя")
#    age = forms.IntegerField(label="Возраст")
#    comment = forms.CharField(label="Комментарий")

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя")
#  age = forms.IntegerField(label="Возраст")
#  comment = forms.CharField(label="Комментарий",
#  widget=forms.Textarea)

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя", initial="Введите ФИО")
#  age = forms.IntegerField(label="Возраст", initial=18)
#  comment = forms.CharField(label="Комментарий", widget=forms.Textarea)

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя", help_text ="Введите ФИО")
#  age = forms.IntegerField(label="Возраст", help_text ="Введите возраст")

# class UserForm(forms.Form):
#  name = forms.CharField(min_length=2, max_length=20)
#  age = forms.IntegerField(min_value=1, max_value=120)
#  weight = forms.DecimalField(min_value=3, max_value=200, decimal_places=2)
#  email = forms.EmailField(label="Электронный адрес")
#  reklama = forms.BooleanField(label="Coглacны получать рекламу", required=False)

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя клиента")
#  age = forms.IntegerField(label="Возраст клиента")

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя клиента", min_length=3)
#  age = forms.IntegerField(label="Возраст клиента", min_value=1, max_value=100)

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя клиента", min_length=3)
#  age = forms.IntegerField(label="Возраст клиента", min_value=1, max_value=100)
#  required_css_class = "field"
#  error_css_class = "error"

class UserForm(forms.Form):
 name = forms.CharField(label="Имя клиента",
 widget=forms.TextInput(attrs={"class": "myfield"}))
 age = forms.IntegerField(label="Возраст клиента",
 widget=forms.NumberInput(attrs={"class": "myfield"}))

