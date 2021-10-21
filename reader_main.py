#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Includes methods to communicate with the Kathrein RFID-reader utilizing the matlab engine
"""

# https://de.mathworks.com/help/matlab/matlab-engine-for-python.html
import matlab.engine
import time


__author__ = "Miroslav Lach"
__copyright__ = "Copyright 2021, HOT"
__version__ = "1.0"
__email__ = "miroslav.lach@tum.de"


def show_return_message(flag):
    """
    Translate result flag into text message
    :param flag: returned flag to be matched with respective message
    :return:
    """
    try:
        flag_int = int(flag)
    except Exception:
        return
    result_flag_dict = {0: 'NoError',
                        1: 'NoData',
                        2: 'CRCError',
                        3: 'NoLicense',
                        4: 'OutOfRange',
                        5: 'NoStandard',
                        6: 'NoAntenna',
                        7: 'NoFrequency',
                        8: 'NoCarrier',
                        9: 'AntennaError',
                        10: 'NoTag',
                        11: 'MoreThanOneTagInField',
                        12: 'WrongLicenseKey',
                        13: 'FWRejected',
                        14: 'WrongCFM',
                        15: 'NoHandle',
                        16: 'NoProfile',
                        128: 'NonSpecified'}
    print('reader message: ' + result_flag_dict[int(flag_int)] + ' [' + str(int(flag_int)) + ']')


def rfid_reader_init(mode, power):
    """
    This function starts up the matlab engine and initializes the reader
    :param mode: mode [0, 1] NormalMode = 0 (required for EPC scan) / DirectMode = 1 (for direct carrier)
    :param power: power per port in dBm
    :return obj: returns the handler instance
    """
    eng = matlab.engine.start_matlab()
    obj = eng.reader_init(mode, power)  # mode [0, 1], power in dBm
    return eng, obj


def rfid_reader_start(eng, obj):
    """
    Start to emit the carrier
    :param eng: engine handler
    :param obj: instance
    :return:
    """
    result_flag = eng.reader_on(obj)
    show_return_message(result_flag)


def rfid_reader_stop(eng, obj):
    """
    Deactivate the carrier
    :param eng: engine handler
    :param obj: instance
    :return:
    """
    result_flag = eng.reader_off(obj)
    show_return_message(result_flag)


def rfid_reader_engine_disconnect(eng, obj):
    """
    Disconnect the reader and close matlab engine
    :param eng: engine handler
    :param obj: instance
    :return:
    """
    stat = eng.reader_disconnect(obj)
    print(stat)
    eng.quit()



def rfid_scan4tags(eng, obj):
    """
    Scans for available RFID-tags (found tags are saved into txt-file)
    :param eng: engine handler
    :param obj: instance
    :return:
    """
    result_flag = eng.scan_tags(obj)
    show_return_message(result_flag)
    if result_flag == 0.0 or result_flag == 10.0:
        print('Scan4Tags: no tags found.')
    else:
        tag_count = str(result_flag).split(',')[1].replace('[', '').replace(']', '')
        print('Scan4Tags: ' + tag_count.split('.')[0] + ' tags found!')


if __name__ == '__main__':
    # emit carrier only
    # eng, obj = rfid_reader_init(1, 20)  # mode [0, 1], power [dBm]
    # rfid_reader_start(eng, obj)
    # time.sleep(5)  # wait 5 secs
    # rfid_reader_stop(eng, obj)
    # rfid_reader_engine_disconnect(eng, obj)

    # scan for tags
    eng, obj = rfid_reader_init(0, 22)  # mode [0, 1], power [dBm]
    rfid_scan4tags(eng, obj)
    rfid_reader_engine_disconnect(eng, obj)
















