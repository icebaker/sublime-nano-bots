import time
import threading
import http.client
import json
from urllib.parse import urlsplit

import sublime

from .nanobot_state import NanoBotState


class NanoBot:
    @staticmethod
    def stop():
        NanoBotState.instance().stop()

    @staticmethod
    def perform(config, params, callback):
        cartridge = NanoBot.cartridge(config, params['cartridge'])

        NanoBot.stop()

        if config['NANO_BOTS_STREAM']:
            threading.Thread(
                target=NanoBot.stream_request,
                args=(config, params, cartridge, callback)).start()
        else:
            threading.Thread(
                target=NanoBot.non_stream_request,
                args=(config, params, cartridge, callback)).start()

    @staticmethod
    def cartridges(config):
        response = NanoBot.send_request(
            config, None, 'GET', '/cartridges',
            None, None, 1)
        return response

    @staticmethod
    def cartridge(config, cartridge_id):
        return NanoBot.send_request(
            config, {'id': cartridge_id},
            'POST', '/cartridges/source')

    @staticmethod
    def non_stream_request(config, params, cartridge, callback):
        def thread_callback(response):
            if NanoBotState.instance().state['status'] != 'stopped':
                NanoBotState.instance().update(
                    cartridge, {'status': 'finished', 'thread': None})
                callback(response)

        thread_event = threading.Event()

        thread = threading.Thread(
            target=NanoBot.send_request,
            args=(config, params, 'POST', '/cartridges',
                  thread_callback, thread_event))

        NanoBotState.instance().update(
            cartridge,
            {'status': 'pending', 'started_at': time.time(),
             'thread': thread_event})

        thread.start()

    @staticmethod
    def stream_request(config, params, cartridge, callback):
        NanoBotState.instance().update(
            cartridge,
            {'status': 'pending', 'started_at': time.time(), 'thread': None})

        response = NanoBot.send_request(
            config, params, 'POST', '/cartridges/stream')

        stream_id = response.get('id', '')
        if not stream_id:
            sublime.error_message('No Stream ID received.');
            return

        state = ''

        while NanoBotState.instance().state['status'] != 'stopped':
            response = NanoBot.send_request(
                config, None, 'GET', '/cartridges/stream/' + stream_id)
            output = response.get('output')

            if state != output:
                response['fragment'] = output[len(state):]
                state = output
                callback(response)

            if response.get('state') == 'finished':
                NanoBotState.instance().update(
                    cartridge, {'status': 'finished', 'thread': None})

                break

        response['fragment'] = ''
        callback(response)

    @staticmethod
    def send_request(
        config, params, method, path,
        thread_callback=None, thread_event=None, timeout=None
    ):
        try:
            hostname, port = NanoBot.get_host_port(
                config['NANO_BOTS_API_ADDRESS'])
            url = NanoBot.get_url(config['NANO_BOTS_API_ADDRESS'], path)
            conn = NanoBot.create_connection(hostname, port, timeout)
            headers = NanoBot.create_headers(config)
            json_str = NanoBot.create_json(params)

            conn.request(method, url, json_str, headers)
            response = NanoBot.get_response(conn)
            conn.close()

            if thread_callback is not None and thread_event is not None:
                if not thread_event.is_set():
                    thread_callback(response)

            return response
        except Exception as error:
            sublime.error_message(
                'Error: {} - {}'.format(
                    config['NANO_BOTS_API_ADDRESS'], str(error)))

            return {}

    @staticmethod
    def get_host_port(api_address):
        parsed_url = urlsplit(api_address)
        hostname = parsed_url.hostname
        port = parsed_url.port or 80  # Default port if not specified
        return hostname, port

    @staticmethod
    def get_url(api_address, path):
        return api_address + path

    @staticmethod
    def create_connection(hostname, port, timeout):
        return http.client.HTTPConnection(hostname, port, timeout=timeout)

    @staticmethod
    def create_headers(config):
        return {
        'Content-type': 'application/json',
        'NANO_BOTS_USER_IDENTIFIER': 'sublime-text/' + config['NANO_BOTS_USER_IDENTIFIER']}

    @staticmethod
    def create_json(params):
        return json.dumps(params)

    @staticmethod
    def get_response(conn):
        response = conn.getresponse()
        output = {}
        if response.status == 200:
            try:
                output = json.loads(response.read().decode())
            except json.JSONDecodeError:
                output = {'output': 'Invalid JSON response.'}
        else:
            output = {
                'output': 'Request failed with status code: {}'.format(
                    response.status)}
        return output
