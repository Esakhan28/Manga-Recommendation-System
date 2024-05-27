import csv
from django.core.management.base import BaseCommand
from manga.models import Mangacard

class Command(BaseCommand):
    help = 'Load books data into the database'

    def handle(self, *args, **kwargs):
        file_path = "C:/Users/ABHINDHIRA/OneDrive/Documents/book-recommender-system/book-recommender-system/Books.csv"  # Update with your actual file path
        batch_size = 1000  # Define a batch size
        books = []

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for idx, row in enumerate(reader):
                try:
                    book = Mangacard(
                        isbn=row['isbn'],  # Treat ISBN as a string
                        title=row['title'],
                        author=row['author'],
                        year_of_publication=int(row['year_of_publication']),
                        publisher=row['publisher'],
                        image_url=row['image_url']
                    )
                    books.append(book)

                    if (idx + 1) % batch_size == 0:
                        Mangacard.objects.bulk_create(books)
                        books = []  # Clear the list to start the next batch
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error processing row {idx + 1}: {e}"))

            # Insert the remaining data
            if books:
                Mangacard.objects.bulk_create(books)

        self.stdout.write(self.style.SUCCESS('Successfully loaded books data'))
