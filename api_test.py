import io, pycurl
import _constants as const


if __name__ == '__main__':
    buffer = io.BytesIO()
    curl = pycurl.Curl()
    curl.setopt(curl.URL, const.ENDPOINT)
    curl.setopt(curl.WRITEDATA, buffer)
    curl.perform()
    curl.close()

    body = buffer.getvalue()
    print(body.decode(const.ENCODING))
