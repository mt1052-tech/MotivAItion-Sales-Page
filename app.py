from flask import Flask, request, jsonify, render_template
import stripe

app = Flask(__name__, static_folder='static', template_folder='templates')

stripe.api_key = "sk_test_..."  # Dein Stripe Secret Key hier

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'eur',
                    'unit_amount': 990,
                    'product_data': {'name': '50 KI-LIFEHACKS E-Book'}
                },
                'quantity': 1
            }],
            mode='payment',
            success_url='https://deineseite.de/success',
            cancel_url='https://deineseite.de/cancel'
        )
        return jsonify({'id': session.id})
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(port=4242, debug=True)