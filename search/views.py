import json

import requests
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .forms import SearchForm

# This variable maps a search type to the name of the key containing search
# results. It's immutable because it should change - the Spotify API _should_
# be stable.
RESULT_KEY_MAP = (
    ('artist', 'artists',),
    ('album', 'albums',),
    ('playlist', 'playlists',),
    ('track', 'tracks',),
)


def search_index(request):
    results = None
    result_count = None

    # We will lose the POST data every time we use pagination
    # One way of keeping this data is to add it to a session
    # Make sure we only add this data when we're actually using pagination
    # ('page' in request.GET)
    if not request.method == 'POST' and 'page' in request.GET:
        if 'search-post' in request.session:
            request.POST = request.session['search-post']
            request.method = 'POST'

    if request.method == 'POST':
        form = SearchForm(request.POST)
        request.session['search-post'] = request.POST

        if form.is_valid():
            search_type = form.cleaned_data['search_type']
            search_string = form.cleaned_data['search_string']
            response = requests.get(
                '{}={}&type={}&limit={}'
                .format(
                    settings.SPOTIFY_BASE_URL, search_string, search_type,
                    settings.SPOTIFY_LIMIT
                )
            )
            # Deal with any strange responses from Spotify
            response.raise_for_status()
            if response.status_code == 200:
                response_content = json.loads(
                    response.content.decode('utf-8')
                )
                print(response_content)
                result_key = dict(RESULT_KEY_MAP)[search_type]
                search_results = response_content[result_key]['items']
                result_count = response_content[result_key]['total']

                paginator = Paginator(
                    search_results, settings.SEARCH_RESULTS_PER_PAGE
                )

                page = request.GET.get('page')
                try:
                    results = paginator.page(page)
                except PageNotAnInteger:
                    results = paginator.page(1)
                except EmptyPage:
                    results = paginator.page(paginator.num_pages)
    else:
        form = SearchForm()

    print(results)

    context = {
        'search_results': results,
        'form': form,
        'result_count': result_count,
        'search_limit': settings.SPOTIFY_LIMIT
    }
    return render(request, 'search.html', context)
