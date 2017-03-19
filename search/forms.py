from django import forms

SEARCH_TYPES = (
    ('album', 'Album',),
    ('artist', 'Artist',),
    ('playlist', 'Playlist',),
    ('track', 'Track',),
)


class SearchForm(forms.Form):
    search_type = forms.ChoiceField(label='Filter', required=True,
                                    choices=SEARCH_TYPES)
    search_string = forms.CharField(label='', max_length='100')
