# Gas_utility

## 🚀 Getting Started

- Python 3.8+
- pip
- virtualenv (optional, but recommended)

### ⚙️ Setup

```bash
# Clone the repo
git clone https://github.com/your-username/gas-utility.git
cd gas-utility

# Create virtual environment
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser for admin login
python manage.py createsuperuser

# Start the server
python manage.py runserver


#Authentications
Login to the Django admin at: http://127.0.0.1:8000/admin/
REST API supports session-based login via /api-auth/


## API ENDPOINTS
- Base Url
App	         Prefix
Customer	 /customer/
Support	     /support/

-Customer APIs

Method	             Endpoint	                            Description
GET	                /customer/customers/	                List all customers
POST	            /customer/customers/	                Create a new customer
GET	                /customer/customers/<id>/	            Retrieve a customer by ID
PUT             	/customer/customers/<id>/	            Full update
PATCH	            /customer/customers/<id>/	            Partial update
DELETE	            /customer/customers/<id>/	            Delete a customer



 Service Request Endpoints
Method	                  Endpoint	                                           Description
GET	                     /customer/service-requests/	                     List all service requests
POST	                 /customer/service-requests/	                     Create a new service request
GET	                     /customer/service-requests/<id>/	                 Retrieve a service request by ID
PUT	                     /customer/service-requests/<id>/	                 Full update of a service request
PATCH	                 /customer/service-requests/<id>/	                 Partial update
DELETE	                 /customer/service-requests/<id>/	                 Delete a service request


#   Testing with Postman