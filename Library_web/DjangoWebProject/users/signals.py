# Set permissions for staff members
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from Catalog.models import Book
from management.models import BorrowBook

User = get_user_model()

@receiver(post_save, sender=User)
def assign_permissions_to_staff(sender, instance, created, **kwargs):
    if created and instance.is_staff and not instance.is_superuser:
        permissions_to_add = []

        # Permissions for Book
        book_ct = ContentType.objects.get_for_model(Book)
        permissions_to_add += Permission.objects.filter(
            content_type=book_ct,
            codename__in=['add_book', 'change_book', 'view_book']
        )

        # Permissions for BorrowBook
        borrow_ct = ContentType.objects.get_for_model(BorrowBook)
        permissions_to_add += Permission.objects.filter(
            content_type=borrow_ct,
            codename__in=['add_borrowbook', 'change_borrowbook', 'view_borrowbook', 'delete_borrowbook']
        )

        # Permissions to add users
        user_ct = ContentType.objects.get_for_model(User)
        permissions_to_add += Permission.objects.filter(
            content_type=user_ct,
            codename__in=['add_customuser', 'change_customuser', 'view_customuser']
        )

        for perm in permissions_to_add:
            instance.user_permissions.add(perm)



