import time

from app.logger import logger


async def log_requests(request, call_next):
    endpoint = request.url.path
    params = dict(request.query_params)
    user_agent = dict(request.headers).get("user-agent", "<no-user-agent>")
    ip_address = request.client.host

    start = time.perf_counter()
    response = await call_next(request)
    duration = round(time.perf_counter() - start, 2)

    response_code = response.status_code

    message = (f"Endpoint: {endpoint} | params: {params}, user_agent: {user_agent} |"
               f" ip_address: {ip_address} | response_code: {response_code} | duration: {duration}")
    logger.info(message)
    return response
