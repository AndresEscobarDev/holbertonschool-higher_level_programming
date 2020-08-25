#!/usr/bin/python3
"""  script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the body of
the response (decoded in utf-8) """


if __name__ == "__main__":
    from urllib import request, parse
    import sys

    email = parse.urlencode({'email': "{}"
                             .format(sys.argv[2])}).encode("utf-8")
    with request.urlopen(sys.argv[1], email) as response:
        print(response.read().decode("utf-8"))
