import base64
from datetime import datetime
import json

from django.http import HttpResponseForbidden, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from holodeck.models import Metric, Sample


@csrf_exempt
def store(request):
    """
    Main API method storing pushed data.
    TODO: Needs a lot of work, security, validation etc.
    """
    if request.method == 'POST':
        data = request.body
        data = json.loads(base64.b64decode(data).decode('zlib'))

        # Get the Metric for provided api_key, otherwise fail with Forbidden.
        try:
            metric = Metric.objects.get(api_key=data['api_key'])
        except Metric.DoesNotExist:
            return HttpResponseForbidden()

        timestamp = datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S')

        for sample in data['samples']:
            # Samples overide on metric, string and timestamp values.
            sample_obj, created = Sample.objects.get_or_create(
                metric=metric,
                string_value=sample[0],
                timestamp=timestamp
            )
            sample_obj.integer_value = sample[1]
            sample_obj.save()

    return HttpResponse()
