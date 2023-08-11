from django.contrib import admin

from app_canado.models import User
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "surname",
        "email",
        "phone",

    ]

class auto(admin.ModelAdmin):
    list_display = [
        "gamintojas",
        "marke",

    ]
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Slaptažodis', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Pakartokite slaptažodį', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password2 != password1:
            raise forms.ValidationError("Slaptažodžiai nesutampa")
        return password2
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]

class MyUserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'is_admin', 'is_active')
    list_filter = ('is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)



admin.site.register(User, MyUserAdmin)

