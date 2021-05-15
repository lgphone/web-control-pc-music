import asyncio
import uvicorn
import socket
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.responses import JSONResponse
import pyautogui

app_run_port = 8088
app_run_host = "0.0.0.0"

templates = Jinja2Templates(directory='templates')
app = Starlette()
app.mount('/static', StaticFiles(directory='statics'), name='static')


async def press_key_board(key_code):
    def _press_keyboard():
        pyautogui.press(key_code)

    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(
        None, _press_keyboard)
    return result


async def get_local_ip():
    def _func():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip_addr = s.getsockname()[0]
        finally:
            s.close()

        return ip_addr

    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, _func)


@app.on_event('startup')
async def startup_do():
    local_ip = await get_local_ip()
    print(f"{'*' * 10} | {'*' * 10}")
    print(f"{'*' * 10} | {'*' * 10}")
    print("  Web Control PC Music")
    print(f"{'*' * 10} | {'*' * 10}")
    print(f"{'*' * 10} | {'*' * 10}")
    print(f" 请使用手机浏览器访问\n {local_ip}:{app_run_port}")
    print(f"{'*' * 10} | {'*' * 10}")
    print(f"{'*' * 10} | {'*' * 10}")
    print(f"{'*' * 10} | {'*' * 10}")


@app.route('/')
async def index(request):
    template = "index.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)


@app.route('/api/music')
async def music_control_api(request):
    action = request.query_params.get('action')
    if action not in ['playpause', 'next', 'prev']:
        return JSONResponse({'status': 1, 'msg': f'控制指令: {action} 非法!'})

    action_key_code_map = {
        'playpause': 'playpause',
        'next': 'nexttrack',
        'prev': 'prevtrack',
    }

    await press_key_board(action_key_code_map[action])
    return JSONResponse({'status': 0})


@app.route('/api/volume')
async def volume_control_api(request):
    action = request.query_params.get('action')
    if action not in ['up', 'down', 'mute']:
        return JSONResponse({'status': 1, 'msg': f'音量控制指令: {action} 非法!'})

    action_key_code_map = {
        'up': 'volumeup',
        'down': 'volumedown',
        'mute': 'volumemute'
    }

    await press_key_board(action_key_code_map[action])
    return JSONResponse({'status': 0})


@app.exception_handler(404)
async def not_found(request, exc):
    """
    Return an HTTP 404 page.
    """
    template = "404.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=404)


@app.exception_handler(500)
async def server_error(request, exc):
    """
    Return an HTTP 500 page.
    """
    template = "500.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=500)


if __name__ == "__main__":
    uvicorn.run(app, host=app_run_host, port=app_run_port, access_log=False)
