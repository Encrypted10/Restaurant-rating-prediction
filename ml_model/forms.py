from django import forms

class RestaurantRatingForm(forms.Form):
    PRICE_RANGE_CHOICES = [(1, '1'), (2, '2')]
    RATING_TEXT_CHOICES = [
        ('Poor', 'Poor'),
        ('Average', 'Average'),
        ('Good', 'Good'),
        ('Very Good', 'Very Good'),
        ('Excellent', 'Excellent'),
    ]
    RATING_COLOR_CHOICES = [
        ('Red', 'Red'),
        ('Orange', 'Orange'),
        ('Green', 'Green'),
        ('Dark Green', 'Dark Green'),
    ]

    price_range = forms.ChoiceField(choices=PRICE_RANGE_CHOICES, label="Price Range")
    rating_text = forms.ChoiceField(choices=RATING_TEXT_CHOICES, label="Rating Text")
    rating_color = forms.ChoiceField(choices=RATING_COLOR_CHOICES, label="Rating Color")

    has_table_booking = forms.BooleanField(required=False, label="Has Table Booking")
    has_online_delivery = forms.BooleanField(required=False, label="Has Online Delivery")
    is_delivering_now = forms.BooleanField(required=False, label="Is Delivering Now")
    switch_to_order_menu = forms.BooleanField(
    required=False,
    label="Switch to Order Menu",
    initial=False,
    disabled=True,
)


    currency = forms.CharField(max_length=20)
    city = forms.CharField(max_length=50)
    average_cost_for_two = forms.FloatField(label="Average Cost for Two")
