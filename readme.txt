cd Axians_smart_support

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the app using Gunicorn
gunicorn -b 0.0.0.0:5000 run:app
