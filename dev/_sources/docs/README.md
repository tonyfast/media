# `/docs` for media

all published content is managed in this directory.

## publishing a document

1. [submitting new media](submit.md)
2. [reviewing a document](review.md)
3. [final touches](publish.md)



## the folder pattern
    
the folder pattern is meant to be valid python names and descriptive datetime names.

    pattern = '{roman_format}/{full_lowercase_month}'.format(
        roman_format="mmxxi",
        full_lowercase_month="september"
    )