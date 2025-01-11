from django.db.models import Q
from django.core.paginator import Paginator

def get_transactions(month, page=1, per_page=10, search_text=''):
    """
    Retrieves product transactions for a given month, 
    with optional search and pagination.

    Args:
        month (int): Month of the year (1-12)
        page (int, optional): Page number. Defaults to 1.
        per_page (int, optional): Items per page. Defaults to 10.
        search_text (str, optional): Search query. Defaults to ''.

    Returns:
        Paginator: Paginated queryset of ProductTransaction objects
    """
    query = ProductTransaction.objects.filter(date_of_sale__month=month)

    if search_text:
        query = query.filter(
            Q(title__icontains=search_text) | 
            Q(description__icontains=search_text) | 
            Q(category__icontains=search_text)  # Added category search
        )

    paginator = Paginator(query, per_page)
    return paginator.get_page(page)