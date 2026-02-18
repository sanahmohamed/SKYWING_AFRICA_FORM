from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            'full_name', 'contact_number', 'email', 'nationality', 'age',
            'budget', 'property_type', 'date_of_attending', 'time_slot', 'reference'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'w-full border border-gray-300 rounded px-4 py-3 text-sm uppercase tracking-widest text-gray-500 focus:outline-none focus:border-yellow-500 focus:ring-1 focus:ring-yellow-500',
            }),
            'contact_number': forms.TextInput(attrs={
                'placeholder': 'CONTACT NUMBER',
                'class': 'w-full border border-gray-300 rounded px-4 py-3 text-sm uppercase tracking-widest text-gray-500 focus:outline-none focus:border-yellow-500 focus:ring-1 focus:ring-yellow-500',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'EMAIL ADDRESS',
                'class': 'w-full border border-gray-300 rounded px-4 py-3 text-sm uppercase tracking-widest text-gray-500 focus:outline-none focus:border-yellow-500 focus:ring-1 focus:ring-yellow-500',
            }),
            'nationality': forms.TextInput(attrs={
                'placeholder': 'NATIONALITY',
                'class': 'w-full border border-gray-300 rounded px-4 py-3 text-sm uppercase tracking-widest text-gray-500 focus:outline-none focus:border-yellow-500 focus:ring-1 focus:ring-yellow-500',
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Age',
                'class': 'w-full border border-gray-300 rounded px-4 py-3 text-sm text-gray-500 focus:outline-none focus:border-yellow-500 focus:ring-1 focus:ring-yellow-500',
                'min': '18',
                'max': '120',
            }),
            'budget': forms.RadioSelect(attrs={
                'class': 'radio-custom',
            }),
            'property_type': forms.RadioSelect(attrs={
                'class': 'radio-custom',
            }),
            'date_of_attending': forms.RadioSelect(attrs={
                'class': 'radio-custom',
            }),
            'time_slot': forms.RadioSelect(attrs={
                'class': 'radio-custom',
            }),
            'reference': forms.TextInput(attrs={
                'placeholder': 'YOUR REFERENCE',
                'class': 'w-full border border-gray-300 rounded px-4 py-3 text-sm uppercase tracking-widest text-gray-500 focus:outline-none focus:border-yellow-500 focus:ring-1 focus:ring-yellow-500',
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            return email.lower()
        return email

    def clean_full_name(self):
        name = self.cleaned_data.get('full_name')
        if name and len(name.strip()) < 2:
            raise forms.ValidationError('Please enter your full name.')
        return name

    def clean_contact_number(self):
        number = self.cleaned_data.get('contact_number')
        if number and len(number.strip()) < 5:
            raise forms.ValidationError('Please enter a valid contact number.')
        return number
