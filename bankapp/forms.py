from django import forms

from bankapp.models import Person, City


GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]
MATERIALS_PROVIDE_CHOICE = [
 ('Debit Card', 'Debit Card'),
 ('Credit Card', 'Credit Card'),
 ('Check Book', 'Check Book'),
]
class PersonCreationForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    materials = forms.MultipleChoiceField(label='Materials Provide', choices=MATERIALS_PROVIDE_CHOICE,
                                         widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter Your Email-ID'}),
            'address': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your Address'}),
            'age': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your Age'}),
            'dob': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'account': forms.Select(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'mob': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter Your Mobile Number'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['city'].queryset = City.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.district.city_set.order_by('name')