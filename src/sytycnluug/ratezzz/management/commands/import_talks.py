import sys
import csv

from django.core.management.base import NoArgsCommand

from ...models import Talk

import logging
logger = logging.getLogger(__file__)


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        reader = csv.reader(sys.stdin)

        for entry in reader:
            talk, is_created = Talk.objects.get_or_create(name=entry[1],
                speakers=entry[2])

            if is_created:
                logger.info('Added: {0!s}'.format(talk))
            else:
                logger.info('Skipped: {0!s}'.format(talk))
