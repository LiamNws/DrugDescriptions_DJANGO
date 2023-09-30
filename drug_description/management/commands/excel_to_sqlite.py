import pandas as pd
from django.core.management.base import BaseCommand
from drug_description.models import Drug

class Command(BaseCommand):
    help = 'Load drug data from Excel into the database'

    def handle(self, *args, **kwargs):
        excel_file = 'C:/Users/liamn/IdeaProjects/TestSite/PT_portfolio/PT_portfolio/source/DrugDescriptions.xlsx'
        try:
            df = pd.read_excel(excel_file)
            for _, row in df.iterrows():
                # Map "TRUE" and "FALSE" to True and False respectively
                is_active = bool(row["Active Status"])
                
                drug, created = Drug.objects.get_or_create(
                    name=row['Drug Name'],
                    medicine_id=row['Medicine ID'],
                    is_active=is_active,
                    form=row['Form'],
                    shape=row['Shape'],
                    colour=row['Colour'],
                    imprint=row['Imprint']
                )

            self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error loading data: {e}'))
