from aiohttp import web
from atm_manager import Atm, count_coins


async def create_atm(app):
    app['atm'] = Atm()


async def get_cash_handler(request):
    try:
        content = await request.json()
    except Exception:
        data = {'message': 'Json is not valid!'}
        return web.json_response(data=data, status=400)
    else:
        requested_cash = content.get('amount')
        if not requested_cash:
            data = {'message': 'There is no amount in json.'}
            return web.json_response(data=data, status=400)
        else:
            requested_cash = float(requested_cash)
            if requested_cash > 0:
                if requested_cash > 2000:
                    data = {'message': 'Exceeded the limit!'}
                    return web.json_response(data=data, status=400)
                result = app['atm'].count(requested_cash)
                if isinstance(result, list):
                    coins = count_coins(result)
                    # print(result)
                    if coins > 50:
                        data = {'message': 'ToMuchCoinsException'}
                        return web.json_response(data=data, status=400)
                    else:
                        data = {'result': result}
                        return web.json_response(data=data, status=200)
                else:
                    data = {'message':
                                'With no loving in our '
                                'souls And no money in our coats.',
                            'Max current amount available for the withdrawal': result}
                    return web.json_response(data=data, status=409)
            else:
                data = {'message': 'Wrong amount'}
                return web.json_response(data=data, status=400)


async def add_cash_handler(request):
    try:
        content = await request.json()
    except Exception as e:
        print(e)
        data = {'message': 'Json is not valid!'}
        return web.json_response(data=data, status=400)
    else:
        cash = content.get('cash')
        app['atm'].put_money(cash)
        data = {'message': 'Money was added successfully'}
        return web.json_response(data=data, status=200)


if __name__ == '__main__':
    app = web.Application()
    app.router.add_post('/atm/withdrawal', get_cash_handler)
    app.router.add_put('/atm/refill', add_cash_handler)
    app.on_startup.append(create_atm)
    web.run_app(app, host='127.0.0.1', port=8080)