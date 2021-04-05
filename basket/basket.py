from decimal import Decimal


class Basket():
    """
    Base basket class to provide default behaviour 
    from which child classes can inherit or override
    - If a session does not exist, create a session (aka creating a cookie containing unique session id)
    """

    def __init__(self, request):

        self.session = request.session
        basket = self.session.get('session_key')
        if 'session' not in request.session:
            basket = self.session['session_key'] = {}
        self.basket = basket

    def __len__(self):
        """
        Get basket data and count the quantity of items
        """
        return sum(item['quantity'] for item in self.basket.values())

    def add(self, product, qty):
        """
        Adding and updating the users' basket session data
        """
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {
                'price': str(product.price),
                'quantity': int(qty)
            }

        self.session.modified = True

    def update(self, product, qty):
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, product):
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def save(self):
        self.session.modified = True

