from django.shortcuts import render
from django.utils import timezone
from .forms import BandForm
from .models import Band, Concert
from internetarchive import get_session
from dateutil.parser import parse

# Create your views here.
def index(request):
    results = []
    form = BandForm(request.GET or None)

    print(f"Request GET data: {request.GET}")
    print(f"Form valid? {form.is_valid()}")

    if form.is_valid():
        band = form.cleaned_data['band']
        Concert.objects.filter(band=band).delete()
        concerts = Concert.objects.filter(band=band)

        if not concerts.exists():
            Concert.objects.filter(band=band).delete()
            session = get_session()
            session.mount_http_adapter()
            query = f"{band.band_name} live"
            search = session.search_items(query)

            print(f"CHECK SEARCH:")
            print(f"search: {search}")

            for item in search:
                identifier = item['identifier']
                item_obj = session.get_item(identifier)
                meta = item_obj.metadata
                publication_date = timezone.now()
                public_date_str = meta.get('publicdate')
                try:
                    public_date = parse(public_date_str)
                    print(f'public_date: {public_date}')
                except:
                    public_date = timezone.now()
                try: 
                    files = list(item_obj.get_files())
                except Exception as e:
                    print(f"Error fetching files for {identifier}: {e}")
                    continue

                print(f"CHECKING FILES!")
                flac_files = [f.name for f in files if f.name.lower().endswith('.flac')]
                print(f"Checking {identifier}: Found FLAC files: {flac_files}")

                if flac_files:
                    concert = Concert.objects.create(
                        internet_archive_identifier=identifier,
                        band=band,
                        publication_date=publication_date,
                        flac_present=True
                    )
        
            concerts = Concert.objects.filter(band=band)

        print(f"CHECK")
        print(f"Found {concerts.count()} concerts for band {band.band_name}")
        for concert in concerts:
            print(f"concert: {concert}")
            entry = {'title': concert.internet_archive_identifier}
            if concert.flac_present:
                entry['flac_url'] = f"https://archive.org/compress/{concert.internet_archive_identifier}/formats=FLAC&file=/{concert.internet_archive_identifier}.zip"
            results.append(entry)

    return render(request, 'concertdownloader/index.html', {'form': form, 'results': results})