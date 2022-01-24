# This example sets up an endpoint using the Flask framework.
# Watch this video to get started: https://youtu.be/7Ul1vfmsDck.

import imp
import os
import stripe
from django.conf import settings
from rest_framework.views import APIView
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeCheckoutView(APIView):
  def post(self, request):
    try:
      session = stripe.checkout.Session.create(
          line_items=[{
              'price': 'price-------------',
              'quantity': 1,
          }, ],
          mode='payment',
          success_url=settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
          cancel_url=settings.SITE_URL + '/?cancelled=true',
      )
      return redirect(session.url)
    except:
      return Response(
          {'error': 'something went wrong creating stripe checkout session'},
          status=status.HTTP_500_INTERNAL_SERVER_ERROR
      )
