def filter_listing_queryset(self, queryset, queries):
    if queries.get("country"):
        queryset = queryset.filter(country__name=queries["country"])
    if queries.get("max_price"):
        queryset = queryset.filter(price__lte=queries["max_price"])
    if queries.get("min_price"):
        queryset = queryset.filter(price__gte=queries["min_price"])
    if queries.get("toilets"):
        queryset = queryset.filter(toilets_count__gte=queries["toilets"])
    if queries.get("beds"):
        queryset = queryset.filter(beds_count__gte=queries["beds"])
    if queries.get("guests"):
        queryset = queryset.filter(guests_count__gte=queries["guests"])
    if queries.get("pool"):
        queryset = queryset.filter(pool=True)
    if queries.get("pets"):
        queryset = queryset.filter(pets=True)
    if queries.get("parking"):
        queryset = queryset.filter(parking=True)
    return queryset
