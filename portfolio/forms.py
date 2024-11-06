from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, required=True)
#     email = forms.EmailField(required=True)
#     subject = forms.CharField(max_length=150, required=True)
#     message = forms.CharField(widget=forms.Textarea, required=True)



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)



# Allergy

class AllergyForm(forms.Form):
    allergen_type = forms.ChoiceField(choices=[
        ('Food - Wheat', 'Food - Wheat'),
        ('Food - Nuts', 'Food - Nuts'),
        ('Food - Dairy', 'Food - Dairy'),
        ('Food - Seafood', 'Food - Seafood'),
        ('Environmental - Pollen', 'Environmental - Pollen'),
        ('Environmental - Dust', 'Environmental - Dust'),
        ('Environmental - Mold', 'Environmental - Mold'),
        ('Environmental - Insect', 'Environmental - Insect'),
        ('Food - Spices', 'Food - Spices'),
    ])
    ige_levels = forms.FloatField(label='IgE Levels (kU/L)')
    exposure_frequency = forms.ChoiceField(choices=[
        ('Rarely', 'Rarely'),
        ('Monthly', 'Monthly'),
        ('Daily', 'Daily'),
        ('Seasonal', 'Seasonal'),
    ])
    symptoms = forms.ChoiceField(choices=[
        ('Oral allergy syndrome', 'Oral allergy syndrome'),
        ('Swelling', 'Swelling'),
        ('Hives', 'Hives'),
        ('Itchy skin', 'Itchy skin'),
        ('Nasal congestion', 'Nasal congestion'),
        ('Coughing', 'Coughing'),
        ('Shortness of breath', 'Shortness of breath'),
        ('Rash', 'Rash'),
        ('Anaphylaxis', 'Anaphylaxis'),
    ])
    family_history = forms.ChoiceField(choices=[
        ('Yes', 'Yes'),
        ('No', 'No'),
    ])

# Electrolyte
class ElectrolyteForm(forms.Form):
    serum_sodium = forms.FloatField(label='Serum Sodium (mmol/L)')
    serum_potassium = forms.FloatField(label='Serum Potassium (mmol/L)')
    serum_calcium = forms.FloatField(label='Serum Calcium (mg/dL)')
    serum_magnesium = forms.FloatField(label='Serum Magnesium (mg/dL)')
    bicarbonate = forms.FloatField(label='Bicarbonate (mmol/L)')
    phosphorus = forms.FloatField(label='Phosphorus (mg/dL)')
    
