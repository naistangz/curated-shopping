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
