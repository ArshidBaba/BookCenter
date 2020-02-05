from django.db import models
import uuid

# class Query(models.Model):
#     query_text = models.TextField(max_length=300, help_text='Writ your query')

    # def __str__(self):
    #     return self.query_text

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100, primary_key=True, default='')
    # last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['name']

    # def __str__(self):
    #     return f'{self.last_name}, {self.first_name}'
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="author", on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(max_length=13, help_text='13 Character ISBN number</a>', blank=True)
    genre = models.ManyToManyField(Genre, related_name="genres", help_text='Select a genre for this book')

    def __str__(self):
        return self.title

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey(Book, related_name="book_inst", on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)  

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book Availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'