from django.shortcuts import render,redirect
#from .models import Project
#from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from threading import Thread
from django.conf import settings
from django.http import HttpResponse

#from .forms import AllergyForm
#from .models import Allergy

#from .forms import ElectrolyteForm
#from .models import ElectrolyteModel

from .models import Project, Allergy, ElectrolyteModel
from .forms import ContactForm, AllergyForm, ElectrolyteForm
import joblib
import pandas as pd
import numpy as np
import os


print("Current directory:", os.getcwd())
print("Template directories:", settings.TEMPLATES)


# def home(request):
#     projects = Project.objects.all()
#     return render(request, 'portfolio/home.html', {'projects': projects})

# 
def hh(request):
    return render(request, 'portfolio/hh.html')
def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def resume(request):
    return render(request, 'portfolio/resume.html')

def publication(request):
    return render(request, 'portfolio/publication.html')

def github(request):
    return render(request, 'portfolio/github.html')

def data_science_blog(request):
    return render(request, 'portfolio/data_science_blog.html')

def photography(request):
     return render(request, 'portfolio/photography.html')

# views.py
from django.core.mail import send_mail, BadHeaderError


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"Subject: {subject}\n\nMessage from {name}\nEmail: {email}\n\nMessage:\n{message}"
        #full_message = f"Message from {name}\n, Email: {email}\n\n{message}"
        try:
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                ['sayprincekumar20@gmail.com'],  # Replace with the email to receive messages
                fail_silently=False,
            )
            return HttpResponse("Email sent successfully!")
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")
    
    return render(request, "portfolio/contact.html")

from django.shortcuts import render

def data_science_blog(request):
    return render(request, 'portfolio/data_science_blog.html')
      
# Load models and feature names
allergy_model_path = os.path.join(os.path.dirname(__file__), 'allergy_train_model.pkl')
allergy_feature_names_path = os.path.join(os.path.dirname(__file__), 'allergy_model_features.pkl')
allergy_model = joblib.load(allergy_model_path)
allergy_feature_names = joblib.load(allergy_feature_names_path)

electrolyte_model_path = os.path.join(os.path.dirname(__file__), 'electrolyte_train_model.pkl')
electrolyte_scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')
electrolyte_model = joblib.load(electrolyte_model_path)
electrolyte_scaler = joblib.load(electrolyte_scaler_path)

#  allergy_prediction
def allergy_prediction(request):
    if request.method == 'POST':
        form = AllergyForm(request.POST)
        if form.is_valid():
            # Prepare data for prediction
            input_data = {
                'IgE Levels (kU/L)': form.cleaned_data['ige_levels'],
                'Exposure Frequency': form.cleaned_data['exposure_frequency'],
                'Allergen Type': form.cleaned_data['allergen_type'],
                'Symptoms': form.cleaned_data['symptoms'],
                'Family History': form.cleaned_data['family_history']
            }

            # Create a DataFrame for prediction
            df_input = pd.DataFrame([input_data])
            df_input = pd.get_dummies(df_input)

            # Align columns with the model's expected input
            df_input = df_input.reindex(columns=allergy_feature_names, fill_value=0)

            # Debugging: Print shapes and expected features
            print("Allergy prediction df_input shape:", df_input.shape)
            print("Expected feature names:", allergy_feature_names)

            if df_input.shape[1] == len(allergy_feature_names):
                prediction = allergy_model.predict(df_input)
                reaction_severity = prediction[0]

                # Save to database
                Allergy.objects.create(
                    allergen_type=form.cleaned_data['allergen_type'],
                    ige_levels=form.cleaned_data['ige_levels'],
                    exposure_frequency=form.cleaned_data['exposure_frequency'],
                    symptoms=form.cleaned_data['symptoms'],
                    family_history=form.cleaned_data['family_history'],
                    reaction_severity=reaction_severity
                )

                return render(request, 'predictor/result.html', {'reaction_severity': reaction_severity})
            else:
                return HttpResponse("Feature alignment error for allergy prediction.")
    else:
        form = AllergyForm()

    return render(request, 'predictor/predict.html', {'form': form})


# Electrolyte Prediction
def electrolyte_prediction(request):
    if request.method == 'POST':
        form = ElectrolyteForm(request.POST)
        if form.is_valid():
            # Get the cleaned data
            data = form.cleaned_data
            features = np.array([[data['serum_sodium'], data['serum_potassium'],
                                  data['serum_calcium'], data['serum_magnesium'],
                                  data['bicarbonate'], data['phosphorus']]])
            # Scale the features
            feature_scaled = electrolyte_scaler.transform(features)

            # Make prediction
            prediction = electrolyte_model.predict(feature_scaled)

            # Save to database
            ElectrolyteModel.objects.create(
                serum_sodium=data['serum_sodium'],
                serum_potassium=data['serum_potassium'],
                serum_calcium=data['serum_calcium'],
                serum_magnesium=data['serum_magnesium'],
                bicarbonate=data['bicarbonate'],
                phosphorus=data['phosphorus'],
                outcome=prediction[0]
            )

            return render(request, 'electrolyte/electrolyte_result.html', {'electrolyte_prediction': prediction[0]})
    else:
        form = ElectrolyteForm()

    return render(request, 'electrolyte/electrolyte_predict.html', {'form': form})


def blogs_1(request):
    return render(request,'blogs/Amazon Sales Data.html')

def blogs_2(request):
    return render(request,'blogs/Delhi Metro Network Analysis .html')

def blogs_3(request):
    return render(request,'blogs/Health Monitoring and Analysis using Python.html')

def blogs_4(request):
    return render(request,'blogs/Spotify.html')

def blogs_5(request):
    return render(request,'blogs/Amazon Sales Data/html')

def blogs_6(request):
    return render(request,'blogs/Amazon Sales Data.html')



# views.py
import nbformat
from nbconvert import HTMLExporter
from django.shortcuts import render

def render_notebook_tmdb_movies(request):
    # Define the path to the notebook
    notebook_path = 'portfolio/templates/blogs/tmdb-Movies.ipynb'

   # notebook_path = r'C:\Users\prince_singh04\myportfolio\portfolio\templates\blogs\tmdb-Movies.ipynb'
    
    # Load and convert the notebook to HTML
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_content = nbformat.read(f, as_version=4)

    # Convert the notebook to HTML
    html_exporter = HTMLExporter()
    notebook_html, _ = html_exporter.from_notebook_node(notebook_content)

    # Pass the notebook HTML content to a template
    return render(request, 'blogs/notebook_template.html', {'notebook_html': notebook_html})

def render_notebook_T20_World_cup(request):
    # Define the path to the notbook
    notbook_path= 'portfolio/templates/blogs/T20 World Cup 2024 Match Analysis.ipynb'

   # notbook_path= r'C:\Users\prince_singh04\myportfolio\portfolio\templates\blogs\T20 World Cup 2024 Match Analysis.ipynb'

    # Load and convert the notbook to HTML
    with open(notbook_path, 'r', encoding='utf-8') as f:
       notebook_content= nbformat.read(f,as_version=4)

    # convert the notebbok to Html
    html_exploer= HTMLExporter()
    notebook_html_T20, _ =  html_exploer.from_notebook_node(notebook_content)

    # pass the notebook HTML content to a template
    return render (request, 'blogs/notbook_template_T20.html', {'notebook_html_T20': notebook_html_T20})



