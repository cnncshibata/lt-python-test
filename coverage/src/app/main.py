def parse(http_status_code: int) -> str:
    if 100 <= http_status_code < 200:
        return 'Informational'
    elif 200 <= http_status_code < 300:
        return 'Success'
    elif 300 <= http_status_code < 400:
        return 'Redirection'
    elif 400 <= http_status_code < 500:
        return 'ClientError'
    elif 500 <= http_status_code < 600:
        return 'ServerError'
    else:
        raise Exception(f'Invalid status code: {http_status_code}')
