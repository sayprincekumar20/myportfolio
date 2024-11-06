from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField()

    def __str__(self):
        return self.title


# Allery
class Allergy(models.Model):
    ALLERGEN_TYPES = [
        ('Food - Wheat', 'Food - Wheat'),
        ('Food - Nuts', 'Food - Nuts'),
        ('Food - Dairy', 'Food - Dairy'),
        ('Food - Seafood', 'Food - Seafood'),
        ('Environmental - Pollen', 'Environmental - Pollen'),
        ('Environmental - Dust', 'Environmental - Dust'),
        ('Environmental - Mold', 'Environmental - Mold'),
        ('Environmental - Insect', 'Environmental - Insect'),
        ('Food - Spices', 'Food - Spices'),
    ]

    EXPOSURE_FREQUENCIES = [
        ('Rarely', 'Rarely'),
        ('Monthly', 'Monthly'),
        ('Daily', 'Daily'),
        ('Seasonal', 'Seasonal'),
    ]

    allergen_type = models.CharField(max_length=50, choices=ALLERGEN_TYPES)
    ige_levels = models.FloatField()
    exposure_frequency = models.CharField(max_length=20, choices=EXPOSURE_FREQUENCIES)
    symptoms = models.CharField(max_length=50)
    family_history = models.CharField(max_length=3)  # Yes/No
    reaction_severity = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.allergen_type} - {self.reaction_severity}"


# Electrolyte
class ElectrolyteModel(models.Model):
    serum_sodium = models.FloatField()
    serum_potassium = models.FloatField()
    serum_calcium = models.FloatField()
    serum_magnesium = models.FloatField()
    bicarbonate = models.FloatField()
    phosphorus = models.FloatField()
    outcome = models.CharField(max_length= 50)

    def __str__(self):
        return f"Electrolyte Data - {self.outcome}"
        