from django.shortcuts import render

# Create your views here.
import os
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'ml_model', 'restaurant_rating_model.pkl')

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)


from django.shortcuts import render
from .forms import RestaurantRatingForm
import pandas as pd

def predict_rating_form(request):
    predicted_rating = None

    if request.method == 'POST':
        form = RestaurantRatingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Convert boolean values to 'Yes'/'No' because model expects these strings
            bool_map = {True: 'Yes', False: 'No'}
            features = {
                'Price range': int(data['price_range']),
                'Rating text': data['rating_text'],
                'Rating color': data['rating_color'],
                'Has Table booking': bool_map[data['has_table_booking']],
                'Has Online delivery': bool_map[data['has_online_delivery']],
                'Is delivering now': bool_map[data['is_delivering_now']],
                'Switch to order menu': bool_map[data['switch_to_order_menu']],
                'Currency': data['currency'],
                'City': data['city'],
                'Average Cost for two': data['average_cost_for_two'],
            }

            df = pd.DataFrame([features])
            predicted_rating = model.predict(df)[0]
    else:
        form = RestaurantRatingForm()

    return render(request, 'ml_model/predict_form.html', {'form': form, 'predicted_rating': predicted_rating})



def landing_page(request):
    return render(request, 'ml_model/index.html')