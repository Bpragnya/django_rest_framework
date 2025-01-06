from django.db.models import Q

class Helpers():
    def apply_mime_type_filter(queryset,mime_type):
        """Apply MIME type filters to the given queryset."""
        if mime_type:
            mime_types = mime_type.split(',')
            mime_types_filters = Q()
            for m in mime_types:
                mime_types_filters |= Q(mime_type__icontains=m.strip())
            return queryset.filter(mime_types_filters)
        return queryset
    
    def apply_subject_filter(queryset, subject):
        if subject:
            subjects = subject.split(',')  # Assuming comma-separated values for topics
            subject_filters = Q()
            for s in subjects:
                subject_filters |= Q(subject__name__icontains=s.strip())
            return queryset.filter(subject_filters)
        return queryset
    
    def apply_bookshelf_filter(queryset, bookshelf):
        if bookshelf:
            bookshelves = bookshelf.split(',')  # Assuming comma-separated values for bookshelves
            bookshelf_filters = Q()
            for bs in bookshelves:
                bookshelf_filters |= Q(bookshelf__name__icontains=bs.strip())
            return queryset.filter(bookshelf_filters)
        return queryset
        
    def apply_language_filter(queryset, language):
        if language:
            languages = language.split(',')  # Assuming comma-separated values for language
            language_filters = Q()
            for l in languages:
                language_filters |= Q(language__code__icontains=l.strip())
            return queryset.filter(language_filters)
        return queryset

    def apply_author_filter(queryset, author):
        if author:
            authors = author.split(',')  # Assuming comma-separated values for authors
            author_filters = Q()
            for a in authors:
                author_filters |= Q(author__name__icontains=a.strip())
            return queryset.filter(author_filters)
        return queryset