'parsers': 
[<rest_framework.parsers.JSONParser object at 0x10dcbc710>, 
<rest_framework.parsers.FormParser object at 0x10dcbc780>, 
<rest_framework.parsers.MultiPartParser object at 0x10dcbccf8>], 
'authenticators': 
[<rest_framework_jwt.authentication.JSONWebTokenAuthentication object at 0x10dcbc828>, 
<rest_framework.authentication.SessionAuthentication object at 0x10dcbc978>, 
<rest_framework.authentication.BasicAuthentication object at 0x10dcbc908>], 
'negotiator': <rest_framework.negotiation.DefaultContentNegotiation object at 0x10dcbc588>, 
'parser_context': 
    {'view': <payment.api.views.PaymentAPICreateView object at 0x10dcbc390>, 
    'args': (), 
    'kwargs': {}, 
    'request': <rest_framework.request.Request object at 0x10dcbc940>, 
    'encoding': 'utf-8'}, 
    '_data': <QueryDict: 
            {'csrfmiddlewaretoken': ['4NjPFq6ljMFccYxbucB1VO6vgQj6L8sbKTiaZmAD0pBlnxlvYdOUbsApilFG75XD'], 
            'booking_id': ['1'], 
            'payment': ['KHJT67857']
            }
            >, 
            '_files': <MultiValueDict: {}>, 
            '_full_data': <QueryDict: {
                'csrfmiddlewaretoken': [
                    '4NjPFq6ljMFccYxbucB1VO6vgQj6L8sbKTiaZmAD0pBlnxlvYdOUbsApilFG75XD'
                    ],
                    'booking_id': ['1'], 'payment': ['KHJT67857']}>, '_content_type': <class 'rest_framework.request.Empty'>, '_stream': <WSGIRequest: POST '/api/payment/create'>, 'accepted_renderer': <rest_framework.renderers.BrowsableAPIRenderer object at 0x10dcbca20>, 'accepted_media_type': 'text/html', 'version': None, 'versioning_scheme': None, 'csrf_processing_done': True, '_authenticator': <rest_framework.authentication.SessionAuthentication object at 0x10dcbc978>, '_user': <SimpleLazyObject: <CustomUser: ahmedamedy@gmail.com>>, '_auth': None}