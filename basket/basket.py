class Basket():
    """
    Base basket class to provide default behaviour 
    from which child classes can inherit or override
    """

    def __init__(self, request):

        self.session = request.session
        basket = self.session.get('session_key')
        if 'session' not in request.session:
            basket = self.session['session_key'] = {}
        self.basket = basket

    def add(self, product, product_qty):
        """
        Adding and updating the users' basket session data
        """
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {
                'price': str(product.price),
                'quantity': int(product_qty)
            }

        self.session.modified = True
