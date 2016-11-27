class Matcher:
    def __init__(self, routes):
        self._routes = routes

    def match_request(self, request):
        for route in self._routes:
            rest = request.path

            for typ, data in route.segments:
                if typ == 'exact':
                    if not rest.startswith(data):
                        break

                    rest = rest[len(data):]
                elif typ == 'placeholder':
                    value, slash, rest = rest.partition('/')
                    rest = slash + rest
                else:
                    assert 0, 'Unknown type'

            if not rest:
                if route.methods and request.method not in route.methods:
                    continue

                return route
