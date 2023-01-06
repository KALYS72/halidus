from urls import urlpatterns

while True:
    input_url = input('input url: ')
    found = False
    for url, view in urlpatterns:
        if url == input_url:
            foudfnd = True
            try:
                view()
            except Exception as e:
                print(e)
    if not found:
        print(f'404: url not found')


