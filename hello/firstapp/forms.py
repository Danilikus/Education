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
class UserForm(forms.Form):
    city = forms.TypedMultipleChoiceField(label="Выберите город",
        empty_value=None,
            choices=((1, "Москва"),
                (2, "Воронеж"),
                (3, "Курск"),
                (4, "Томск")))