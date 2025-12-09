# Zac Motors API - Setup & Documentation

## Setup Instructions

### 1. Create Project Structure
```bash
mkdir zac_motors_backend
cd zac_motors_backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install Django==4.2.7 djangorestframework==3.14.0 drf-yasg==1.21.7 stripe==7.4.0 python-decouple==3.8 django-cors-headers==4.3.0 requests==2.31.0
```

### 3. Create Django Project and App
```bash
django-admin startproject zac_motors .
python manage.py startapp api
```

### 4. Create .env File
Create a `.env` file in the root directory:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
STRIPE_SECRET_KEY=your-stripe-secret-key
STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key
PAYSTACK_SECRET_KEY=your-paystack-secret-key
PAYSTACK_PUBLIC_KEY=your-paystack-public-key
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Server
```bash
python manage.py runserver
```

---

## API Documentation URLs

Once the server is running, you can access the interactive API documentation:

### Swagger UI (Interactive)
🔗 **http://localhost:8000/swagger/**
- Interactive API documentation
- Test endpoints directly in the browser
- View request/response schemas
- Try out API calls with example data

### ReDoc (Clean Documentation)
🔗 **http://localhost:8000/redoc/**
- Clean, readable documentation
- Better for sharing with team members
- Print-friendly format
- Easier to navigate for reading

### OpenAPI Schema (JSON)
🔗 **http://localhost:8000/swagger.json**
- Raw OpenAPI 3.0 schema
- Can be imported into Postman, Insomnia, etc.

---

## API Endpoints Documentation

### Base URL
`http://localhost:8000/api/`

---

## Car Endpoints

### List All Cars
- **GET** `/api/cars/`
- **Query Parameters:**
  - `is_available=true/false`
  - `condition=new/used`

**Response:**
```json
{
  "count": 10,
  "results": [
    {
      "id": 1,
      "make": "Toyota",
      "model": "Camry",
      "year": 2024,
      "price": "28500.00",
      "condition": "new",
      "color": "Silver",
      "mileage": 0,
      "vin": "1HGBH41JXMN109186",
      "is_available": true
    }
  ]
}
```

### Get Single Car
- **GET** `/api/cars/{id}/`

### Create Car (Admin)
- **POST** `/api/cars/`

---

## Payment Endpoints (Paystack & Stripe)

### Initialize Paystack Payment
- **POST** `/api/payments/initialize_paystack/`

**Request Body:**
```json
{
  "car_id": 1,
  "amount": "28500.00",
  "email": "customer@example.com",
  "callback_url": "https://yoursite.com/verify-payment"
}
```

**Response:**
```json
{
  "status": true,
  "message": "Authorization URL created",
  "authorization_url": "https://checkout.paystack.com/xxxxx",
  "access_code": "xxxxx",
  "reference": "xxxxx"
}
```

### Verify Paystack Payment
- **POST** `/api/payments/verify_paystack/`

**Request Body:**
```json
{
  "reference": "xxxxx",
  "car_id": 1,
  "customer_name": "John Doe",
  "customer_phone": "+2348012345678"
}
```

**Response:**
```json
{
  "message": "Payment verified successfully",
  "data": {
    "id": 1,
    "car": 1,
    "customer_name": "John Doe",
    "customer_email": "customer@example.com",
    "amount": "28500.00",
    "status": "completed"
  }
}
```

### Create Stripe Payment Intent
- **POST** `/api/payments/create_payment_intent/`

**Request Body:**
```json
{
  "car_id": 1,
  "amount": "28500.00"
}
```

**Response:**
```json
{
  "client_secret": "pi_xxxxx_secret_xxxxx",
  "payment_intent_id": "pi_xxxxx"
}
```

### Confirm Stripe Payment
- **POST** `/api/payments/confirm_payment/`

**Request Body:**
```json
{
  "payment_intent_id": "pi_xxxxx",
  "car_id": 1,
  "customer_name": "John Doe",
  "customer_email": "john@example.com",
  "customer_phone": "+1234567890",
  "amount": "28500.00"
}
```

---

## Appointment Endpoints

### Book Appointment
- **POST** `/api/appointments/`

**Request Body:**
```json
{
  "customer_name": "Jane Smith",
  "customer_email": "jane@example.com",
  "customer_phone": "+2348012345678",
  "appointment_type": "showroom_visit",
  "appointment_date": "2024-12-01T14:00:00Z",
  "car": 1,
  "message": "I'm interested in test driving this vehicle"
}
```

**Response:**
```json
{
  "message": "Appointment booked successfully",
  "data": {
    "id": 1,
    "customer_name": "Jane Smith",
    "customer_email": "jane@example.com",
    "customer_phone": "+2348012345678",
    "appointment_type": "showroom_visit",
    "appointment_date": "2024-12-01T14:00:00Z",
    "car": 1,
    "status": "pending",
    "message": "I'm interested in test driving this vehicle"
  }
}
```

### List Appointments
- **GET** `/api/appointments/`
- **Query Parameters:**
  - `status=pending/confirmed/completed/cancelled`

### Confirm Appointment (Admin)
- **POST** `/api/appointments/{id}/confirm/`

### Cancel Appointment
- **POST** `/api/appointments/{id}/cancel/`

---

##  Contact Endpoints

### Send Contact Message
- **POST** `/api/contact/`

**Request Body:**
```json
{
  "name": "Mike Johnson",
  "email": "mike@example.com",
  "phone": "+2348012345678",
  "subject": "Question about financing",
  "message": "I'd like to know more about your financing options."
}
```

---

## Testing with cURL, Postman & DJango rest Framework environment 

### Initialize Paystack Payment
```bash
curl -X POST http://localhost:8000/api/payments/initialize_paystack/ \
  -H "Content-Type: application/json" \
  -d '{
    "car_id": 1,
    "amount": "5000000",
    "email": "customer@example.com"
  }'
```

### Verify Paystack Payment
```bash
curl -X POST http://localhost:8000/api/payments/verify_paystack/ \
  -H "Content-Type: application/json" \
  -d '{
    "reference": "your-paystack-reference",
    "car_id": 1,
    "customer_name": "John Doe",
    "customer_phone": "+2348012345678"
  }'
```
### Testing with Django framework env
Note: You can test these endpoints using Django's built-in test client or by creating test views and also your application must be running before this works. 

---
http://127.0.0.1:8000/api/contact/

### Book an Appointment
```bash
curl -X POST http://localhost:8000/api/appointments/ \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "customer_phone": "+2348012345678",
    "appointment_type": "showroom_visit",
    "appointment_date": "2024-12-01T14:00:00Z",
    "message": "Looking to buy a new car"
  }'
```

---

## Paystack Integration Guide

### Getting Paystack API Keys

1. Sign up at [paystack.com](https://paystack.com)
2. Complete your business verification
3. Navigate to Settings → API Keys & Webhooks
4. Copy your **Secret Key** and **Public Key**
5. Add them to your `.env` file

### Supported Currencies
- NGN (Nigerian Naira)
- GHS (Ghanaian Cedi)
- ZAR (South African Rand)
- USD (US Dollar)

### Payment Flow

1. **Initialize Transaction**: Call `/api/payments/initialize_paystack/`
2. **Redirect Customer**: Send customer to the `authorization_url` returned
3. **Customer Pays**: Customer completes payment on Paystack's secure checkout
4. **Verify Payment**: Call `/api/payments/verify_paystack/` with the reference
5. **Confirmation**: Payment is saved and car is marked as unavailable

### Webhook Setup (Optional but Recommended)

Add this to your views to handle Paystack webhooks:

```python
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import hmac
import hashlib

@csrf_exempt
def paystack_webhook(request):
    # Verify webhook signature
    signature = request.headers.get('x-paystack-signature')
    body = request.body
    
    hash = hmac.new(
        settings.PAYSTACK_SECRET_KEY.encode('utf-8'),
        body,
        hashlib.sha512
    ).hexdigest()
    
    if hash == signature:
        event = json.loads(body)
        if event['event'] == 'charge.success':
            # Handle successful payment
            reference = event['data']['reference']
            # Update your payment record
    
    return HttpResponse(status=200)
```

---

## Admin Panel
Access the Django admin panel at: `http://localhost:8000/admin/`

---

## Currency Notes

- **Stripe**: Uses USD by default (amount in cents)
- **Paystack**: Uses NGN by default (amount in kobo)
  - Change currency in the code: `"currency": "NGN"` → `"currency": "GHS"` etc.

---

## Next Steps

1. ✅ Test all endpoints using Swagger UI
2. ✅ Set up Paystack account and get API keys
3. ✅ Configure webhooks for automatic payment updates
4. ✅ Add email notifications for appointments
5. ✅ Implement user authentication if needed

